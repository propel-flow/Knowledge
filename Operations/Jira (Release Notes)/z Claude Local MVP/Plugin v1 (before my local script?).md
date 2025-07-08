# Jira Plugin Wrapper Development Path

## Decision Point: Choose Your Plugin Architecture

You have 3 main options for Jira plugin development:

### **Option 1: Atlassian Forge (Recommended for MVP)**

- **Pros**: Official platform, built-in hosting, easy deployment
- **Cons**: Some limitations, newer ecosystem
- **Best for**: Quick MVP, official support

### **Option 2: Atlassian Connect**

- **Pros**: More flexibility, can use your own infrastructure
- **Cons**: Need to host yourself, more complex
- **Best for**: Custom requirements, existing infrastructure

### **Option 3: Browser Extension + Webhooks**

- **Pros**: Maximum flexibility, works with any Jira instance
- **Cons**: Users need to install extension
- **Best for**: Rapid prototyping, internal teams

## **Recommended Path: Start with Forge**

Based on your requirements, I recommend starting with **Atlassian Forge** because:

- Built-in hosting (no AWS setup needed initially)
- Integrates with your existing Python logic
- Easy to deploy and test
- Can migrate to Connect later if needed

---

# Step-by-Step Forge Plugin Development

## Step 1: Forge Setup

### **Install Forge CLI**

```bash
# Install Forge CLI
npm install -g @forge/cli

# Login to Atlassian
forge login

# Verify installation
forge --version
```

### **Create Your Plugin Project**

```bash
# Create new Forge app
forge create jira-doc-intelligence

# Choose template: "jira-issue-panel" (gives you issue-level integration)
cd jira-doc-intelligence

# Install dependencies
npm install
```

## Step 2: Plugin Structure Setup

### **src/index.js** - Main Plugin Entry Point

```javascript
import Resolver from '@forge/resolver';
import api, { route } from '@forge/api';

const resolver = new Resolver();

// Main resolver for processing Jira issues
resolver.define('processIssue', async (req) => {
  const { issueKey } = req.payload;
  
  try {
    // Get issue data from Jira API
    const issueResponse = await api.asApp().requestJira(route`/rest/api/3/issue/${issueKey}`, {
      headers: {
        'Accept': 'application/json'
      }
    });
    
    const issue = await issueResponse.json();
    
    // Process with your AI logic (adapted from your Python code)
    const processedData = await processIssueWithAI(issue);
    
    return {
      success: true,
      data: processedData
    };
    
  } catch (error) {
    console.error('Error processing issue:', error);
    return {
      success: false,
      error: error.message
    };
  }
});

// AI processing function (adapted from your Python code)
async function processIssueWithAI(issue) {
  const basicInfo = {
    key: issue.key,
    summary: issue.fields.summary,
    status: issue.fields.status.name,
    type: issue.fields.issuetype.name,
    priority: issue.fields.priority?.name || 'Unknown',
    resolution: issue.fields.resolution?.name || 'Unresolved',
    description: issue.fields.description || 'No description provided',
    created: issue.fields.created,
    updated: issue.fields.updated
  };

  // Call external AI service (your Python API or OpenAI directly)
  const aiAnalysis = await generateAIContent(basicInfo);
  
  return {
    ...basicInfo,
    aiAnalysis
  };
}

// AI content generation (calls external service or OpenAI)
async function generateAIContent(issueData) {
  // Option 1: Call your Python API (if hosted)
  // Option 2: Call OpenAI directly from Forge
  // Option 3: Use Forge's external API capabilities
  
  // For now, let's call OpenAI directly
  const openaiResponse = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini',
      messages: [{
        role: 'user',
        content: `Extract symptom and condition for release notes from this Jira issue:
        
        Summary: ${issueData.summary}
        Description: ${issueData.description}
        
        Return JSON with: {"symptom": "...", "condition": "...", "category": "..."}`
      }],
      max_tokens: 300,
      temperature: 0.3
    })
  });
  
  const result = await openaiResponse.json();
  
  try {
    return JSON.parse(result.choices[0].message.content);
  } catch (e) {
    return {
      symptom: "AI processing failed",
      condition: "Unable to extract condition",
      category: "unknown"
    };
  }
}

// Batch processing resolver
resolver.define('processBatch', async (req) => {
  const { jql, maxResults = 20 } = req.payload;
  
  try {
    const searchResponse = await api.asApp().requestJira(route`/rest/api/3/search`, {
      headers: {
        'Accept': 'application/json'
      },
      params: {
        jql,
        maxResults,
        fields: 'summary,description,status,priority,issuetype,created,updated,resolution'
      }
    });
    
    const searchResults = await searchResponse.json();
    
    const processedIssues = [];
    for (const issue of searchResults.issues) {
      const processed = await processIssueWithAI(issue);
      processedIssues.push(processed);
    }
    
    return {
      success: true,
      totalFound: searchResults.total,
      processed: processedIssues.length,
      data: processedIssues
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
});

export const handler = resolver.getDefinitions();
```

### **src/frontend/index.jsx** - UI Component

```jsx
import React, { useState, useEffect } from 'react';
import { invoke } from '@forge/bridge';

function App() {
  const [issueData, setIssueData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [processing, setProcessing] = useState(false);

  useEffect(() => {
    // Get current issue context
    invoke('view.getContext').then(context => {
      const issueKey = context.extension.issue.key;
      processCurrentIssue(issueKey);
    });
  }, []);

  const processCurrentIssue = async (issueKey) => {
    setProcessing(true);
    try {
      const result = await invoke('processIssue', { issueKey });
      setIssueData(result.data);
    } catch (error) {
      console.error('Processing failed:', error);
    } finally {
      setProcessing(false);
      setLoading(false);
    }
  };

  const runBatchProcess = async () => {
    setProcessing(true);
    try {
      // Use your JQL queries from Python code
      const jql = 'issuetype in (Bug, Defect) AND status in (Closed, Resolved) AND resolution in (Fixed, Done) ORDER BY priority DESC';
      const result = await invoke('processBatch', { jql, maxResults: 10 });
      console.log('Batch processing result:', result);
      // Handle batch results (maybe show in modal or new view)
    } catch (error) {
      console.error('Batch processing failed:', error);
    } finally {
      setProcessing(false);
    }
  };

  if (loading) {
    return <div>Loading issue data...</div>;
  }

  return (
    <div style={{ padding: '16px' }}>
      <h3>Documentation Intelligence</h3>
      
      {issueData && (
        <div>
          <h4>{issueData.key} - {issueData.summary}</h4>
          
          <div style={{ marginBottom: '16px' }}>
            <strong>Status:</strong> {issueData.status} | 
            <strong> Type:</strong> {issueData.type} |
            <strong> Priority:</strong> {issueData.priority}
          </div>

          {issueData.aiAnalysis && (
            <div style={{ 
              border: '1px solid #ddd', 
              borderRadius: '4px', 
              padding: '12px',
              backgroundColor: '#f9f9f9' 
            }}>
              <h5>AI-Generated Release Notes Content</h5>
              
              <div style={{ marginBottom: '8px' }}>
                <strong>Category:</strong> {issueData.aiAnalysis.category}
              </div>
              
              <div style={{ marginBottom: '8px' }}>
                <strong>Symptom:</strong> {issueData.aiAnalysis.symptom}
              </div>
              
              <div style={{ marginBottom: '8px' }}>
                <strong>Condition:</strong> {issueData.aiAnalysis.condition}
              </div>
              
              <div style={{ 
                padding: '8px', 
                backgroundColor: issueData.aiAnalysis.symptom !== issueData.aiAnalysis.condition ? '#d4edda' : '#f8d7da',
                borderRadius: '4px',
                marginTop: '8px'
              }}>
                Quality Check: Symptom ≠ Condition {issueData.aiAnalysis.symptom !== issueData.aiAnalysis.condition ? '✓' : '✗'}
              </div>
            </div>
          )}

          <div style={{ marginTop: '16px' }}>
            <button 
              onClick={() => processCurrentIssue(issueData.key)}
              disabled={processing}
              style={{ marginRight: '8px' }}
            >
              {processing ? 'Processing...' : 'Reprocess Issue'}
            </button>
            
            <button 
              onClick={runBatchProcess}
              disabled={processing}
            >
              Run Batch Process
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
```

### **manifest.yml** - Plugin Configuration

```yaml
modules:
  jira:issuePanel:
    - key: jira-doc-intelligence-panel
      function: main
      title: Documentation Intelligence
      icon: https://developer.atlassian.com/platform/forge/images/icons/issue-panel-icon.svg
  function:
    - key: main
      handler: index.handler

app:
  id: ari:cloud:ecosystem::app/your-app-id

permissions:
  scopes:
    - read:jira-work
    - write:jira-work
  external:
    fetch:
      backend:
        - https://api.openai.com

environments:
  development:
    variables:
      OPENAI_API_KEY: your-openai-api-key
  production:
    variables:
      OPENAI_API_KEY: your-production-openai-api-key
```

## Step 3: Deploy and Test

### **Deploy to Development**

```bash
# Deploy to development environment
forge deploy

# Install on your Jira site
forge install

# View logs
forge logs
```

### **Test Your Plugin**

1. Go to any Jira issue
2. Look for "Documentation Intelligence" panel on the right side
3. See AI-generated content for the issue
4. Test batch processing functionality

## Step 4: Integration with Your Python Logic

### **Option A: Keep Python Logic in Forge**

Translate your Python functions to JavaScript (as shown above)

### **Option B: Call Python API from Forge**

```javascript
// In your Forge resolver
async function callPythonAPI(issueData) {
  const response = await fetch('https://your-python-api.herokuapp.com/process', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(issueData)
  });
  
  return await response.json();
}
```

### **Option C: Hybrid Approach**

- Keep simple processing in Forge (fast)
- Call Python API for complex AI processing (when needed)

## Step 5: Next Development Steps

### **Phase 1: Basic Plugin (Week 1)**

- ✅ Issue panel showing AI-generated content
- ✅ Single issue processing
- ✅ Basic UI with quality checks

### **Phase 2: Enhanced Features (Week 2)**

- Batch processing UI
- JQL query builder
- Export functionality (markdown, JSON)
- Settings panel for configuration

### **Phase 3: Advanced Integration (Week 3)**

- Webhook integration for real-time processing
- Confluence publishing
- Custom field creation
- Advanced AI prompting

## Quick Start Commands

```bash
# Start development
forge create jira-doc-intelligence
cd jira-doc-intelligence

# Copy the code above into appropriate files
# Set up your OpenAI API key in manifest.yml

# Deploy and test
forge deploy
forge install
forge logs --tail
```

## Expected User Experience

1. **Developer opens Jira issue**
2. **Sees "Documentation Intelligence" panel**
3. **Views AI-generated symptom, condition, category**
4. **Can reprocess or run batch operations**
5. **Gets immediate feedback on content quality**

This Forge plugin gives you a direct integration with Jira that leverages your existing Python logic while providing a native Jira user experience. Once you validate this approach, you can expand to more sophisticated features or migrate to Atlassian Connect for more flexibility.