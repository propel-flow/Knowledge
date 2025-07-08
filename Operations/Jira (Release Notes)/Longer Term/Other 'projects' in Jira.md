
# Jira Configuration Differences by Project Type

You're absolutely right - different project types have vastly different Jira configurations. Here's how they typically differ and how it impacts your documentation plugin:

## **Common Atlassian Project Templates**

### **1. Software Development (Your Current Focus)**

```yaml
Issue Types: Epic, Story, Task, Bug, Subtask
Workflows: To Do → In Progress → Code Review → Testing → Done
Custom Fields: Story Points, Sprint, Fix Version, Components
Documentation Focus: Release notes, API docs, technical specifications
```

### **2. Marketing Campaign Management**

```yaml
Issue Types: Campaign, Creative Asset, Blog Post, Social Media Post, Email
Workflows: Ideation → Planning → Creation → Review → Approval → Published
Custom Fields: Target Audience, Channel, Budget, Launch Date, Campaign Type
Documentation Focus: Campaign briefs, performance reports, content calendars
```

### **3. Product Management**

```yaml
Issue Types: Initiative, Feature, User Story, Market Research, Competitive Analysis
Workflows: Backlog → Prioritized → In Development → Testing → Released
Custom Fields: Business Value, Customer Segment, Revenue Impact, OKR Alignment
Documentation Focus: PRDs, roadmaps, feature specifications, market analysis
```

### **4. IT Service Management (ITSM)**

```yaml
Issue Types: Incident, Service Request, Problem, Change Request, Knowledge Article
Workflows: Open → Assigned → In Progress → Resolved → Closed
Custom Fields: SLA, Priority Matrix, Affected Services, Resolution Category
Documentation Focus: Runbooks, incident reports, change documentation, KB articles
```

### **5. HR/People Operations**

```yaml
Issue Types: Hiring Request, Onboarding Task, Performance Review, Policy Update
Workflows: Requested → Approved → In Progress → Completed → Archived
Custom Fields: Department, Role Level, Hiring Manager, Start Date, Budget Code
Documentation Focus: Job descriptions, policy documents, process guides, org charts
```

### **6. Legal/Compliance**

```yaml
Issue Types: Contract Review, Legal Request, Compliance Check, Risk Assessment
Workflows: Submitted → Under Review → Legal Review → Approved → Implemented
Custom Fields: Risk Level, Compliance Framework, Stakeholder, Due Date, Cost Center
Documentation Focus: Legal briefs, compliance reports, contract summaries, risk assessments
```

### **7. Finance/Procurement**

```yaml
Issue Types: Purchase Request, Invoice Processing, Budget Planning, Vendor Evaluation
Workflows: Requested → Budget Check → Approval → Procurement → Received → Paid
Custom Fields: Cost Center, Vendor, Amount, Approval Level, GL Account
Documentation Focus: Financial reports, vendor evaluations, budget summaries, audit trails
```

### **8. Content/Creative**

```yaml
Issue Types: Article, Video, Design Asset, Review, Publication
Workflows: Concept → Draft → Review → Revisions → Approval → Published
Custom Fields: Content Type, Target Audience, Publication Date, Brand Guidelines
Documentation Focus: Content briefs, brand guidelines, publication schedules, performance metrics
```

### **9. Operations/Facilities**

```yaml
Issue Types: Maintenance Request, Equipment Purchase, Space Planning, Vendor Management
Workflows: Requested → Assessed → Scheduled → In Progress → Completed → Verified
Custom Fields: Location, Equipment Type, Priority Level, Vendor, Cost
Documentation Focus: Maintenance logs, equipment manuals, vendor contracts, operational procedures
```

### **10. Sales/Customer Success**

```yaml
Issue Types: Lead, Opportunity, Customer Issue, Renewal, Upsell
Workflows: Qualified → Proposal → Negotiation → Closed Won/Lost
Custom Fields: Deal Size, Sales Stage, Account Owner, Close Date, Customer Segment
Documentation Focus: Sales playbooks, customer communications, deal summaries, renewal reports
```

## **How This Impacts Your Documentation Plugin**

### **1. Field Mapping Strategy**

```python
# Enhanced field mapping for different project types
FIELD_MAPPINGS = {
    "software": {
        "title_field": "summary",
        "description_field": "description", 
        "status_field": "status",
        "priority_field": "priority",
        "category_logic": "issuetype + resolution",
        "customer_impact": "priority + labels",
        "documentation_types": ["release_notes", "api_docs", "bug_reports"]
    },
    
    "marketing": {
        "title_field": "summary",
        "description_field": "description",
        "status_field": "status", 
        "priority_field": "campaign_priority",  # Custom field
        "category_logic": "campaign_type + channel",
        "customer_impact": "target_audience + reach",
        "documentation_types": ["campaign_briefs", "performance_reports", "content_guides"]
    },
    
    "product": {
        "title_field": "summary",
        "description_field": "description",
        "status_field": "status",
        "priority_field": "business_value",  # Custom field
        "category_logic": "feature_type + customer_segment", 
        "customer_impact": "revenue_impact + user_segment",
        "documentation_types": ["prds", "roadmaps", "feature_specs"]
    },
    
    "itsm": {
        "title_field": "summary", 
        "description_field": "description",
        "status_field": "status",
        "priority_field": "incident_priority",  # Custom field
        "category_logic": "incident_type + affected_service",
        "customer_impact": "sla_breach + user_count",
        "documentation_types": ["incident_reports", "runbooks", "kb_articles"]
    }
}
```

### **2. AI Prompt Adaptation by Project Type**

```python
def get_ai_prompts_by_project_type(project_type):
    prompts = {
        "software": {
            "symptom": "Extract what the user observes when this bug occurs",
            "condition": "Explain the technical conditions that trigger this issue",
            "impact": "Describe the impact on system functionality"
        },
        
        "marketing": {
            "symptom": "Describe the marketing challenge or opportunity", 
            "condition": "Explain the market conditions or campaign context",
            "impact": "Describe the business impact on brand/revenue/engagement"
        },
        
        "product": {
            "symptom": "Describe the user problem or market need",
            "condition": "Explain the conditions where this need is most critical", 
            "impact": "Describe the business value and user benefit"
        },
        
        "itsm": {
            "symptom": "Describe what users experience during this incident",
            "condition": "Explain the system conditions that cause this issue",
            "impact": "Describe the service impact and affected users"
        }
    }
    
    return prompts.get(project_type, prompts["software"])
```

### **3. Documentation Output Templates**

```python
OUTPUT_TEMPLATES = {
    "software": {
        "release_notes": """
        ## {issue_key} - {summary}
        **Type**: {issue_type}
        **Priority**: {priority}
        
        **Symptom**: {ai_symptom}
        **Condition**: {ai_condition}
        **Resolution**: {resolution}
        """,
        
        "bug_report": """
        # Bug Report: {issue_key}
        ## Problem Description
        {ai_symptom}
        
        ## Reproduction Steps
        {ai_condition}
        
        ## Technical Details
        {description}
        """
    },
    
    "marketing": {
        "campaign_brief": """
        # Campaign Brief: {issue_key}
        ## Campaign Overview
        {ai_symptom}
        
        ## Target Audience & Context
        {ai_condition}
        
        ## Expected Outcomes
        {ai_impact}
        """,
        
        "performance_report": """
        # Campaign Performance: {issue_key}
        ## Campaign Results
        {ai_symptom}
        
        ## Market Response
        {ai_condition}
        
        ## Business Impact
        {ai_impact}
        """
    },
    
    "product": {
        "prd": """
        # Product Requirements: {issue_key}
        ## Problem Statement
        {ai_symptom}
        
        ## Market Context
        {ai_condition}
        
        ## Business Value
        {ai_impact}
        
        ## Technical Requirements
        {description}
        """
    }
}
```

### **4. Project Type Detection Logic**

```python
def detect_project_type(project_key, issue_types, custom_fields):
    """Auto-detect project type based on Jira configuration"""
    
    # Check issue types
    if any(t in issue_types for t in ['Bug', 'Story', 'Epic', 'Task']):
        if any(f in custom_fields for f in ['Story Points', 'Sprint', 'Fix Version']):
            return 'software'
    
    if any(t in issue_types for t in ['Campaign', 'Creative Asset', 'Blog Post']):
        return 'marketing'
        
    if any(t in issue_types for t in ['Initiative', 'Feature', 'Market Research']):
        return 'product'
        
    if any(t in issue_types for t in ['Incident', 'Service Request', 'Problem']):
        return 'itsm'
        
    if any(t in issue_types for t in ['Hiring Request', 'Onboarding', 'Performance Review']):
        return 'hr'
        
    # Default fallback
    return 'generic'
```

### **5. Enhanced Plugin Configuration**

```javascript
// Forge plugin with project type awareness
const projectTypeConfig = {
  software: {
    panelTitle: "Release Notes Intelligence",
    primaryActions: ["Generate Release Notes", "Process Defects", "API Documentation"],
    aiPromptStyle: "technical"
  },
  
  marketing: {
    panelTitle: "Campaign Intelligence", 
    primaryActions: ["Generate Brief", "Performance Analysis", "Content Planning"],
    aiPromptStyle: "creative"
  },
  
  product: {
    panelTitle: "Product Intelligence",
    primaryActions: ["Generate PRD", "Market Analysis", "Feature Planning"], 
    aiPromptStyle: "strategic"
  },
  
  itsm: {
    panelTitle: "Service Intelligence",
    primaryActions: ["Incident Analysis", "Generate Runbook", "KB Article"],
    aiPromptStyle: "operational"
  }
};

// Auto-configure based on detected project type
resolver.define('getProjectConfig', async (req) => {
  const projectType = await detectProjectType(req.context.projectKey);
  return projectTypeConfig[projectType] || projectTypeConfig.software;
});
```

## **Deployment Strategy for Multiple Project Types**

### **Phase 1: Start with Software Projects**

- Perfect your current approach
- Validate AI processing quality
- Build core plugin infrastructure

### **Phase 2: Expand to High-Value Adjacent Types**

- **Product Management**: Similar to software but different outputs (PRDs vs release notes)
- **ITSM**: Similar issue tracking but different documentation needs

### **Phase 3: Customize for Creative/Marketing**

- Different AI prompting styles
- Visual content considerations
- Campaign-specific workflows

### **Phase 4: Enterprise-Wide Rollout**

- Support all project types
- Advanced configuration options
- Admin controls for different teams

## **Universal Plugin Architecture**

```python
class UniversalDocumentationPlugin:
    def __init__(self):
        self.project_configs = FIELD_MAPPINGS
        self.ai_prompts = get_ai_prompts_by_project_type
        self.output_templates = OUTPUT_TEMPLATES
    
    def process_issue(self, issue, project_type=None):
        # Auto-detect if not provided
        if not project_type:
            project_type = self.detect_project_type(issue)
        
        # Use project-specific configuration
        config = self.project_configs[project_type]
        prompts = self.ai_prompts(project_type)
        
        # Process with appropriate logic
        return self.generate_documentation(issue, config, prompts)
```

This approach makes your plugin valuable across the entire organization, not just engineering teams. Each project type gets tailored AI processing and documentation output that matches their specific needs and workflows.