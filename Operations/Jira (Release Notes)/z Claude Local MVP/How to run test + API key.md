API token: ATATT3xFfGF0cMmF-rkxcZoIlh_4QQ1b2ujDkpggicD2QsBue8aAkYH6RCNsoK4yQF1M2qn1uOQWm-JmthAwV-SWTVME8XPv7wFr5u68KOf2JnoDNjmp3GYieTs5iWe66kyTA2qE5K3XTquPbQx2mSYloATL3pTsWMykMNjtpLgneL6mlo-JhWQ=4F68DBDE
# Jira Pricing Options for Single User Testing


## **Recommended Setup for Your Testing**

### **Step 1: Create Free Jira Cloud Instance**

```bash
# Go to Atlassian and create account
https://www.atlassian.com/software/jira/free

# Choose "Jira Software" 
# Select "Cloud" option
# Create your site: https://your-site-name.atlassian.net
```

### **Step 2: Configure for Your Testing Needs**

```yaml
Projects to Create:
  1. "XCP" - Test project mimicking your real environment
  2. "NVO" - Second test project  
  3. "WS" - Third test project
  4. "TEST-DOC" - Dedicated project for plugin testing

Issue Types Needed:
  - Bug/Defect (for CWC/CWOC testing)
  - Epic (for platform content testing)
  - Story (for enhancement testing)
```

### **Step 3: Add Required Custom Fields**

Since you're on free tier, you get custom fields:

```yaml
Custom Fields to Add:
  1. "Documentation Required" (Select List: Yes/No/Auto-Detect)
  2. "Disclosure Status" (Select List: Internal Only/Approved for Publication/Under Review)  
  3. "Customer Impact" (Select List: None/Low/Medium/High/Critical)
  4. "Documentation Notes" (Paragraph Text)
```

### **Step 4: Create Test Data**

```javascript
// Sample issues to create for testing
const testIssues = [
  {
    project: "XCP",
    type: "Bug", 
    summary: "Random contracts listed in Contracts table",
    description: "After unlinking portal account, random contracts appear in the table",
    priority: "High",
    status: "Open"
  },
  {
    project: "XCP",
    type: "Bug",
    summary: "Incorrect operation status displayed", 
    description: "When events from XIQ come out of order, status shows incorrectly",
    priority: "Medium",
    status: "Closed",
    resolution: "Fixed"
  },
  {
    project: "NVO", 
    type: "Epic",
    summary: "Introduction to Extreme Platform ONE",
    description: "Epic for platform introduction content in release notes"
  }
];
```

## **API Access Setup (Free Tier)**

### **Generate API Token**

1. Go to: https://id.atlassian.com/manage-profile/security/api-tokens
2. Create API token
3. Save securely for your `.env` file

### **Test API Access**

```bash
# Test with curl (replace with your details)
curl -X GET \
  'https://your-site.atlassian.net/rest/api/3/search?jql=project=XCP' \
  -H 'Accept: application/json' \
  -u 'your-email@domain.com:your-api-token'
```

## **Limitations of Free Tier (and Workarounds)**

### **Storage Limit: 2GB**

- **Impact**: Minimal for testing
- **Workaround**: Clean up test data regularly

### **User Limit: 10 users**

- **Impact**: None for single-user testing
- **Benefit**: Can invite collaborators if needed

### **No Advanced Features**

- **Missing**: Advanced roadmaps, insights
- **Impact**: None for your plugin development
- **Core features available**: API, custom fields, automation, webhooks

## **Best Option: Jira Cloud Free Tier**

✅ **Jira Cloud Standard - FREE for up to 10 users**

- **Cost**: $0/month for up to 10 users
- **Storage**: 2GB
- **Features**: Full Jira functionality including:
    - Custom fields (what you need for your testing)
    - REST API access (critical for your plugin)
    - Webhooks and automation
    - JQL queries
    - All issue types (Bug, Epic, Story, etc.)
- **Perfect for**: Development and testing your plugin

**Sign up**: https://www.atlassian.com/software/jira/free



## **Migration Path**

```yaml
Development Phases:
  Phase 1: Free Jira Cloud (your testing)
    - Develop and test plugin locally
    - Validate AI processing logic
    - Perfect JQL queries and field setup
    
  Phase 2: Company Jira Integration
    - Apply learnings to production Jira
    - Deploy plugin to company environment
    - Scale with enterprise features
```

## **Quick Start Commands**

```bash
# Update your .env with free Jira instance
JIRA_BASE_URL=https://your-test-site.atlassian.net
JIRA_USERNAME=your-email@domain.com  
JIRA_API_TOKEN=your_generated_token

# Test connection
npm run dev
# Visit: http://localhost:3000/api/test/test-connection
```

## **Total Cost for Development**

```yaml
Jira Cloud Free: $0/month
OpenAI API (GPT-4o mini): ~$1-5/month (for testing)
AWS Free Tier: $0/month (first year)
Total Development Cost: ~$1-5/month
```

**Recommendation**: Start with Jira Cloud Free tier immediately. It provides everything you need for plugin development and testing, with easy migration path to your company's production Jira environment later.

The free tier is genuinely functional - not a limited trial - so you can develop and test your entire plugin architecture without any cost pressure.