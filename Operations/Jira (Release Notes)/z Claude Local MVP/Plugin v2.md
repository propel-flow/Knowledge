
# Making Your Code into a Jira Plugin

You're absolutely right - what you ran is a **standalone script**, not a Jira plugin. Let me show you how to turn it into an actual plugin that users can trigger from within Jira.

## **Current State vs Plugin State**

### **What You Have Now:**

```yaml
Current: Standalone Python script
Trigger: Manual execution (python main.py)
Access: Local computer only
Users: Just you
Integration: External API calls to Jira
```

### **What You Need for a Plugin:**

```yaml
Target: Jira-integrated plugin
Trigger: From within Jira UI (buttons, panels, menus)
Access: All Jira users
Users: Anyone with permissions
Integration: Native Jira integration
```

## **Option 1: Atlassian Forge Plugin (Recommended)**

### **Convert Your Python Logic to Forge (JavaScript)**

#### **manifest.yml**

```yaml
modules:
  jira:issuePanel:
    - key: doc-intelligence-panel
      function: main
      title: Documentation Intelligence
      icon: https://developer.atlassian.com/platform/forge/images/icons/issue-panel-icon.svg
  
  jira:globalPage:
    - key: bulk-processor
      function: bulk-processor
      title: Bulk Documentation Processor
      
  function:
    - key: main
      handler: index.handler
    - key: bulk-processor  
      handler: bulk.handler

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
      OPENAI_API_KEY: your-key-here
```

#### **src/index.js** (Issue Panel - Single Issue Processing)

```javascript
import Resolver from '@forge/resolver';
import api, { route } from '@forge/api';

const resolver = new Resolver();

// Your Python logic converted to JavaScript
resolver.define('processCurrentIssue', async (req) => {
  const { issueKey } = req.payload;
  
  try {
    // Get issue data (replaces your jira.issue() call)
    const issueResponse = await api.asApp().requestJira(
      route`/rest/api/3/issue/${issueKey}`,
      {
        headers: { 'Accept': 'application/json' }
      }
    );
    
    const issue = await issueResponse.json();
    
    // Your process_issue_with_ai logic converted
    const processedData = await processIssueWithAI(issue);
    
    return {
      success: true,
      data: processedData
    };
    
  } catch (error) {
    console.error('Processing error:', error);
    return { success: false, error: error.message };
  }
});

// Convert your Python AI functions to JavaScript
async function processIssueWithAI(issue) {
  const basicInfo = {
    key: issue.key,
    summary: issue.fields.summary,
    status: issue.fields.status.name,
    type: issue.fields.issuetype.name,
    priority: issue.fields.priority?.name || 'Unknown',
    description: issue.fields.description || 'No description'
  };

  // Call OpenAI (your extract_symptom_with_ai logic)
  const aiAnalysis = await generateAIContent(basicInfo);
  
  return {
    ...basicInfo,
    aiAnalysis
  };
}

async function generateAIContent(issueData) {
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
        content: `
Extract documentation content from this Jira issue:

Summary: ${issueData.summary}
Description: ${issueData.description}

Return JSON with:
{
  "symptom": "what user observes",
  "condition": "when it happens", 
  "category": "defect-cwc|defect-cwoc|enhancement|etc",
  "confidence": 0.85
}
`
      }],
      max_tokens: 400,
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
      category: "unknown",
      confidence: 0.1
    };
  }
}

export const handler = resolver.getDefinitions();
```

#### **src/frontend/index.jsx** (UI Panel Users See)

```jsx
import React, { useState, useEffect } from 'react';
import { invoke } from '@forge/bridge';
import { Button, LoadingButton, Badge, SectionMessage } from '@atlaskit/components';

function DocumentationPanel() {
  const [issueData, setIssueData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [processing, setProcessing] = useState(false);

  useEffect(() => {
    // Get current issue context from Jira
    invoke('view.getContext').then(context => {
      const issueKey = context.extension.issue.key;
      processIssue(issueKey);
    });
  }, []);

  const processIssue = async (issueKey) => {
    setProcessing(true);
    try {
      const result = await invoke('processCurrentIssue', { issueKey });
      if (result.success) {
        setIssueData(result.data);
      }
    } catch (error) {
      console.error('Processing failed:', error);
    } finally {
      setProcessing(false);
      setLoading(false);
    }
  };

  const regenerateContent = async () => {
    if (issueData) {
      await processIssue(issueData.key);
    }
  };

  if (loading) {
    return <div style={{ padding: '16px' }}>Loading documentation analysis...</div>;
  }

  return (
    <div style={{ padding: '16px' }}>
      <h3>📝 Documentation Intelligence</h3>
      
      {issueData && (
        <div>
          <div style={{ marginBottom: '16px' }}>
            <Badge appearance="primary">{issueData.type}</Badge>
            <Badge appearance={issueData.priority === 'High' ? 'important' : 'default'}>
              {issueData.priority}
            </Badge>
            <Badge>{issueData.status}</Badge>
          </div>

          {issueData.aiAnalysis && (
            <div style={{ 
              border: '1px solid #ddd', 
              borderRadius: '8px', 
              padding: '16px',
              backgroundColor: '#f9f9f9',
              marginBottom: '16px'
            }}>
              <h4>🤖 AI-Generated Release Notes Content</h4>
              
              <div style={{ marginBottom: '12px' }}>
                <strong>Category:</strong> 
                <Badge appearance="outline">{issueData.aiAnalysis.category}</Badge>
                <span style={{ marginLeft: '8px' }}>
                  <strong>Confidence:</strong> {(issueData.aiAnalysis.confidence * 100).toFixed(0)}%
                </span>
              </div>
              
              <div style={{ marginBottom: '12px' }}>
                <strong>Symptom:</strong>
                <p style={{ marginLeft: '16px', fontStyle: 'italic' }}>
                  {issueData.aiAnalysis.symptom}
                </p>
              </div>
              
              <div style={{ marginBottom: '12px' }}>
                <strong>Condition:</strong>
                <p style={{ marginLeft: '16px', fontStyle: 'italic' }}>
                  {issueData.aiAnalysis.condition}
                </p>
              </div>

              {/* Quality Check */}
              <SectionMessage 
                appearance={
                  issueData.aiAnalysis.symptom !== issueData.aiAnalysis.condition 
                    ? "confirmation" 
                    : "warning"
                }
              >
                <p>
                  <strong>Quality Check:</strong> Symptom ≠ Condition{' '}
                  {issueData.aiAnalysis.symptom !== issueData.aiAnalysis.condition ? '✅' : '⚠️'}
                </p>
              </SectionMessage>
            </div>
          )}

          <div style={{ display: 'flex', gap: '8px' }}>
            <LoadingButton 
              isLoading={processing}
              onClick={regenerateContent}
            >
              🔄 Regenerate Content
            </LoadingButton>
            
            <Button 
              appearance="primary"
              onClick={() => {
                // Copy content to clipboard or open in modal
                navigator.clipboard.writeText(
                  `Symptom: ${issueData.aiAnalysis.symptom}\n\nCondition: ${issueData.aiAnalysis.condition}`
                );
              }}
            >
              📋 Copy to Clipboard
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

export default DocumentationPanel;
```

#### **src/bulk.js** (Bulk Processing Page)

```javascript
import Resolver from '@forge/resolver';
import api, { route } from '@forge/api';

const resolver = new Resolver();

// Your Python batch processing logic
resolver.define('processBatchIssues', async (req) => {
  const { jql, maxResults = 20 } = req.payload;
  
  try {
    // Your jira.search_issues() equivalent
    const searchResponse = await api.asApp().requestJira(
      route`/rest/api/3/search`,
      {
        headers: { 'Accept': 'application/json' },
        params: { jql, maxResults, fields: 'summary,description,status,priority,issuetype' }
      }
    );
    
    const searchResults = await searchResponse.json();
    
    // Process each issue (your main loop logic)
    const processedIssues = [];
    for (const issue of searchResults.issues) {
      const processed = await processIssueWithAI(issue);
      processedIssues.push(processed);
    }
    
    return {
      success: true,
      totalFound: searchResults.total,
      processed: processedIssues.length,
      issues: processedIssues
    };
    
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// Define your JQL queries (from your Python queries dict)
resolver.define('getPresetQueries', async () => {
  return {
    defects_cwc: 'issuetype in (Bug, Defect) AND status in (Closed, Resolved) AND resolution in (Fixed, Done) ORDER BY priority DESC',
    defects_cwoc: 'issuetype in (Bug, Defect) AND status = Closed AND resolution in ("Won\'t Fix", Duplicate) ORDER BY key ASC',
    open_defects: 'issuetype in (Bug, Defect) AND status not in (Closed, Resolved, Done) AND priority in (High, Highest) ORDER BY priority DESC',
    platform_epics: 'issuetype = Epic AND (summary ~ "Introduction.*" OR summary ~ "Prerequisites.*")'
  };
});

export const handler = resolver.getDefinitions();
```

## **How Users Would Trigger Your Plugin**

### **Trigger 1: Issue Panel (Single Issue)**

```yaml
Where: Right side panel of any Jira issue
When: User opens any issue
What: Shows AI-generated documentation content
Actions: 
  - Regenerate content
  - Copy to clipboard
  - Export as markdown
```

### **Trigger 2: Global Page (Bulk Processing)**

```yaml
Where: Jira Apps menu → "Documentation Processor"
When: User wants to process multiple issues
What: Shows JQL query builder and batch results
Actions:
  - Select preset queries (your Python queries)
  - Custom JQL input
  - Bulk process and download results
```

### **Trigger 3: Issue Actions (Context Menu)**

```yaml
Where: Issue "..." menu → "Generate Documentation"
When: User right-clicks issue or uses actions menu
What: Processes single issue and shows results
Actions:
  - Process current issue
  - Add to batch queue
  - Generate release notes
```

## **Deploy Your Plugin**

```bash
# Install Forge CLI
npm install -g @forge/cli

# Create your app
forge create doc-intelligence-plugin
cd doc-intelligence-plugin

# Copy the code above into respective files

# Deploy to development
forge deploy

# Install on your Jira site
forge install

# View in Jira
# 1. Go to any issue → see panel on right
# 2. Go to Apps menu → see bulk processor
```

## **User Experience Flow**

### **Single Issue Processing:**

1. **User opens Jira issue**
2. **Sees "Documentation Intelligence" panel** on right side
3. **Clicks "Generate Content"** button
4. **Views AI-generated symptom, condition, category**
5. **Can regenerate or copy content**

### **Bulk Processing:**

1. **User goes to Apps → Documentation Processor**
2. **Selects preset query** (your defects_cwc, etc.)
3. **Clicks "Process Issues"**
4. **Views results table with all processed issues**
5. **Downloads as CSV/JSON** (like your Python output)

## **Next Steps**

### **Phase 1: Basic Plugin (This Week)**

- Convert your Python logic to Forge JavaScript
- Deploy issue panel for single-issue processing
- Test with your existing Jira data

### **Phase 2: Enhanced Features (Next Week)**

- Add bulk processing page
- Implement your JQL preset queries
- Add export functionality (CSV, JSON, Markdown)

### **Phase 3: Advanced Integration (Following Week)**

- Add webhook processing (real-time)
- Confluence publishing integration
- Custom field updates

Your Python script is perfect as the logic foundation - now we just need to wrap it in Jira's plugin framework so users can access it natively!