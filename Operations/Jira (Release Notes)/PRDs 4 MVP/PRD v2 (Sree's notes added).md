Release note specific (strict logic)
# Updated PRD: Jira Integration Requirements for Automated Release Notes

## Jira Standardization Requirements

### Critical Jira Fields to Implement

Based on the release notes automation requirements, the following fields must be standardized across all projects:

#### **1. Core Release Notes Fields (All Issue Types)**

```yaml
Required Fields:
  - "Release Notes Required": Yes/No (Select List)
  - "Release Notes Description": Long Text (Rich Text Editor)
  - "Disclosure Status": Select List
    Options: ["Approved for Publication", "Internal Only", "Under Review"]
  - "Exclude From Document": Yes/No (Select List)
  - "Target Version": Version Picker
  - "Release Notes Category": Select List
    Options: ["Defects CWC", "Defects CWOC", "Open Defects", "Known Issues", "Features", "Prerequisites", "Introduction"]
```

#### **2. Defect-Specific Fields**

```yaml
Defect Fields:
  - "Symptom": Long Text
    Description: "Brief summary of the defect"
    Validation: Required if Release Notes Required = Yes
    
  - "Condition": Long Text  
    Description: "Detailed explanation of when the defect occurs"
    Validation: Must be different from Symptom field
    
  - "Workaround": Long Text
    Description: "Steps to resolve or work around the issue"
    Validation: Required for "Defects CWC" category
    
  - "Resolution Type": Select List
    Options: ["Resolved With Code", "Resolved Without Code", "Won't Fix", "Duplicate"]
```

#### **3. Epic-Specific Fields for Platform Content**

```yaml
Epic Fields:
  - "Epic Category": Select List
    Options: ["Introduction", "Supported Applications", "Prerequisites", 
             "Features Supported", "Features Not Supported", "Known Issues"]
             
  - "Feature Table Data": Structured Text
    Description: "Tabular data for features (JSON format)"
    Example: '[{"feature": "Backup & Restore", "description": "Manual backup..."}]'
    
  - "Supported Devices": Multi-line Text
    Description: "List of supported devices and OS versions"
```

## Jira Plugin Requirements

### **Microservice 7: Jira Field Validation Service**

**Purpose**: Real-time field validation and AI-assisted content completion

**Technical Specifications**:

```yaml
Runtime: AWS Lambda (Node.js)
Integration: Jira Webhook Events + Browser Extension
AI Provider: GPT-4o Mini (cost-effective for validation)
Storage: S3 for validation rules and templates
```

**Key Features**:

- Real-time field validation via webhooks
- AI-powered content suggestions
- Browser extension for form guidance
- Template auto-population based on issue type

### **Browser Extension Requirements**

#### **Real-Time Validation Features**

```javascript
// Example validation rules
const validationRules = {
  symptomConditionDifferent: {
    fields: ['symptom', 'condition'],
    rule: 'must_be_different',
    message: 'Symptom and Condition cannot be identical'
  },
  
  workaroundRequired: {
    fields: ['workaround'],
    condition: 'resolution_type === "Resolved With Code"',
    rule: 'required',
    message: 'Workaround is required for defects resolved with code changes'
  },
  
  releaseNotesDescription: {
    fields: ['release_notes_description'],
    condition: 'release_notes_required === "Yes"',
    rule: 'required_and_meaningful',
    message: 'Release Notes Description required and must be descriptive'
  }
}
```

#### **AI-Assisted Content Generation**

```yaml
AI Features:
  - Auto-generate Release Notes Description from Summary + Description
  - Suggest Symptom/Condition based on defect details
  - Validate technical accuracy of content
  - Check for completeness based on issue type
  - Suggest appropriate Release Notes Category
```

## JQL Query Standardization

### **Required JQL Templates by Category**

Based on the existing XCO queries, standardize across all projects:

#### **1. Defects Closed with Code Changes (CWC)**

```sql
"Target Version" = "{VERSION}" 
AND issuetype in (Defect, ESR) 
AND "Disclosure Status" = "Approved for Publication" 
AND status in (Closed, Resolved, Testing) 
AND resolution = "Resolved With Code" 
AND "Release Notes Required" = "Yes"
AND ("Exclude From Document" not in (Yes) OR "Exclude From Document" is EMPTY) 
ORDER BY key ASC
```

#### **2. Defects Closed without Code Changes (CWOC)**

```sql
"Target Version" = "{VERSION}" 
AND issuetype in (Defect, ESR) 
AND "Disclosure Status" = "Approved for Publication" 
AND status = Closed 
AND resolution = "Resolved Without Code" 
AND "Release Notes Required" = "Yes"
AND ("Exclude From Document" not in (Yes) OR "Exclude From Document" is EMPTY) 
ORDER BY key ASC
```

#### **3. Open Defects**

```sql
project in ({PROJECT_LIST}) 
AND issuetype in (Defect, ESR) 
AND status not in (Closed, Resolved, Done, Testing, Returned) 
AND "Disclosure Status" = "Approved for Publication" 
AND "Release Notes Required" = "Yes"
AND ("Exclude From Document" not in (Yes) OR "Exclude From Document" is EMPTY) 
ORDER BY key ASC
```

#### **4. Epic Content (Introduction, Features, etc.)**

```sql
"Target Version" = "{VERSION}" 
AND issuetype = Epic 
AND "Epic Category" in ({CATEGORY_LIST})
AND "Disclosure Status" = "Approved for Publication" 
AND ("Exclude From Document" not in (Yes) OR "Exclude From Document" is EMPTY) 
ORDER BY "Epic Category", key ASC
```

## User Training & Guidance System

### **Microservice 8: User Guidance Service**

**Purpose**: Contextual help and training for Jira field completion

```yaml
Components:
  - Interactive field tooltips
  - Step-by-step wizards for complex issue types
  - Template library with examples
  - AI-powered content suggestions
  - Real-time validation feedback
```

### **Field Completion Guidelines**

#### **For Defects:**

```yaml
Step-by-Step Process:
  1. Issue Creation:
     - Select appropriate project (XCP, NVO, WS, Extreme AI Expert)
     - Choose "Defect" issue type
     
  2. Basic Information:
     - Summary: Clear, concise description
     - Target Version: Select from dropdown
     - Release Notes Required: Set to "Yes" if customer-facing
     
  3. Release Notes Content:
     - Symptom: "Brief summary of what users observe"
       Example: "Random contracts listed in Contracts table"
       
     - Condition: "Detailed explanation of when/how it occurs"  
       Example: "Random contracts appear after unlinking portal account"
       Validation: Must be different from Symptom
       
     - Workaround: "Steps to resolve (if applicable)"
       Required for: Code change resolutions
       
  4. Publication Control:
     - Disclosure Status: "Approved for Publication" (for external docs)
     - Exclude From Document: Leave empty unless specifically excluding
```

#### **For Epics (Platform Content):**

```yaml
Epic Creation Process:
  1. Epic Setup:
     - Epic Name: Match predefined categories
       Options: ["Introduction to Extreme Platform ONE", 
                "Supported Applications", "Prerequisites", etc.]
     - Epic Category: Auto-populate based on Epic Name
     
  2. Content Development:
     - Description: Comprehensive overview for the section
     - Feature Table Data: Use JSON format for structured data
       Example: '[{"feature": "SSO", "description": "Single sign-on capability"}]'
       
  3. Version Management:
     - Target Version: Must match release version
     - Release Notes Required: Always "Yes" for platform content
```

### **AI-Powered Field Assistance**

#### **Browser Extension Features:**

```yaml
Real-Time Assistance:
  - Field validation with immediate feedback
  - Content suggestions based on similar issues
  - Template auto-completion
  - Grammar and clarity checking
  - Technical terminology validation

Smart Suggestions:
  - Auto-generate Release Notes Description from Summary
  - Suggest Symptom/Condition based on issue details  
  - Recommend appropriate categories and labels
  - Flag incomplete or problematic entries

Quality Checks:
  - Ensure Symptom ≠ Condition
  - Verify required fields are complete
  - Check for appropriate technical detail level
  - Validate against company style guidelines
```

## Implementation Requirements

### **Phase 1: Jira Configuration (Week 1-2)**

```yaml
Tasks:
  - Create custom fields across all projects (XCP, NVO, WS, Extreme AI Expert)
  - Configure field schemes and screen layouts
  - Set up validation rules and required field logic
  - Create JQL templates for each project
  - Configure workflow transitions based on field values
```

### **Phase 2: Browser Extension Development (Week 3-4)**

```yaml
Technology Stack:
  - Frontend: Chrome Extension (Manifest V3)
  - Backend: AWS Lambda + API Gateway
  - AI Integration: GPT-4o Mini for real-time suggestions
  - Storage: S3 for templates and validation rules

Key Features:
  - Real-time field validation
  - AI content suggestions
  - Template library integration
  - Style guide enforcement
```

### **Phase 3: Training & Documentation (Week 5-6)**

```yaml
Deliverables:
  - Interactive training modules
  - Field completion guidelines
  - Video tutorials for each issue type
  - Quick reference cards
  - AI assistant integration documentation
```

## Success Metrics

### **Data Quality Metrics**

```yaml
Targets:
  - 95% of issues have complete required fields
  - 90% of Symptom/Condition pairs are sufficiently different
  - 85% of Release Notes descriptions meet quality standards
  - <5% issues require manual intervention during generation
```

### **User Adoption Metrics**

```yaml
Targets:
  - 80% of users enable browser extension within 30 days
  - 90% field completion rate with real-time assistance
  - 75% reduction in "back-and-forth" on field corrections
  - 60% improvement in first-draft release notes quality
```

This comprehensive approach ensures both the technical infrastructure and user experience support high-quality, automated release notes generation while maintaining the flexibility needed across different project types.