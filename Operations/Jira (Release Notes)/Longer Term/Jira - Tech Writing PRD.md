# AWS Product Requirements Document: Confluence-Jira Technical Documentation Platform

## Executive Summary

This PRD outlines a microservices-based technical documentation platform that integrates Confluence as the primary CMS with Jira for workflow management, AWS for content storage and versioning, and Claude AI capabilities via MCP integration. The solution addresses the technical writing team's current pain points while leveraging existing organizational infrastructure.

## Business Context

**Current State**: Technical writing team using disparate tools with limited integration, facing capacity constraints and workflow inefficiencies with Claude AI tooling.

**Target State**: Unified platform leveraging existing Jira/Confluence adoption with AI-enhanced documentation workflows, discrete AWS microservices for scalability, and seamless version control.

**Strategic Alignment**: Builds on existing business investment in Atlassian ecosystem while modernizing technical documentation workflows.

## Architecture Overview

### Core Components

1. **Jira Plugin**: Workflow orchestration and task management
2. **Confluence Integration**: Content authoring and presentation layer
3. **AWS Backend**: Microservices for content processing, storage, and AI integration
4. **MCP Layer**: Claude AI integration for content generation and analysis

## Microservice Specifications

### 1. Content Storage Service (AWS S3 + DynamoDB)

**Purpose**: Centralized content storage with versioning and metadata management

**Technical Specifications**:

- **Storage**: S3 buckets with versioning enabled
- **Metadata**: DynamoDB tables for content relationships, versions, and status
- **API**: REST endpoints for CRUD operations

**Key Features**:

- Atomic content versioning with rollback capability
- Content relationship mapping (parent/child documents)
- Metadata indexing for search and retrieval
- Integration with Confluence page hierarchy

**Testing Strategy**:

- Unit tests for version management logic
- Integration tests with Confluence API
- Load testing for concurrent access scenarios

**Recommended Starting Repository**:

- AWS Samples: `aws-samples/serverless-content-management`

### 2. AI Content Processing Service (AWS Lambda + Bedrock)

**Purpose**: Claude AI integration for content generation, analysis, and enhancement

**Technical Specifications**:

- **Runtime**: AWS Lambda (Node.js/Python)
- **AI Integration**: Amazon Bedrock with Claude model access
- **Queue**: SQS for async processing
- **Storage**: S3 for prompt templates and generated content

**Key Features**:

- Screenshot analysis and documentation generation
- Content gap analysis between versions
- Strategic document planning recommendations
- Translation services with glossary integration
- PRD generation from functional specifications

**MCP Integration Points**:

- Custom MCP server for Confluence content access
- Screenshot capture and analysis workflows
- Content comparison and enhancement suggestions

**Testing Strategy**:

- Mock AI responses for consistent testing
- A/B testing framework for prompt optimization
- Performance testing for large document processing

**Recommended Starting Repository**:

- AWS Samples: `aws-samples/amazon-bedrock-workshop`
- MCP: `modelcontextprotocol/servers`

### 3. Workflow Orchestration Service (AWS Step Functions)

**Purpose**: Manages complex documentation workflows and state transitions

**Technical Specifications**:

- **Engine**: AWS Step Functions for workflow orchestration
- **Integration**: Direct integration with Jira webhook events
- **Monitoring**: CloudWatch for workflow visibility
- **Error Handling**: DLQ and retry mechanisms

**Key Features**:

- Document review and approval workflows
- Content publishing pipelines
- AI-assisted content generation workflows
- Translation workflow management
- Content audit and analytics processing

**Testing Strategy**:

- Workflow simulation with mock data
- State transition validation
- Error scenario testing
- Performance benchmarking

**Recommended Starting Repository**:

- AWS Samples: `aws-samples/aws-stepfunctions-examples`

### 4. Analytics and Metrics Service (AWS Analytics Suite)

**Purpose**: Content performance tracking and usage analytics

**Technical Specifications**:

- **Data Lake**: S3 with Glue for ETL
- **Analytics**: Amazon Athena for querying
- **Visualization**: QuickSight dashboards
- **Real-time**: Kinesis for streaming analytics

**Key Features**:

- Content usage metrics and engagement tracking
- Document effectiveness scoring
- Translation quality metrics
- AI-generated content performance analysis
- Team productivity metrics

**Testing Strategy**:

- Data pipeline validation
- Analytics query performance testing
- Dashboard functionality testing
- Data accuracy verification

**Recommended Starting Repository**:

- AWS Samples: `aws-samples/amazon-athena-cross-account-catalog`

### 5. Translation and Localization Service (AWS Translate + Custom)

**Purpose**: Multi-language content management with domain-specific glossaries

**Technical Specifications**:

- **Translation**: AWS Translate with custom terminology
- **Storage**: S3 for glossaries and translation memories
- **Processing**: Lambda for post-processing and quality checks
- **Cache**: ElastiCache for frequently accessed translations

**Key Features**:

- Glossary-aware translation with product terminology
- Translation memory integration
- Quality scoring and human review workflows
- Batch and real-time translation modes

**Testing Strategy**:

- Translation accuracy validation
- Glossary integration testing
- Performance testing for large document sets
- Quality scoring algorithm validation

**Recommended Starting Repository**:

- AWS Samples: `aws-samples/amazon-translate-workshop`

### 6. Integration Gateway Service (AWS API Gateway)

**Purpose**: Unified API layer for all microservice interactions

**Technical Specifications**:

- **Gateway**: API Gateway with Lambda authorizers
- **Authentication**: Integration with Atlassian OAuth
- **Rate Limiting**: Built-in throttling and usage plans
- **Monitoring**: CloudWatch and X-Ray tracing

**Key Features**:

- Centralized authentication and authorization
- Request/response transformation
- API versioning and backward compatibility
- Rate limiting and quota management
- Audit logging for all API interactions

**Testing Strategy**:

- API contract testing
- Authentication/authorization validation
- Load testing and rate limiting verification
- Security penetration testing

**Recommended Starting Repository**:

- AWS Samples: `aws-samples/api-gateway-secure-pet-store`

## Jira Plugin Specifications

### Core Plugin Features

**Workflow Integration**:

- Custom Jira issue types for documentation requests
- Automated transitions based on content processing status
- Integration with approval workflows in Confluence
- AI-generated task breakdowns for complex documentation projects

**Dashboard Components**:

- Content pipeline status visualization
- Team productivity metrics
- AI processing queue status
- Translation project tracking

**Custom Fields**:

- Content complexity scoring
- AI confidence ratings
- Review assignment automation
- Publication readiness indicators

**Recommended Starting Repository**:

- Atlassian: `atlassian/atlassian-connect-express`
- Community: `atlassian-labs/jira-steps-plugin`

## MCP Integration Strategy

### Custom MCP Servers

**Confluence MCP Server**:

- Read/write access to Confluence spaces and pages
- Content hierarchy navigation
- Template and macro management
- Version history access

**Jira MCP Server**:

- Issue creation and management
- Workflow transition automation
- Custom field manipulation
- Project and sprint integration

**AWS Content MCP Server**:

- S3 content access and manipulation
- DynamoDB metadata queries
- Translation service integration
- Analytics data access

**Recommended Starting Repository**:

- Official: `modelcontextprotocol/servers/src/confluence`
- Community: `punkpeye/mcp-atlassian`

## Security and Compliance

### Data Protection

- Encryption at rest (S3, DynamoDB)
- Encryption in transit (TLS 1.3)
- IAM role-based access control
- VPC isolation for sensitive processing

### Audit and Compliance

- CloudTrail logging for all AWS actions
- Confluence audit log integration
- GDPR compliance for user data
- SOC 2 Type II alignment

### Access Control

- Atlassian OAuth integration
- Multi-factor authentication requirements
- Principle of least privilege
- Regular access reviews and rotation

## Implementation Phases

### Phase 1: Foundation (Weeks 1-4)

- Content Storage Service deployment
- Basic Confluence integration
- Jira plugin framework setup
- Core MCP server development

### Phase 2: AI Integration (Weeks 5-8)

- AI Content Processing Service
- Screenshot analysis capabilities
- Basic content generation workflows
- Translation service foundation

### Phase 3: Advanced Workflows (Weeks 9-12)

- Workflow Orchestration Service
- Advanced AI features (PRD generation, content strategy)
- Analytics and metrics implementation
- Performance optimization

### Phase 4: Production Readiness (Weeks 13-16)

- Security hardening
- Performance testing and optimization
- Documentation and training materials
- Rollout planning and execution

## Success Metrics

### Technical Metrics

- API response time < 200ms (95th percentile)
- Content processing throughput > 100 documents/hour
- AI accuracy rating > 85% for generated content
- System uptime > 99.9%

### Business Metrics

- 50% reduction in document creation time
- 75% reduction in strategic planning time
- 90% improvement in translation turnaround
- 40% increase in content reuse

### User Experience Metrics

- Time to first AI suggestion < 30 seconds
- User adoption > 80% within 6 months
- User satisfaction score > 4.0/5.0
- Support ticket reduction > 60%

## Risk Mitigation

### Technical Risks

- **AI Service Limits**: Implement request queuing and fallback mechanisms
- **Data Loss**: Multi-region backup and versioning strategies
- **Performance Degradation**: Auto-scaling and performance monitoring
- **Integration Failures**: Circuit breakers and graceful degradation

### Business Risks

- **User Adoption**: Comprehensive training and change management
- **Cost Overruns**: Usage monitoring and budget alerts
- **Compliance Issues**: Regular security audits and compliance reviews
- **Vendor Lock-in**: Multi-cloud strategy and portable architectures

This microservices architecture provides discrete, testable components while maintaining integration simplicity through the existing Atlassian ecosystem, positioning the organization for scalable, AI-enhanced technical documentation workflows.

Retry

K

DynamoDB vs PostGres?

Also for most of these tasks I know GPT4o mini works (with the right specific prompting and is a lot more cost effective (but not available through Bedrock)

Edit

## Database Selection: DynamoDB vs PostgreSQL

### **Recommendation: PostgreSQL (RDS)**

**Primary Reasons:**

### 1. **Relational Data Structure**

Technical documentation has inherently relational characteristics:

- **Document Hierarchies**: Parent-child relationships, cross-references, dependencies
- **User Permissions**: Complex role-based access with inheritance
- **Workflow States**: Multi-step approval processes with state transitions
- **Translation Relationships**: One-to-many language variants with shared metadata
- **Content Auditing**: Complex queries across versions, authors, and approval chains

### 2. **Query Complexity**

Your use cases require sophisticated querying:

- **Content Analytics**: "Show me all documents by team X, modified in last 30 days, with >50% AI-generated content"
- **Dependency Mapping**: "Find all documents that reference deprecated product Y"
- **Performance Reporting**: "Generate productivity metrics across teams, projects, and time periods"
- **Content Audit**: "Identify orphaned content with no recent usage"

### 3. **ACID Compliance**

Critical for documentation workflows:

- **Approval Workflows**: Ensure consistent state transitions
- **Version Management**: Atomic updates across related content
- **Content Publishing**: All-or-nothing deployments to prevent broken states

### 4. **Confluence Integration**

PostgreSQL offers superior integration patterns:

- **Structured Queries**: Mirror Confluence's relational data model
- **Complex Joins**: Efficient cross-table operations for content relationships
- **Full-Text Search**: Built-in capabilities that complement Confluence search

### **Updated Architecture Recommendation:**

yaml

```yaml
Database Services:
  Primary Store: 
    - Amazon RDS PostgreSQL (Multi-AZ)
    - Read replicas for analytics workloads
  
  Caching Layer:
    - ElastiCache Redis for session data
    - CloudFront for static content delivery
  
  Search & Analytics:
    - OpenSearch for full-text search
    - S3 + Athena for data lake analytics
```

---

## AI Model Selection: GPT-4o Mini vs Claude

### **Recommendation: Hybrid Approach with GPT-4o Mini Primary**

**Cost Analysis:**

- **GPT-4o Mini**: ~$0.15-0.60 per 1M tokens
- **Claude 3.5 Sonnet (Bedrock)**: ~$3.00-15.00 per 1M tokens
- **Potential Savings**: 80-90% cost reduction for bulk operations

### **Updated AI Content Processing Service Architecture:**

yaml

```yaml
AI Processing Tiers:
  Tier 1 - Bulk Operations (GPT-4o Mini):
    - Screenshot documentation
    - Content gap analysis  
    - Translation services
    - Basic PRD generation
    - Content summarization
    
  Tier 2 - Complex Analysis (Claude via API):
    - Strategic document planning
    - Nuanced content review
    - Complex technical writing
    - Multi-document synthesis
    
  Tier 3 - Specialized Tasks (MCP + Claude):
    - Interactive content editing
    - Real-time collaboration features
    - Advanced screenshot analysis
```

### **Implementation Strategy:**

#### 1. **Smart Routing Service**

typescript

```typescript
interface AIRouter {
  routeRequest(task: DocumentationTask): AIProvider {
    if (task.complexity < COMPLEXITY_THRESHOLD) {
      return GPT4oMiniProvider;
    }
    if (task.requiresInteractivity) {
      return ClaudeMCPProvider;
    }
    return ClaudeAPIProvider;
  }
}
```

#### 2. **Cost-Optimized Processing Pipeline**

yaml

```yaml
Processing Flow:
  1. Content Ingestion → GPT-4o Mini (Classification)
  2. Simple Tasks → GPT-4o Mini (Bulk Processing)  
  3. Complex Tasks → Claude API (Quality Processing)
  4. Interactive Tasks → Claude MCP (Real-time)
  5. Quality Assurance → Hybrid Validation
```

### **Updated Microservice: AI Content Processing Service**

**Technical Specifications:**

yaml

```yaml
Runtime: AWS Lambda (Node.js/Python)
AI Providers:
  Primary: OpenAI GPT-4o Mini (via API)
  Secondary: Claude 3.5 Sonnet (via API)
  Interactive: Claude MCP (for real-time features)
Queue: SQS with priority routing
Storage: S3 for prompts, templates, and cache
Cost Monitoring: CloudWatch custom metrics
```

**Enhanced Features:**

- **Intelligent Task Routing**: Automatic model selection based on task complexity
- **Cost Monitoring**: Real-time spend tracking with alerts
- **Quality Validation**: Cross-model validation for critical content
- **Prompt Optimization**: A/B testing across models for optimal performance
- **Fallback Mechanisms**: Graceful degradation between AI providers

### **Cost Management Strategy:**

#### 1. **Usage Optimization**

yaml

```yaml
Cost Controls:
  - Prompt caching for repeated operations
  - Batch processing for bulk tasks
  - Smart chunking to minimize token usage
  - Result caching with intelligent TTL
```

#### 2. **Monitoring & Alerting**

yaml

```yaml
Metrics:
  - Cost per document processed
  - Model accuracy by task type  
  - Processing time by complexity
  - User satisfaction by AI provider
```

### **Updated Repository Recommendations:**

**AI Integration Starting Points:**

yaml

```yaml
Primary Repositories:
  - OpenAI Integration: "openai/openai-node"
  - Anthropic Integration: "anthropics/anthropic-sdk-typescript"  
  - Cost Optimization: "aws-samples/serverless-ai-cost-optimizer"
  - Multi-Provider: "microsoft/semantic-kernel"

MCP Integration:
  - Official: "modelcontextprotocol/servers"
  - TypeScript SDK: "modelcontextprotocol/typescript-sdk"
```

### **Risk Mitigation for Hybrid Approach:**

#### 1. **Quality Assurance**

- Cross-validation between models for critical content
- Human review workflows for high-stakes documentation
- Quality scoring with automatic escalation

#### 2. **Cost Management**

- Monthly budget caps with automatic throttling
- Real-time cost alerts at 75% and 90% thresholds
- Automatic downgrade to cheaper models when approaching limits

#### 3. **Vendor Risk**

- Multi-provider architecture prevents vendor lock-in
- Fallback mechanisms ensure service continuity
- Standardized prompt templates across providers

### **Expected Outcomes:**

**Cost Savings:**

- 80-90% reduction in AI processing costs
- Maintained quality for 95% of use cases
- ROI improvement from 6 months to 3 months

**Performance Benefits:**

- Faster processing for bulk operations
- Maintained quality for complex tasks
- Improved cost predictability

This hybrid approach maximizes cost efficiency while maintaining the quality and capability advantages that made Claude attractive for your technical writing use cases.

Retry

![Release Notes Workflow and Responsibilities.pdf](/api/d112de9b-afab-4f89-a2bd-35979f7390e5/files/b7e21986-fda1-44fa-8940-3dead7200722/thumbnail)

pdf

### Proof of Concept for Standardizing EPICs and Release Notes Fields in JIRA for generating Release Notes.docx

212 lines

docx

K

What are key elements from the Jira side that need to be built into the PRD for the Jira upfront trigger? As well as a basic how to for users to know how to fill out the Jira properly (or an AI via a webbrowser plugin that gives them real time feedback when the info isn't filled out as expected and therefore will give bad results)

Edit

# Updated PRD: Jira Integration Requirements for Automated Release Notes

## Jira Standardization Requirements

### Critical Jira Fields to Implement

Based on the release notes automation requirements, the following fields must be standardized across all projects:

#### **1. Core Release Notes Fields (All Issue Types)**

yaml

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

yaml

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

yaml

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

yaml

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

javascript

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

yaml

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

sql

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

sql

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

sql

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

sql

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

yaml

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

yaml

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

yaml

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

yaml

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

yaml

```yaml
Tasks:
  - Create custom fields across all projects (XCP, NVO, WS, Extreme AI Expert)
  - Configure field schemes and screen layouts
  - Set up validation rules and required field logic
  - Create JQL templates for each project
  - Configure workflow transitions based on field values
```

### **Phase 2: Browser Extension Development (Week 3-4)**

yaml

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

yaml

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

yaml

```yaml
Targets:
  - 95% of issues have complete required fields
  - 90% of Symptom/Condition pairs are sufficiently different
  - 85% of Release Notes descriptions meet quality standards
  - <5% issues require manual intervention during generation
```

### **User Adoption Metrics**

yaml

```yaml
Targets:
  - 80% of users enable browser extension within 30 days
  - 90% field completion rate with real-time assistance
  - 75% reduction in "back-and-forth" on field corrections
  - 60% improvement in first-draft release notes quality
```

This comprehensive approach ensures both the technical infrastructure and user experience support high-quality, automated release notes generation while maintaining the flexibility needed across different project types.

Retry

K

Not all of these will be standardized fields in Jira - wha

Also not 'Release Notes' required - but Documentation required - and does this really need to be a field or can it be part of the plugin

Edit

You're absolutely right. Let me refactor this with a more practical approach:

# Refined PRD: Jira Plugin for Documentation Automation

## Core Philosophy: Minimal Jira Changes + Smart Plugin Logic

### **What Actually Needs to be Standardized in Jira**

#### **Essential Custom Fields Only (4 fields max)**

yaml

```yaml
Required Custom Fields:
  1. "Documentation Required": Yes/No/Auto-Detect
     - Plugin can auto-detect based on issue type, labels, components
     - Override capability for edge cases
     
  2. "Disclosure Status": 
     - Internal Only | Approved for Publication | Under Review
     - Critical for security/compliance
     
  3. "Customer Impact": 
     - None | Low | Medium | High | Critical
     - Helps prioritize what goes in release notes
     
  4. "Documentation Notes": Long Text (Optional)
     - Override/supplement auto-generated content
     - Plugin uses this when present, generates when empty
```

### **Plugin-Based Intelligence Instead of Fields**

#### **Smart Content Detection Logic**

javascript

```javascript
// Plugin logic for determining documentation requirements
const shouldIncludeInDocs = (issue) => {
  // Auto-detect patterns instead of requiring fields
  const autoDetectRules = {
    // Always include if explicitly marked
    explicit: issue.customFields['Documentation Required'] === 'Yes',
    
    // Auto-include based on issue characteristics  
    customerFacing: [
      issue.labels?.includes('customer-facing'),
      issue.components?.some(c => c.name.includes('UI')),
      issue.issueType === 'Bug' && issue.priority >= 'High',
      issue.resolution === 'Fixed' && issue.affects?.includes('Production')
    ].some(Boolean),
    
    // Exclude internal-only items
    exclude: [
      issue.labels?.includes('internal-only'),
      issue.customFields['Disclosure Status'] === 'Internal Only',
      issue.summary?.toLowerCase().includes('test'),
      issue.components?.some(c => c.name.includes('Internal'))
    ].some(Boolean)
  };
  
  return autoDetectRules.explicit || 
         (autoDetectRules.customerFacing && !autoDetectRules.exclude);
};
```

## Jira Plugin Architecture

### **Microservice 7: Jira Content Intelligence Service**

yaml

```yaml
Purpose: Smart content extraction and categorization without heavy field requirements

Technical Specifications:
  Runtime: AWS Lambda (Node.js)
  AI Provider: GPT-4o Mini (cost-effective classification)
  Triggers: 
    - Jira webhook events (issue updated/resolved)
    - Scheduled batch processing
    - On-demand via plugin UI
  Storage: S3 for processed content cache
```

### **Plugin Features (No New Fields Required)**

#### **1. Intelligent Content Extraction**

javascript

```javascript
// Extract documentation content from existing fields
const extractDocumentationContent = (issue) => {
  const content = {
    // Use existing fields creatively
    symptom: extractSymptom(issue.summary, issue.description),
    condition: extractCondition(issue.description, issue.comments),
    workaround: extractWorkaround(issue.comments, issue.resolution),
    
    // AI-enhanced categorization
    category: classifyIssue(issue), // "defect-cwc", "defect-cwoc", "enhancement", etc.
    severity: determineSeverity(issue.priority, issue.labels, issue.components),
    
    // Smart formatting
    customerDescription: generateCustomerFriendlyDescription(issue)
  };
  
  return content;
};
```

#### **2. Real-Time Field Enhancement (Browser Extension)**

yaml

```yaml
Features:
  - Overlay suggestions on existing Jira fields
  - Real-time validation of Summary/Description quality
  - AI-powered content improvement suggestions
  - Auto-categorization feedback
  - Documentation preview before save

Implementation:
  - Chrome Extension injecting into Jira UI
  - No new Jira fields required
  - Uses existing field content for AI processing
```

### **Content Categorization Logic**

#### **Auto-Detection Rules (No Custom Fields)**

yaml

```yaml
Defects Closed with Code Changes (CWC):
  Detection Logic:
    - Issue Type: Bug/Defect
    - Status: Closed/Resolved  
    - Resolution: Fixed/Done
    - Has code commits linked OR fix version set
    - Priority: Medium+ OR has customer-facing labels

Defects Closed without Code Changes (CWOC):
  Detection Logic:
    - Issue Type: Bug/Defect
    - Status: Closed
    - Resolution: Won't Fix | Duplicate | Cannot Reproduce
    - Customer Impact: Medium+ (custom field)

Open Defects:
  Detection Logic:
    - Issue Type: Bug/Defect
    - Status: Open | In Progress | Reopened
    - Priority: High+ OR customer-facing labels
    - Created > 30 days ago (configurable)

Features/Enhancements:
  Detection Logic:
    - Issue Type: Story | Epic | New Feature
    - Status: Done/Closed
    - Has release notes in description OR significant customer impact
```

## JQL Templates (Using Existing + Minimal Custom Fields)

### **Revised JQL Queries**

sql

```sql
-- CWC Defects (minimal custom field usage)
"Target Version/s" = "{VERSION}" 
AND issuetype in (Bug, Defect) 
AND status in (Closed, Resolved) 
AND resolution in (Fixed, Done)
AND (
  "Customer Impact" in (Medium, High, Critical) 
  OR labels in (customer-facing, production-impact)
  OR priority in (High, Highest)
)
AND "Disclosure Status" != "Internal Only"
ORDER BY priority DESC, key ASC

-- Open Defects (using existing fields primarily)
project in ({PROJECT_LIST}) 
AND issuetype in (Bug, Defect) 
AND status not in (Closed, Resolved, Done) 
AND (
  priority in (High, Highest, Critical)
  OR "Customer Impact" in (High, Critical)
  OR labels in (customer-facing)
)
AND "Disclosure Status" = "Approved for Publication"
ORDER BY priority DESC, created ASC

-- Platform Content (Epic-based, minimal custom fields)
issuetype = Epic 
AND "Target Version/s" = "{VERSION}"
AND (
  summary ~ "Introduction to.*"
  OR summary ~ "Prerequisites.*" 
  OR summary ~ "Supported Applications.*"
  OR summary ~ "Features.*"
)
AND "Disclosure Status" != "Internal Only"
ORDER BY summary ASC
```

## User Experience Without Heavy Field Requirements

### **Plugin UI Overlay Approach**

yaml

```yaml
Browser Extension Features:
  1. Smart Field Enhancement:
     - Overlay AI suggestions on Summary field
     - Real-time quality scoring of Description
     - Auto-suggest labels based on content
     
  2. Documentation Preview:
     - Show how issue will appear in release notes
     - Preview generated customer-friendly description
     - Highlight missing information that would improve output
     
  3. One-Click Optimization:
     - "Optimize for Documentation" button
     - Auto-enhance existing field content
     - Suggest additional context in comments
```

### **Minimal Training Required**

yaml

```yaml
User Guidelines:
  "Just write good summaries and descriptions - the plugin handles the rest"
  
  Key Practices:
    1. Clear, descriptive summaries
    2. Detailed descriptions with context
    3. Use existing labels appropriately (customer-facing, etc.)
    4. Set priority based on actual impact
    5. Use comments for workarounds and additional context
```

## Implementation Strategy

### **Phase 1: Plugin Foundation (Week 1-2)**

yaml

```yaml
Tasks:
  - Add 4 essential custom fields only
  - Build content extraction AI service
  - Create basic JQL templates using existing fields
  - Develop classification algorithms
```

### **Phase 2: Browser Extension (Week 3-4)**

yaml

```yaml
Tasks:
  - Chrome extension for Jira UI enhancement
  - Real-time content analysis and suggestions
  - Documentation preview functionality
  - Integration with AI processing service
```

### **Phase 3: Intelligent Automation (Week 5-6)**

yaml

```yaml
Tasks:
  - Automated issue categorization
  - Batch processing for existing issues
  - Release notes generation pipeline
  - Quality scoring and feedback loops
```

## Benefits of This Approach

### **For Users:**

- Minimal change to existing workflow
- No complex field training required
- AI does the heavy lifting
- Real-time feedback improves quality

### **For Organization:**

- Leverages existing Jira investment
- No disruptive field standardization project
- Faster implementation timeline
- Lower adoption resistance

### **For Documentation Quality:**

- AI ensures consistency
- Smart categorization reduces errors
- Automated content enhancement
- Scalable across all projects

This approach maximizes automation while minimizing disruption to existing Jira workflows and user habits.

Retry

K

This will also be a playwright plugin integrated with a webbrowser extension to interact with the companies demo environment and highlight the key changes in the UI since the previous release

These Jira's are likely to only provide additional (but also need to work as well as they can as a stand alone feature too - if the playwright version doesn't exist)

There are also recording demos that could provide additional context if needed (or follow up a user to do a quick Loom run through of other things the documentation should consider after they review the draft documents). How could the plugin

It can also pull into Github Repos where alerts or API BE features render on the front end (so both English and translated versions of these stay consistent with final product documentation)

Include these in an overarching PRD and recommend which one to start testing with first

Edit

# Comprehensive PRD: Multi-Modal Documentation Intelligence Platform

## Executive Summary

A unified documentation platform that combines Jira workflow intelligence, UI change detection via Playwright automation, GitHub API integration, and multi-modal content generation to create comprehensive, accurate release documentation with minimal manual effort.

## System Architecture Overview

yaml

```yaml
Core Components:
  1. Jira Intelligence Layer (Workflow & Content)
  2. UI Change Detection System (Playwright + Browser Extension)
  3. GitHub Integration Service (API/Alert Documentation)
  4. Multi-Modal Content Generation (AI + Human Feedback Loop)
  5. Demo Recording Integration (Loom/Video Analysis)
  6. Translation Consistency Engine
```

## Component Specifications

### **Component 1: Jira Intelligence Service**

_(Previously Detailed - Core Foundation)_

**Status**: Foundation component - must work standalone **Priority**: Implement first for immediate value

yaml

```yaml
Standalone Capabilities:
  - Smart content extraction from existing Jira fields
  - AI-powered categorization and documentation generation
  - Release notes automation from Jira data alone
  - Quality scoring and gap identification

Enhanced Capabilities (when integrated):
  - Cross-reference with UI changes from Playwright
  - Validate against GitHub API changes
  - Incorporate demo recording insights
```

### **Component 2: UI Change Detection System**

**Purpose**: Automated detection and documentation of UI changes between releases

#### **Microservice 9: Playwright Automation Service**

yaml

```yaml
Technical Specifications:
  Runtime: AWS Lambda (with custom Playwright layer)
  Triggers: 
    - Scheduled runs (nightly/weekly)
    - Release branch deployments
    - Manual trigger via Jira plugin
  Storage: S3 for screenshots, diff images, and analysis results
  AI Integration: GPT-4o Mini for change analysis and description
```

**Core Features:**

javascript

```javascript
// Playwright automation workflow
const uiChangeDetection = {
  environments: {
    baseline: 'demo-env-previous-release',
    current: 'demo-env-current-release'
  },
  
  workflows: [
    {
      name: 'navigation-flows',
      steps: ['login', 'dashboard', 'key-features', 'settings'],
      capture: ['screenshots', 'network-requests', 'console-logs']
    },
    {
      name: 'feature-workflows', 
      steps: ['create-item', 'edit-item', 'delete-item'],
      capture: ['screenshots', 'form-interactions', 'api-calls']
    }
  ],
  
  analysis: {
    visualDiff: 'pixel-perfect-comparison',
    functionalDiff: 'interaction-flow-changes', 
    contentDiff: 'text-and-label-changes',
    apiDiff: 'backend-integration-changes'
  }
};
```

#### **Browser Extension Integration**

yaml

```yaml
Extension Features:
  - Real-time highlighting of detected changes
  - Overlay documentation suggestions on UI elements
  - Click-to-document workflow for manual additions
  - Integration with Jira issue creation
  - Screenshot annotation tools

Technical Implementation:
  - Chrome Extension (Manifest V3)
  - WebSocket connection to Playwright service
  - Real-time change highlighting overlay
  - Direct integration with demo environments
```

### **Component 3: GitHub Integration Service**

**Purpose**: Track API changes, alerts, and backend features that impact documentation

#### **Microservice 10: GitHub Documentation Sync Service**

yaml

```yaml
Technical Specifications:
  Runtime: AWS Lambda (Node.js)
  Triggers: GitHub webhooks, scheduled scans
  Integration: GitHub GraphQL API, REST API
  AI Processing: GPT-4o Mini for change impact analysis
  Storage: S3 for processed change logs and documentation updates
```

**Key Features:**

javascript

```javascript
const githubIntegration = {
  monitoring: {
    apiChanges: {
      files: ['*/api/**/*.js', '*/routes/**/*.js', '*/controllers/**/*.js'],
      triggers: ['openapi-spec-changes', 'endpoint-modifications'],
      analysis: 'impact-on-frontend-documentation'
    },
    
    alertSystems: {
      files: ['*/alerts/**/*.js', '*/notifications/**/*.js'],
      triggers: ['new-alert-types', 'message-template-changes'],
      analysis: 'user-facing-alert-documentation'
    },
    
    featureFlags: {
      files: ['*/features/**/*.js', '*/config/features.json'],
      triggers: ['new-features', 'feature-deprecation'],
      analysis: 'documentation-impact-assessment'
    }
  },
  
  documentation: {
    extraction: 'auto-extract-jsdoc-comments',
    translation: 'sync-with-i18n-files',
    validation: 'cross-reference-with-ui-changes'
  }
};
```

### **Component 4: Demo Recording Integration Service**

**Purpose**: Leverage existing demo recordings and request targeted follow-ups

#### **Microservice 11: Video Content Analysis Service**

yaml

```yaml
Technical Specifications:
  Runtime: AWS Lambda + MediaConvert
  AI Integration: 
    - Amazon Transcribe (speech-to-text)
    - GPT-4o Mini (content analysis)
    - Amazon Rekognition (visual analysis)
  Storage: S3 for video processing and analysis results
  Integration: Loom API, internal recording systems
```

**Features:**

yaml

```yaml
Automated Analysis:
  - Transcribe demo recordings to text
  - Extract key feature demonstrations
  - Identify gaps between recorded demos and detected changes
  - Generate follow-up questions for demo creators

Follow-up Automation:
  - Auto-generate Loom recording requests
  - Template-based follow-up messages
  - Integration with team notification systems
  - Tracking of requested vs. completed follow-ups

Content Enhancement:
  - Extract visual workflows from recordings
  - Generate step-by-step documentation from demos
  - Cross-reference with UI change detection
  - Identify missing documentation areas
```

### **Component 5: Translation Consistency Engine**

**Purpose**: Ensure UI changes, API responses, and documentation stay consistent across languages

#### **Microservice 12: Multi-Language Consistency Service**

yaml

```yaml
Technical Specifications:
  Runtime: AWS Lambda (Python)
  Translation: AWS Translate + Custom Glossaries
  Validation: Cross-language consistency checking
  Storage: S3 for translation memories and glossaries
  Integration: GitHub i18n files, Jira content, UI text extraction
```

**Key Features:**

javascript

```javascript
const translationConsistency = {
  sources: {
    ui: 'extracted-from-playwright-screenshots',
    api: 'github-i18n-json-files', 
    documentation: 'jira-generated-content',
    alerts: 'github-alert-templates'
  },
  
  validation: {
    terminology: 'consistent-product-names-across-languages',
    context: 'ui-context-matches-documentation-context',
    completeness: 'all-languages-have-equivalent-content'
  },
  
  automation: {
    detection: 'flag-inconsistencies-across-sources',
    correction: 'suggest-updates-for-out-of-sync-content',
    workflow: 'create-jira-issues-for-translation-updates'
  }
};
```

## Integration Architecture

### **Data Flow Between Components**

mermaid

```mermaid
graph TD
    A[Jira Issues] --> B[Content Intelligence]
    C[Playwright UI Detection] --> B
    D[GitHub Changes] --> B
    E[Demo Recordings] --> B
    B --> F[AI Content Generation]
    F --> G[Multi-Language Processing]
    G --> H[Documentation Output]
    
    I[Browser Extension] --> C
    I --> A
    J[Follow-up Automation] --> E
    K[Translation Validation] --> G
```

### **Cross-Component Intelligence**

yaml

```yaml
Enhanced Documentation Generation:
  Base: Jira content extraction (standalone capable)
  + UI Changes: Playwright-detected modifications
  + API Changes: GitHub integration insights  
  + Demo Context: Video analysis and follow-ups
  + Translation: Multi-language consistency
  
Result: Comprehensive, accurate, multi-modal documentation
```

## Implementation Roadmap

### **Phase 1: Foundation (Weeks 1-4) - START HERE**

**Priority: Jira Intelligence Service**

yaml

```yaml
Why Start Here:
  ✓ Immediate value with existing data
  ✓ Standalone functionality
  ✓ Foundation for all other components
  ✓ Fastest ROI
  ✓ Minimal external dependencies

Deliverables:
  - Jira custom fields (4 fields max)
  - AI content extraction service
  - Browser extension for Jira enhancement
  - Basic release notes automation
  - JQL templates and workflows
```

**Success Criteria:**

- Generate release notes from Jira data alone
- 70% reduction in manual documentation time
- User adoption >60% within 30 days

### **Phase 2: UI Change Detection (Weeks 5-8)**

**Priority: Playwright + Browser Extension**

yaml

```yaml
Why Second:
  ✓ Builds on Jira foundation
  ✓ High visual impact for stakeholders
  ✓ Addresses major gap in current process
  ✓ Enables demo environment integration

Deliverables:
  - Playwright automation service
  - UI change detection algorithms
  - Browser extension UI overlay
  - Integration with Jira content generation
  - Demo environment screenshot workflows
```

### **Phase 3: GitHub Integration (Weeks 9-12)**

**Priority: API/Backend Change Tracking**

yaml

```yaml
Why Third:
  ✓ Complements UI changes with backend context
  ✓ Ensures technical accuracy
  ✓ Addresses developer-facing documentation
  ✓ API consistency validation

Deliverables:
  - GitHub webhook integration
  - API change detection and analysis
  - Cross-reference with UI changes
  - Enhanced technical documentation
  - Translation file consistency checking
```

### **Phase 4: Multi-Modal Enhancement (Weeks 13-16)**

**Priority: Demo Integration + Translation**

yaml

```yaml
Why Last:
  ✓ Builds on all previous components
  ✓ Adds sophisticated content enhancement
  ✓ Addresses remaining edge cases
  ✓ Completes the comprehensive solution

Deliverables:
  - Video analysis service
  - Automated follow-up workflows
  - Translation consistency engine
  - Multi-language documentation
  - Complete end-to-end automation
```

## Testing Strategy by Component

### **Phase 1 Testing (Jira Intelligence)**

yaml

```yaml
Test Scenarios:
  - Generate release notes from XCP, NVO, WS projects
  - Validate AI categorization accuracy (target: >85%)
  - Test browser extension with real user workflows
  - Measure documentation quality improvement
  - Load test with historical Jira data
```

### **Phase 2 Testing (UI Detection)**

yaml

```yaml
Test Scenarios:
  - Run Playwright against known UI changes
  - Validate change detection accuracy (target: >90%)
  - Test browser extension overlay functionality
  - Cross-reference detected changes with Jira issues
  - Performance test with multiple demo environments
```

### **Phase 3 Testing (GitHub Integration)**

yaml

```yaml
Test Scenarios:
  - Monitor API changes in development branches
  - Validate translation file consistency
  - Test webhook reliability and processing speed
  - Cross-validate with UI change detection
  - Accuracy test with known backend changes
```

### **Phase 4 Testing (Multi-Modal)**

yaml

```yaml
Test Scenarios:
  - Process existing demo recording library
  - Test automated follow-up generation
  - Validate translation consistency across all sources
  - End-to-end workflow with all components
  - User acceptance testing with complete system
```

## Expected Outcomes by Phase

### **Phase 1 Results:**

- 70% reduction in release notes creation time
- Immediate productivity gains for technical writing team
- Foundation for all subsequent enhancements

### **Phase 2 Results:**

- 90% reduction in UI change documentation gaps
- Visual validation of release content accuracy
- Enhanced demo environment integration

### **Phase 3 Results:**

- Complete technical accuracy for API changes
- Consistent documentation across all languages
- Developer-facing documentation automation

### **Phase 4 Results:**

- Comprehensive, multi-modal documentation
- 95% automation of release documentation process
- Seamless integration across all content sources

**Recommendation: Start with Phase 1 (Jira Intelligence) for immediate value and strong foundation, then proceed sequentially through the phases based on organizational priorities and resource availability.**

Retry

K

How can I run Jira component 1 locally as a test on my computer (in prep for a plugin service I will run as an MVP)

Edit

# Local Jira Testing Setup for Component 1

## Overview

You'll create a local development environment that can connect to your actual Jira instance to test the AI content extraction and processing logic before building the full plugin.

## Setup Architecture

yaml

```yaml
Local Development Stack:
  - Node.js application (Jira API integration)
  - Local PostgreSQL (for caching/testing data)
  - OpenAI API integration (GPT-4o Mini)
  - Web interface for testing/validation
  - Docker containers for easy setup
```

## Step 1: Project Structure Setup

bash

```bash
mkdir jira-doc-intelligence
cd jira-doc-intelligence

# Create project structure
mkdir -p {src,config,tests,docker,docs}
mkdir -p src/{services,utils,api,web}

# Initialize Node.js project
npm init -y
```

### **Package.json Dependencies**

json

```json
{
  "name": "jira-doc-intelligence-local",
  "version": "1.0.0",
  "scripts": {
    "dev": "nodemon src/server.js",
    "test": "jest",
    "docker:up": "docker-compose up -d",
    "docker:down": "docker-compose down"
  },
  "dependencies": {
    "express": "^4.18.2",
    "node-fetch": "^3.3.2",
    "openai": "^4.20.1",
    "pg": "^8.11.3",
    "dotenv": "^16.3.1",
    "cors": "^2.8.5",
    "helmet": "^7.1.0",
    "winston": "^3.11.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.7.0",
    "supertest": "^6.3.3"
  }
}
```

## Step 2: Docker Setup for Local Dependencies

### **docker-compose.yml**

yaml

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: jira_doc_intelligence
      POSTGRES_USER: dev_user
      POSTGRES_PASSWORD: dev_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/init.sql:/docker-entrypoint-initdb.d/init.sql

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### **docker/init.sql**

sql

```sql
-- Initialize database schema
CREATE TABLE IF NOT EXISTS jira_issues (
    id SERIAL PRIMARY KEY,
    jira_key VARCHAR(50) UNIQUE NOT NULL,
    issue_type VARCHAR(50),
    status VARCHAR(50),
    priority VARCHAR(50),
    summary TEXT,
    description TEXT,
    created_date TIMESTAMP,
    updated_date TIMESTAMP,
    raw_data JSONB,
    processed_at TIMESTAMP,
    ai_analysis JSONB
);

CREATE TABLE IF NOT EXISTS documentation_content (
    id SERIAL PRIMARY KEY,
    jira_key VARCHAR(50) REFERENCES jira_issues(jira_key),
    content_type VARCHAR(50), -- 'symptom', 'condition', 'workaround', etc.
    generated_content TEXT,
    confidence_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_jira_key ON jira_issues(jira_key);
CREATE INDEX idx_content_type ON documentation_content(content_type);
```

## Step 3: Environment Configuration

### **.env**

bash

```bash
# Jira Configuration
JIRA_BASE_URL=https://your-company.atlassian.net
JIRA_USERNAME=your-email@company.com
JIRA_API_TOKEN=your_jira_api_token

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini

# Database Configuration
DATABASE_URL=postgresql://dev_user:dev_password@localhost:5432/jira_doc_intelligence

# Redis Configuration
REDIS_URL=redis://localhost:6379

# Server Configuration
PORT=3000
NODE_ENV=development
```

### **How to Get Jira API Token:**

1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Create API token
3. Use your email as username, API token as password

## Step 4: Core Services Implementation

### **src/services/jiraService.js**

javascript

```javascript
const axios = require('axios');

class JiraService {
  constructor() {
    this.baseUrl = process.env.JIRA_BASE_URL;
    this.auth = {
      username: process.env.JIRA_USERNAME,
      password: process.env.JIRA_API_TOKEN
    };
  }

  // Test JQL queries from your documentation
  async getIssuesByJQL(jql, maxResults = 50) {
    try {
      const response = await axios.get(`${this.baseUrl}/rest/api/3/search`, {
        auth: this.auth,
        params: {
          jql,
          maxResults,
          fields: 'summary,description,status,priority,issuetype,created,updated,resolution,labels,components'
        }
      });
      
      return response.data.issues;
    } catch (error) {
      console.error('Jira API Error:', error.response?.data || error.message);
      throw error;
    }
  }

  // Get specific issue by key
  async getIssue(issueKey) {
    try {
      const response = await axios.get(`${this.baseUrl}/rest/api/3/issue/${issueKey}`, {
        auth: this.auth,
        params: {
          fields: 'summary,description,status,priority,issuetype,created,updated,resolution,labels,components,comment'
        }
      });
      
      return response.data;
    } catch (error) {
      console.error('Jira Issue Error:', error.response?.data || error.message);
      throw error;
    }
  }

  // Test with your existing JQL from the documentation
  async getDefectsCWC(version = "25.3.0") {
    const jql = `"Target Version/s" = "${version}" 
                 AND issuetype in (Bug, Defect) 
                 AND status in (Closed, Resolved) 
                 AND resolution in (Fixed, Done)
                 ORDER BY priority DESC, key ASC`;
    
    return this.getIssuesByJQL(jql);
  }

  async getOpenDefects(projects = ["XCP", "NVO", "WS"]) {
    const projectList = projects.join('", "');
    const jql = `project in ("${projectList}") 
                 AND issuetype in (Bug, Defect) 
                 AND status not in (Closed, Resolved, Done) 
                 AND priority in (High, Highest, Critical)
                 ORDER BY priority DESC, created ASC`;
    
    return this.getIssuesByJQL(jql);
  }
}

module.exports = JiraService;
```

### **src/services/aiService.js**

javascript

```javascript
const OpenAI = require('openai');

class AIService {
  constructor() {
    this.openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });
  }

  // Extract symptom from Jira issue
  async extractSymptom(issue) {
    const prompt = `
    Extract a concise symptom description from this Jira issue for release notes:
    
    Summary: ${issue.fields.summary}
    Description: ${issue.fields.description || 'No description'}
    
    Requirements:
    - 1-2 sentences maximum
    - Customer-facing language
    - Focus on what the user observes
    - Avoid technical jargon
    
    Symptom:`;

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 150,
        temperature: 0.3
      });

      return response.choices[0].message.content.trim();
    } catch (error) {
      console.error('AI Service Error:', error);
      throw error;
    }
  }

  // Extract condition from Jira issue
  async extractCondition(issue) {
    const prompt = `
    Extract the specific condition when this issue occurs from this Jira issue:
    
    Summary: ${issue.fields.summary}
    Description: ${issue.fields.description || 'No description'}
    
    Requirements:
    - Explain when/how the issue happens
    - Must be different from the symptom
    - Include specific steps or scenarios
    - Customer-facing language
    
    Condition:`;

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 200,
        temperature: 0.3
      });

      return response.choices[0].message.content.trim();
    } catch (error) {
      console.error('AI Service Error:', error);
      throw error;
    }
  }

  // Classify issue for documentation
  async classifyIssue(issue) {
    const prompt = `
    Classify this Jira issue for release notes documentation:
    
    Issue Type: ${issue.fields.issuetype.name}
    Status: ${issue.fields.status.name}
    Resolution: ${issue.fields.resolution?.name || 'Unresolved'}
    Priority: ${issue.fields.priority?.name || 'Unknown'}
    Summary: ${issue.fields.summary}
    
    Categories:
    - defect-cwc: Defect closed with code changes
    - defect-cwoc: Defect closed without code changes  
    - open-defect: Open defect needing documentation
    - enhancement: New feature or improvement
    - known-issue: Known limitation to document
    - exclude: Should not be in release notes
    
    Category:`;

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 50,
        temperature: 0.1
      });

      return response.choices[0].message.content.trim().toLowerCase();
    } catch (error) {
      console.error('AI Classification Error:', error);
      return 'unknown';
    }
  }

  // Generate complete documentation content
  async generateDocumentationContent(issue) {
    const [symptom, condition, category] = await Promise.all([
      this.extractSymptom(issue),
      this.extractCondition(issue), 
      this.classifyIssue(issue)
    ]);

    return {
      symptom,
      condition,
      category,
      issueKey: issue.key,
      confidence: this.calculateConfidence(issue, symptom, condition)
    };
  }

  calculateConfidence(issue, symptom, condition) {
    let score = 0.5; // Base score
    
    // Boost for good description
    if (issue.fields.description && issue.fields.description.length > 50) score += 0.2;
    
    // Boost for clear summary
    if (issue.fields.summary.length > 20) score += 0.1;
    
    // Boost for different symptom/condition
    if (symptom !== condition) score += 0.2;
    
    return Math.min(score, 1.0);
  }
}

module.exports = AIService;
```

### **src/api/testRoutes.js**

javascript

```javascript
const express = require('express');
const JiraService = require('../services/jiraService');
const AIService = require('../services/aiService');

const router = express.Router();
const jiraService = new JiraService();
const aiService = new AIService();

// Test Jira connection
router.get('/test-connection', async (req, res) => {
  try {
    const issues = await jiraService.getIssuesByJQL('project = XCP ORDER BY created DESC', 5);
    res.json({
      success: true,
      message: `Connected successfully. Found ${issues.length} issues`,
      sample: issues.map(i => ({ key: i.key, summary: i.fields.summary }))
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

// Test AI processing on a specific issue
router.get('/test-ai/:issueKey', async (req, res) => {
  try {
    const { issueKey } = req.params;
    const issue = await jiraService.getIssue(issueKey);
    const documentation = await aiService.generateDocumentationContent(issue);
    
    res.json({
      success: true,
      issue: {
        key: issue.key,
        summary: issue.fields.summary,
        status: issue.fields.status.name,
        type: issue.fields.issuetype.name
      },
      generated: documentation
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

// Test batch processing
router.get('/test-batch/:project', async (req, res) => {
  try {
    const { project } = req.params;
    const jql = `project = ${project} AND status in (Closed, Resolved) ORDER BY updated DESC`;
    const issues = await jiraService.getIssuesByJQL(jql, 10);
    
    const processed = await Promise.all(
      issues.slice(0, 3).map(async (issue) => {
        const documentation = await aiService.generateDocumentationContent(issue);
        return {
          key: issue.key,
          summary: issue.fields.summary,
          documentation
        };
      })
    );
    
    res.json({
      success: true,
      processed
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

module.exports = router;
```

### **src/server.js**

javascript

```javascript
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Routes
app.use('/api/test', require('./api/testRoutes'));

// Basic web interface
app.get('/', (req, res) => {
  res.send(`
    <html>
      <head><title>Jira Doc Intelligence Local Test</title></head>
      <body>
        <h1>Jira Documentation Intelligence - Local Testing</h1>
        <h2>Test Endpoints:</h2>
        <ul>
          <li><a href="/api/test/test-connection">Test Jira Connection</a></li>
          <li><a href="/api/test/test-ai/XCP-7262">Test AI Processing (replace with real issue key)</a></li>
          <li><a href="/api/test/test-batch/XCP">Test Batch Processing (replace with real project)</a></li>
        </ul>
        <p>Make sure to update your .env file with real Jira credentials!</p>
      </body>
    </html>
  `);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('Available endpoints:');
  console.log('- GET / (this page)');
  console.log('- GET /api/test/test-connection');
  console.log('- GET /api/test/test-ai/:issueKey');
  console.log('- GET /api/test/test-batch/:project');
});
```

## Step 5: Running the Local Test

### **Installation & Setup**

bash

```bash
# Install dependencies
npm install

# Start Docker services
npm run docker:up

# Start the development server
npm run dev
```

### **Testing Workflow**

1. **Test Jira Connection:**
    
    ```
    http://localhost:3000/api/test/test-connection
    ```
    
2. **Test AI Processing on Specific Issue:**
    
    ```
    http://localhost:3000/api/test/test-ai/XCP-7262
    ```
    
3. **Test Batch Processing:**
    
    ```
    http://localhost:3000/api/test/test-batch/XCP
    ```
    

### **Example Test Script**

Create `tests/integration.test.js`:

javascript

```javascript
const request = require('supertest');
const express = require('express');

describe('Jira Integration Tests', () => {
  test('Should connect to Jira successfully', async () => {
    const response = await request(app)
      .get('/api/test/test-connection')
      .expect(200);
    
    expect(response.body.success).toBe(true);
  });
  
  test('Should process issue with AI', async () => {
    const response = await request(app)
      .get('/api/test/test-ai/XCP-7262') // Use real issue key
      .expect(200);
    
    expect(response.body.generated).toHaveProperty('symptom');
    expect(response.body.generated).toHaveProperty('condition');
    expect(response.body.generated.symptom).not.toBe(response.body.generated.condition);
  });
});
```

## Step 6: Validation & Next Steps

### **What This Local Setup Tests:**

✅ **Jira API Integration** - Confirms your credentials and queries work  
✅ **AI Content Generation** - Tests GPT-4o Mini with your actual data  
✅ **Classification Logic** - Validates issue categorization  
✅ **Content Quality** - Ensures symptom ≠ condition requirement  
✅ **Batch Processing** - Tests scalability with multiple issues

### **Expected Output Example:**

json

```json
{
  "success": true,
  "issue": {
    "key": "XCP-7262",
    "summary": "Random Contracts listed in the Contracts table",
    "status": "Open",
    "type": "Defect"
  },
  "generated": {
    "symptom": "Random contracts appear in the Contracts table.",
    "condition": "This occurs after unlinking the portal account and can happen intermittently during account management operations.",
    "category": "open-defect",
    "issueKey": "XCP-7262",
    "confidence": 0.8
  }
}
```

### **Ready for Plugin Development:**

Once this local testing validates your approach:

1. **Extract** the core logic into reusable modules
2. **Package** as Jira Connect app or Forge app
3. **Deploy** the AI services to AWS Lambda
4. **Integrate** with your PostgreSQL + browser extension architecture

This local setup gives you confidence that your AI processing logic works with real Jira data before investing in the full plugin infrastructure.

Retry

K

Can I use Jira for free or low cost as a 1 perosn user

Edit

# Jira Pricing Options for Single User Testing

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

**Sign up**: [https://www.atlassian.com/software/jira/free](https://www.atlassian.com/software/jira/free)

## Alternative Options

### **Jira Cloud Standard (if you need more)**

- **Cost**: $7.16/user/month (when paid annually)
- **Benefits**: 250GB storage, advanced features
- **Only needed if**: Free tier limitations become problematic

### **Jira Server/Data Center (Self-hosted)**

- **Cost**: One-time license fee (~$10 for 10 users starter license)
- **Pros**: Full control, no monthly fees
- **Cons**: Requires server setup and maintenance
- **Not recommended** for testing/development

## **Recommended Setup for Your Testing**

### **Step 1: Create Free Jira Cloud Instance**

bash

```bash
# Go to Atlassian and create account
https://www.atlassian.com/software/jira/free

# Choose "Jira Software" 
# Select "Cloud" option
# Create your site: https://your-site-name.atlassian.net
```

### **Step 2: Configure for Your Testing Needs**

yaml

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

yaml

```yaml
Custom Fields to Add:
  1. "Documentation Required" (Select List: Yes/No/Auto-Detect)
  2. "Disclosure Status" (Select List: Internal Only/Approved for Publication/Under Review)  
  3. "Customer Impact" (Select List: None/Low/Medium/High/Critical)
  4. "Documentation Notes" (Paragraph Text)
```

### **Step 4: Create Test Data**

javascript

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

1. Go to: [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Create API token
3. Save securely for your `.env` file

### **Test API Access**

bash

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

## **Migration Path**

yaml

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

bash

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

yaml

```yaml
Jira Cloud Free: $0/month
OpenAI API (GPT-4o mini): ~$1-5/month (for testing)
AWS Free Tier: $0/month (first year)
Total Development Cost: ~$1-5/month
```

**Recommendation**: Start with Jira Cloud Free tier immediately. It provides everything you need for plugin development and testing, with easy migration path to your company's production Jira environment later.

The free tier is genuinely functional - not a limited trial - so you can develop and test your entire plugin architecture without any cost pressure.

Retry

### main.py

70 lines

py

K

I already have this code which I know works and is tested - can I leverage it for my test to start in any way? Also how would I need to change it for future requirements mentioned above?

Edit

# Leveraging Your Existing Code for the Test Setup

Your existing Python code is actually perfect as a starting point! It already demonstrates working Jira integration and has the basic structure we need. Let's adapt it for your test requirements and future plugin architecture.

## Step 1: Enhanced Version of Your Current Code

### **Enhanced main.py (Immediate Testing)**

python

```python
import os
import json
import boto3
from jira import JIRA
from datetime import datetime
import openai
from typing import Dict, List, Optional

# === Enhanced CONFIG ===
JIRA_SERVER = os.environ["JIRA_SERVER"]
JIRA_EMAIL = os.environ["JIRA_EMAIL"] 
JIRA_PAT = os.environ["JIRA_PAT"]

# Add OpenAI for testing AI processing
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

S3_BUCKET = "dev-sandbox-for-upstream"
S3_PREFIX = "staging/jira-md/"
OUTPUT_FOLDER = "jira_md_output"

# === Setup Clients ===
jira = JIRA(server=JIRA_SERVER, token_auth=JIRA_PAT)
s3 = boto3.client("s3")

# === Create Output Folder ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === Enhanced JQL Queries (Based on Your PRD Requirements) ===
queries = {
    # Your existing queries
    "extreme_defects_with_code_changes": (
        'project = "Extreme Cloud Platform" AND "Target Version/s" in ("XCP 25.1.0", "XCP 24.6", "XCP 24.5", "XCP 25.2.0") '
        'AND resolution = "Resolved With Code" AND "Release Notes Required" = Yes'
    ),
    "workspace_release_notes": (
        'project = Workspace AND type in (Epic, Story) AND "Target Version" = "WS 25.1.0" '
        'AND resolution = Done AND "Release Notes Required" = Yes'
    ),
    
    # New queries for testing the standardized approach
    "defects_cwc_test": (
        'issuetype in (Bug, Defect) AND status in (Closed, Resolved) '
        'AND resolution in (Fixed, Done) AND priority in (High, Highest) '
        'ORDER BY priority DESC, key ASC'
    ),
    "defects_cwoc_test": (
        'issuetype in (Bug, Defect) AND status = Closed '
        'AND resolution in ("Won\'t Fix", Duplicate, "Cannot Reproduce") '
        'ORDER BY key ASC'
    ),
    "open_defects_test": (
        'issuetype in (Bug, Defect) AND status not in (Closed, Resolved, Done) '
        'AND priority in (High, Highest, Critical) '
        'ORDER BY priority DESC, created ASC'
    ),
    "platform_epics_test": (
        'issuetype = Epic AND summary ~ "Introduction.*" OR summary ~ "Prerequisites.*" '
        'OR summary ~ "Supported Applications.*" OR summary ~ "Features.*"'
    )
}

# === AI Processing Functions (New) ===
def extract_symptom_with_ai(issue) -> Optional[str]:
    """Extract customer-facing symptom using AI"""
    if not OPENAI_API_KEY:
        return None
        
    prompt = f"""
    Extract a concise symptom description for release notes:
    
    Summary: {issue.fields.summary}
    Description: {issue.fields.description or 'No description'}
    
    Requirements:
    - 1-2 sentences maximum
    - Customer-facing language
    - Focus on what the user observes
    
    Symptom:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error for {issue.key}: {e}")
        return None

def extract_condition_with_ai(issue) -> Optional[str]:
    """Extract condition when issue occurs using AI"""
    if not OPENAI_API_KEY:
        return None
        
    prompt = f"""
    Extract the specific condition when this issue occurs:
    
    Summary: {issue.fields.summary}
    Description: {issue.fields.description or 'No description'}
    
    Requirements:
    - Explain when/how the issue happens
    - Must be different from the symptom
    - Customer-facing language
    
    Condition:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error for {issue.key}: {e}")
        return None

def classify_issue_with_ai(issue) -> str:
    """Classify issue for documentation category"""
    if not OPENAI_API_KEY:
        return "unknown"
        
    prompt = f"""
    Classify this Jira issue for release notes:
    
    Issue Type: {issue.fields.issuetype.name}
    Status: {issue.fields.status.name}
    Resolution: {getattr(issue.fields.resolution, 'name', 'Unresolved')}
    Priority: {getattr(issue.fields.priority, 'name', 'Unknown')}
    Summary: {issue.fields.summary}
    
    Categories: defect-cwc, defect-cwoc, open-defect, enhancement, known-issue, exclude
    
    Category:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.1
        )
        return response.choices[0].message.content.strip().lower()
    except Exception as e:
        print(f"AI Classification Error for {issue.key}: {e}")
        return "unknown"

# === Enhanced Issue Processing ===
def process_issue_with_ai(issue) -> Dict:
    """Process issue with AI enhancements - this is your core plugin logic"""
    
    # Basic issue info (your existing approach)
    basic_info = {
        "key": issue.key,
        "summary": issue.fields.summary,
        "status": issue.fields.status.name,
        "type": issue.fields.issuetype.name,
        "priority": getattr(issue.fields.priority, 'name', 'Unknown'),
        "resolution": getattr(issue.fields.resolution, 'name', 'Unresolved'),
        "description": issue.fields.description or "No description provided",
        "created": str(issue.fields.created),
        "updated": str(issue.fields.updated)
    }
    
    # AI-enhanced content (new capabilities)
    ai_content = {}
    if OPENAI_API_KEY:
        print(f"  Processing {issue.key} with AI...")
        ai_content = {
            "symptom": extract_symptom_with_ai(issue),
            "condition": extract_condition_with_ai(issue),
            "category": classify_issue_with_ai(issue),
            "confidence": calculate_confidence(basic_info, ai_content)
        }
    
    return {**basic_info, "ai_analysis": ai_content}

def calculate_confidence(basic_info: Dict, ai_content: Dict) -> float:
    """Calculate confidence score for AI-generated content"""
    score = 0.5  # Base score
    
    # Boost for good description
    if basic_info.get("description") and len(basic_info["description"]) > 50:
        score += 0.2
    
    # Boost for clear summary  
    if len(basic_info.get("summary", "")) > 20:
        score += 0.1
        
    # Boost for different symptom/condition
    symptom = ai_content.get("symptom", "")
    condition = ai_content.get("condition", "")
    if symptom and condition and symptom != condition:
        score += 0.2
        
    return min(score, 1.0)

# === Enhanced Markdown Generation ===
def issue_to_enhanced_markdown(issue_data: Dict) -> str:
    """Generate enhanced markdown with AI content"""
    
    md = f"""# {issue_data['key']} - {issue_data['summary']}

**Status**: {issue_data['status']}  
**Type**: {issue_data['type']}  
**Priority**: {issue_data['priority']}  
**Resolution**: {issue_data['resolution']}  

## Original Description
{issue_data['description']}

"""
    
    # Add AI analysis if available
    ai_analysis = issue_data.get("ai_analysis", {})
    if ai_analysis:
        md += f"""## AI-Generated Release Notes Content

**Category**: {ai_analysis.get('category', 'Unknown')}  
**Confidence**: {ai_analysis.get('confidence', 0):.2f}  

**Symptom**: {ai_analysis.get('symptom', 'Not generated')}  

**Condition**: {ai_analysis.get('condition', 'Not generated')}  

"""
    
    md += f"""## Metadata
- **Created**: {issue_data['created']}
- **Updated**: {issue_data['updated']}
- **Key**: {issue_data['key']}
"""
    
    return md

# === Main Processing Loop (Enhanced) ===
def main():
    """Enhanced main function with AI processing"""
    
    all_results = {}
    
    for tag, jql in queries.items():
        print(f"\n{'='*50}")
        print(f"Running query for: {tag}")
        print(f"JQL: {jql}")
        print(f"{'='*50}")
        
        # Create directory for each query
        query_folder = os.path.join(OUTPUT_FOLDER, tag)
        os.makedirs(query_folder, exist_ok=True)
        
        try:
            # Fetch issues
            issues = jira.search_issues(jql, maxResults=20, fields="*all")
            print(f"Found {len(issues)} issues")
            
            query_results = []
            
            for issue in issues:
                print(f"Processing: {issue.key}")
                
                # Process with AI (your future plugin logic)
                issue_data = process_issue_with_ai(issue)
                query_results.append(issue_data)
                
                # Generate enhanced markdown
                markdown_content = issue_to_enhanced_markdown(issue_data)
                
                # Save locally
                filename = f"{issue.key}.md"
                local_path = os.path.join(query_folder, filename)
                with open(local_path, "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                
                # Upload to S3
                try:
                    s3.upload_file(local_path, S3_BUCKET, S3_PREFIX + tag + "/" + filename)
                    print(f"  ✓ Uploaded: {filename}")
                except Exception as e:
                    print(f"  ✗ S3 Upload failed: {e}")
            
            all_results[tag] = query_results
            
        except Exception as e:
            print(f"Error processing {tag}: {e}")
    
    # Save summary results
    summary_path = os.path.join(OUTPUT_FOLDER, "processing_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, default=str)
    
    print(f"\n{'='*50}")
    print("Processing Complete!")
    print(f"Results saved to: {OUTPUT_FOLDER}")
    print(f"Summary: {summary_path}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
```

## Step 2: Requirements File

### **requirements.txt**

txt

```txt
jira==3.5.0
boto3==1.34.0
openai==1.3.0
python-dotenv==1.0.0
requests==2.31.0
```

## Step 3: Environment Setup

### **.env file**

bash

```bash
# Your existing variables
JIRA_SERVER=https://your-company.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_PAT=your_api_token

# New for AI processing
OPENAI_API_KEY=your_openai_api_key

# AWS (you already have this working)
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_DEFAULT_REGION=us-east-1
```

## Step 4: Run Enhanced Testing

bash

```bash
# Install dependencies
pip install -r requirements.txt

# Load environment variables
source .env  # or use python-dotenv

# Run enhanced processing
python main.py
```

## Step 5: Future Plugin Architecture Adaptation

### **How Your Code Adapts to Plugin Requirements:**

python

```python
# Your current code structure maps perfectly to plugin architecture:

# Current: process_issue_with_ai(issue)
# Future Plugin: Same function, called via webhook/API

# Current: issue_to_enhanced_markdown(issue_data)  
# Future Plugin: Content generation service

# Current: JQL queries dictionary
# Future Plugin: Configuration-driven query templates

# Current: S3 upload
# Future Plugin: Multi-target publishing (Confluence, S3, etc.)
```

### **Plugin Service Wrapper (Next Step)**

python

```python
# api_wrapper.py - Future plugin entry point
from flask import Flask, request, jsonify
from main import process_issue_with_ai, jira

app = Flask(__name__)

@app.route('/webhook/jira', methods=['POST'])
def jira_webhook():
    """Webhook endpoint for Jira events"""
    data = request.json
    issue_key = data.get('issue', {}).get('key')
    
    if issue_key:
        issue = jira.issue(issue_key)
        result = process_issue_with_ai(issue)
        return jsonify(result)
    
    return jsonify({"error": "No issue key found"}), 400

@app.route('/process/batch', methods=['POST'])  
def process_batch():
    """Batch processing endpoint"""
    jql = request.json.get('jql')
    issues = jira.search_issues(jql, maxResults=50)
    
    results = []
    for issue in issues:
        result = process_issue_with_ai(issue)
        results.append(result)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
```

## Immediate Benefits of Your Existing Code

✅ **Proven Jira Integration** - Your authentication and queries work  
✅ **S3 Pipeline** - Storage and processing pipeline established  
✅ **JQL Testing** - You can immediately test new query patterns  
✅ **Batch Processing** - Foundation for scalable processing  
✅ **Output Generation** - Markdown generation pipeline exists

## Quick Test Run

bash

```bash
# Test with your existing setup first
python main.py

# Then add OpenAI API key and test AI features
export OPENAI_API_KEY=your_key
python main.py

# Check output
ls jira_md_output/
cat jira_md_output/*/XCP-*.md  # See AI-enhanced output
```

## Migration Path to Full Plugin

yaml

```yaml
Phase 1 (Current): Enhanced Python Script
  ✓ Your existing code + AI processing
  ✓ Test AI content generation
  ✓ Validate JQL queries
  ✓ Proof of concept with real data

Phase 2: API Service Layer  
  - Wrap your functions in Flask/FastAPI
  - Add webhook endpoints
  - Deploy to AWS Lambda
  
Phase 3: Jira Plugin Integration
  - Convert to Jira Connect/Forge app
  - Add browser extension
  - Real-time processing
```

Your existing code gives you a massive head start - you're already 60% of the way to the core functionality! The AI processing and plugin wrapper are just additional layers on your proven foundation.

Retry

K

Rather than download to AWS can I download it locally for now

Edit

# Local Download Version of Your Enhanced Code

Absolutely! Here's your code modified to work entirely locally without AWS dependency:

## Modified main.py (Local Version)

python

```python
import os
import json
from jira import JIRA
from datetime import datetime
import openai
from typing import Dict, List, Optional
from pathlib import Path

# === Enhanced CONFIG ===
JIRA_SERVER = os.environ["JIRA_SERVER"]
JIRA_EMAIL = os.environ["JIRA_EMAIL"] 
JIRA_PAT = os.environ["JIRA_PAT"]

# Add OpenAI for testing AI processing
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# Local output configuration
OUTPUT_FOLDER = "jira_md_output"
BACKUP_FOLDER = "jira_backups"

# === Setup Clients ===
jira = JIRA(server=JIRA_SERVER, token_auth=JIRA_PAT)

# === Create Output Folders ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)

# === Enhanced JQL Queries ===
queries = {
    # Your existing queries
    "extreme_defects_with_code_changes": (
        'project = "Extreme Cloud Platform" AND "Target Version/s" in ("XCP 25.1.0", "XCP 24.6", "XCP 24.5", "XCP 25.2.0") '
        'AND resolution = "Resolved With Code" AND "Release Notes Required" = Yes'
    ),
    "workspace_release_notes": (
        'project = Workspace AND type in (Epic, Story) AND "Target Version" = "WS 25.1.0" '
        'AND resolution = Done AND "Release Notes Required" = Yes'
    ),
    
    # New test queries for your plugin development
    "defects_cwc_test": (
        'issuetype in (Bug, Defect) AND status in (Closed, Resolved) '
        'AND resolution in (Fixed, Done) AND priority in (High, Highest) '
        'ORDER BY priority DESC, key ASC'
    ),
    "defects_cwoc_test": (
        'issuetype in (Bug, Defect) AND status = Closed '
        'AND resolution in ("Won\'t Fix", Duplicate, "Cannot Reproduce") '
        'ORDER BY key ASC'
    ),
    "open_defects_test": (
        'issuetype in (Bug, Defect) AND status not in (Closed, Resolved, Done) '
        'AND priority in (High, Highest, Critical) '
        'ORDER BY priority DESC, created ASC'
    ),
    "platform_epics_test": (
        'issuetype = Epic AND (summary ~ "Introduction.*" OR summary ~ "Prerequisites.*" '
        'OR summary ~ "Supported Applications.*" OR summary ~ "Features.*")'
    )
}

# === AI Processing Functions ===
def extract_symptom_with_ai(issue) -> Optional[str]:
    """Extract customer-facing symptom using AI"""
    if not OPENAI_API_KEY:
        return None
        
    prompt = f"""
    Extract a concise symptom description for release notes:
    
    Summary: {issue.fields.summary}
    Description: {issue.fields.description or 'No description'}
    
    Requirements:
    - 1-2 sentences maximum
    - Customer-facing language
    - Focus on what the user observes
    
    Symptom:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error for {issue.key}: {e}")
        return None

def extract_condition_with_ai(issue) -> Optional[str]:
    """Extract condition when issue occurs using AI"""
    if not OPENAI_API_KEY:
        return None
        
    prompt = f"""
    Extract the specific condition when this issue occurs:
    
    Summary: {issue.fields.summary}
    Description: {issue.fields.description or 'No description'}
    
    Requirements:
    - Explain when/how the issue happens
    - Must be different from the symptom
    - Customer-facing language
    
    Condition:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error for {issue.key}: {e}")
        return None

def classify_issue_with_ai(issue) -> str:
    """Classify issue for documentation category"""
    if not OPENAI_API_KEY:
        return "unknown"
        
    prompt = f"""
    Classify this Jira issue for release notes:
    
    Issue Type: {issue.fields.issuetype.name}
    Status: {issue.fields.status.name}
    Resolution: {getattr(issue.fields.resolution, 'name', 'Unresolved')}
    Priority: {getattr(issue.fields.priority, 'name', 'Unknown')}
    Summary: {issue.fields.summary}
    
    Categories: defect-cwc, defect-cwoc, open-defect, enhancement, known-issue, exclude
    
    Category:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.1
        )
        return response.choices[0].message.content.strip().lower()
    except Exception as e:
        print(f"AI Classification Error for {issue.key}: {e}")
        return "unknown"

# === Enhanced Issue Processing ===
def process_issue_with_ai(issue) -> Dict:
    """Process issue with AI enhancements - this is your core plugin logic"""
    
    # Basic issue info (your existing approach)
    basic_info = {
        "key": issue.key,
        "summary": issue.fields.summary,
        "status": issue.fields.status.name,
        "type": issue.fields.issuetype.name,
        "priority": getattr(issue.fields.priority, 'name', 'Unknown'),
        "resolution": getattr(issue.fields.resolution, 'name', 'Unresolved'),
        "description": issue.fields.description or "No description provided",
        "created": str(issue.fields.created),
        "updated": str(issue.fields.updated),
        "assignee": issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned"
    }
    
    # AI-enhanced content (new capabilities)
    ai_content = {}
    if OPENAI_API_KEY:
        print(f"  Processing {issue.key} with AI...")
        symptom = extract_symptom_with_ai(issue)
        condition = extract_condition_with_ai(issue)
        category = classify_issue_with_ai(issue)
        
        ai_content = {
            "symptom": symptom,
            "condition": condition,
            "category": category,
            "confidence": calculate_confidence(basic_info, {"symptom": symptom, "condition": condition})
        }
    
    return {**basic_info, "ai_analysis": ai_content}

def calculate_confidence(basic_info: Dict, ai_content: Dict) -> float:
    """Calculate confidence score for AI-generated content"""
    score = 0.5  # Base score
    
    # Boost for good description
    if basic_info.get("description") and len(basic_info["description"]) > 50:
        score += 0.2
    
    # Boost for clear summary  
    if len(basic_info.get("summary", "")) > 20:
        score += 0.1
        
    # Boost for different symptom/condition
    symptom = ai_content.get("symptom", "")
    condition = ai_content.get("condition", "")
    if symptom and condition and symptom != condition:
        score += 0.2
        
    return min(score, 1.0)

# === Enhanced Markdown Generation ===
def issue_to_enhanced_markdown(issue_data: Dict) -> str:
    """Generate enhanced markdown with AI content"""
    
    md = f"""# {issue_data['key']} - {issue_data['summary']}

**Status**: {issue_data['status']}  
**Type**: {issue_data['type']}  
**Priority**: {issue_data['priority']}  
**Resolution**: {issue_data['resolution']}  
**Assignee**: {issue_data['assignee']}  

## Original Description
{issue_data['description']}

"""
    
    # Add AI analysis if available
    ai_analysis = issue_data.get("ai_analysis", {})
    if ai_analysis:
        md += f"""## AI-Generated Release Notes Content

**Category**: {ai_analysis.get('category', 'Unknown')}  
**Confidence**: {ai_analysis.get('confidence', 0):.2f}  

### Symptom
{ai_analysis.get('symptom', 'Not generated')}  

### Condition  
{ai_analysis.get('condition', 'Not generated')}  

### Release Notes Quality Check
- Symptom ≠ Condition: {'✓' if ai_analysis.get('symptom') != ai_analysis.get('condition') else '✗'}
- Has Workaround Info: {'✓' if 'workaround' in issue_data['description'].lower() else '✗'}
- Customer Impact: {issue_data['priority']}

"""
    
    md += f"""## Metadata
- **Created**: {issue_data['created']}
- **Updated**: {issue_data['updated']}
- **Key**: {issue_data['key']}
- **Direct Link**: {os.environ['JIRA_SERVER']}/browse/{issue_data['key']}
"""
    
    return md

# === Local File Management ===
def save_raw_data_backup(query_tag: str, issues: List) -> str:
    """Save raw Jira data as JSON backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_FOLDER, f"{query_tag}_{timestamp}.json")
    
    # Convert issues to serializable format
    backup_data = []
    for issue in issues:
        backup_data.append({
            "key": issue.key,
            "raw": issue.raw,
            "fields": {
                "summary": issue.fields.summary,
                "description": issue.fields.description,
                "status": issue.fields.status.name,
                "priority": getattr(issue.fields.priority, 'name', None),
                "resolution": getattr(issue.fields.resolution, 'name', None),
                "issuetype": issue.fields.issuetype.name,
                "created": str(issue.fields.created),
                "updated": str(issue.fields.updated)
            }
        })
    
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(backup_data, f, indent=2, default=str)
    
    return backup_file

def generate_summary_report(all_results: Dict) -> str:
    """Generate a summary report of all processing"""
    
    report = f"""# Jira Documentation Processing Summary
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Processing Overview
"""
    
    total_issues = 0
    ai_processed = 0
    
    for query_tag, results in all_results.items():
        count = len(results)
        ai_count = sum(1 for r in results if r.get("ai_analysis", {}).get("symptom"))
        total_issues += count
        ai_processed += ai_count
        
        report += f"""
### {query_tag.replace('_', ' ').title()}
- **Issues Found**: {count}
- **AI Processed**: {ai_count}
- **Success Rate**: {(ai_count/count*100) if count > 0 else 0:.1f}%
"""
    
    report += f"""
## Overall Statistics
- **Total Issues**: {total_issues}
- **AI Processing Success**: {ai_processed}/{total_issues} ({(ai_processed/total_issues*100) if total_issues > 0 else 0:.1f}%)
- **Average Confidence**: {sum(r.get('ai_analysis', {}).get('confidence', 0) for results in all_results.values() for r in results if r.get('ai_analysis', {}).get('confidence')) / max(ai_processed, 1):.2f}

## Quality Metrics
"""
    
    # Quality analysis
    symptom_condition_different = 0
    high_confidence = 0
    
    for results in all_results.values():
        for result in results:
            ai = result.get("ai_analysis", {})
            if ai.get("symptom") and ai.get("condition"):
                if ai["symptom"] != ai["condition"]:
                    symptom_condition_different += 1
                if ai.get("confidence", 0) > 0.7:
                    high_confidence += 1
    
    report += f"""
- **Symptom ≠ Condition**: {symptom_condition_different}/{ai_processed} ({(symptom_condition_different/max(ai_processed,1)*100):.1f}%)
- **High Confidence (>0.7)**: {high_confidence}/{ai_processed} ({(high_confidence/max(ai_processed,1)*100):.1f}%)

## Next Steps for Plugin Development
1. Review generated content in `{OUTPUT_FOLDER}/`
2. Check quality of AI categorization
3. Validate JQL queries against your requirements
4. Test with different issue types and priorities

## Files Generated
"""
    
    for query_tag in all_results.keys():
        report += f"- `{OUTPUT_FOLDER}/{query_tag}/` - Individual issue markdown files\n"
    
    report += f"- `{BACKUP_FOLDER}/` - Raw JSON backups\n"
    report += f"- `{OUTPUT_FOLDER}/processing_summary.json` - Detailed results\n"
    
    return report

# === Main Processing Loop ===
def main():
    """Enhanced main function with local processing"""
    
    print(f"{'='*60}")
    print("JIRA DOCUMENTATION INTELLIGENCE - LOCAL TESTING")
    print(f"{'='*60}")
    print(f"Output folder: {OUTPUT_FOLDER}")
    print(f"Backup folder: {BACKUP_FOLDER}")
    print(f"OpenAI enabled: {'Yes' if OPENAI_API_KEY else 'No'}")
    print(f"{'='*60}")
    
    all_results = {}
    
    for tag, jql in queries.items():
        print(f"\n{'='*50}")
        print(f"Query: {tag}")
        print(f"JQL: {jql[:100]}{'...' if len(jql) > 100 else ''}")
        print(f"{'='*50}")
        
        # Create directory for each query
        query_folder = os.path.join(OUTPUT_FOLDER, tag)
        os.makedirs(query_folder, exist_ok=True)
        
        try:
            # Fetch issues
            print("Fetching issues from Jira...")
            issues = jira.search_issues(jql, maxResults=20, fields="*all")
            print(f"Found {len(issues)} issues")
            
            if issues:
                # Save raw backup
                backup_file = save_raw_data_backup(tag, issues)
                print(f"Raw data backed up to: {backup_file}")
                
                query_results = []
                
                for i, issue in enumerate(issues, 1):
                    print(f"Processing {i}/{len(issues)}: {issue.key}")
                    
                    # Process with AI (your future plugin logic)
                    issue_data = process_issue_with_ai(issue)
                    query_results.append(issue_data)
                    
                    # Generate enhanced markdown
                    markdown_content = issue_to_enhanced_markdown(issue_data)
                    
                    # Save locally
                    filename = f"{issue.key}.md"
                    local_path = os.path.join(query_folder, filename)
                    with open(local_path, "w", encoding="utf-8") as f:
                        f.write(markdown_content)
                    
                    print(f"  ✓ Saved: {filename}")
                
                all_results[tag] = query_results
                print(f"✓ Completed {tag}: {len(query_results)} issues processed")
            else:
                print("No issues found for this query")
                all_results[tag] = []
                
        except Exception as e:
            print(f"✗ Error processing {tag}: {e}")
            all_results[tag] = []
    
    # Save summary results
    summary_path = os.path.join(OUTPUT_FOLDER, "processing_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, default=str)
    
    # Generate and save summary report
    summary_report = generate_summary_report(all_results)
    report_path = os.path.join(OUTPUT_FOLDER, "SUMMARY_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(summary_report)
    
    print(f"\n{'='*60}")
    print("🎉 PROCESSING COMPLETE!")
    print(f"{'='*60}")
    print(f"📁 Results: {OUTPUT_FOLDER}/")
    print(f"📄 Summary: {report_path}")
    print(f"💾 Backups: {BACKUP_FOLDER}/")
    print(f"📊 Total Issues: {sum(len(results) for results in all_results.values())}")
    print(f"🤖 AI Processing: {'Enabled' if OPENAI_API_KEY else 'Disabled (add OPENAI_API_KEY)'}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
```

## Updated requirements.txt

txt

```txt
jira==3.5.0
openai==1.3.0
python-dotenv==1.0.0
requests==2.31.0
```

## Updated .env file

bash

```bash
# Your existing Jira config
JIRA_SERVER=https://your-company.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_PAT=your_api_token

# Add OpenAI for AI processing (optional)
OPENAI_API_KEY=your_openai_api_key

# Remove AWS variables (not needed for local)
# AWS_ACCESS_KEY_ID=...
# AWS_SECRET_ACCESS_KEY=...
```

## Local Folder Structure After Running

```
your-project/
├── main.py
├── requirements.txt
├── .env
├── jira_md_output/           # All generated content
│   ├── extreme_defects_with_code_changes/
│   │   ├── XCP-1234.md
│   │   └── XCP-5678.md
│   ├── defects_cwc_test/
│   ├── open_defects_test/
│   ├── processing_summary.json
│   └── SUMMARY_REPORT.md     # Overview of everything
├── jira_backups/             # Raw JSON backups
│   ├── extreme_defects_20241215_143022.json
│   └── defects_cwc_test_20241215_143045.json
```

## Quick Start

bash

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your Jira credentials

# Run processing
python main.py

# Check results
ls jira_md_output/
cat jira_md_output/SUMMARY_REPORT.md
```

## What You Get Locally

✅ **All Jira Data**: Downloaded and processed locally  
✅ **AI Analysis**: If OpenAI key provided, enhanced content generation  
✅ **Markdown Files**: Individual files for each issue  
✅ **JSON Backups**: Raw Jira data preserved  
✅ **Summary Report**: Overall processing statistics  
✅ **Quality Metrics**: Validation of AI-generated content  
✅ **No AWS Dependency**: Everything stored locally

This gives you the same capabilities as the AWS version but keeps everything on your local machine for development and testing!

Retry

K

Where / how do I focus on the Jira plugin wrapper component next

Edit

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

bash

```bash
# Install Forge CLI
npm install -g @forge/cli

# Login to Atlassian
forge login

# Verify installation
forge --version
```

### **Create Your Plugin Project**

bash

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

javascript

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

jsx

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

yaml

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

bash

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

javascript

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

bash

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

Retry

K

On sign up - there were a number of other project related management things (marketing etc) - at least 10 - how would their Jira's be configured differently for those types of projects?

Edit

# Jira Configuration Differences by Project Type

You're absolutely right - different project types have vastly different Jira configurations. Here's how they typically differ and how it impacts your documentation plugin:

## **Common Atlassian Project Templates**

### **1. Software Development (Your Current Focus)**

yaml

```yaml
Issue Types: Epic, Story, Task, Bug, Subtask
Workflows: To Do → In Progress → Code Review → Testing → Done
Custom Fields: Story Points, Sprint, Fix Version, Components
Documentation Focus: Release notes, API docs, technical specifications
```

### **2. Marketing Campaign Management**

yaml

```yaml
Issue Types: Campaign, Creative Asset, Blog Post, Social Media Post, Email
Workflows: Ideation → Planning → Creation → Review → Approval → Published
Custom Fields: Target Audience, Channel, Budget, Launch Date, Campaign Type
Documentation Focus: Campaign briefs, performance reports, content calendars
```

### **3. Product Management**

yaml

```yaml
Issue Types: Initiative, Feature, User Story, Market Research, Competitive Analysis
Workflows: Backlog → Prioritized → In Development → Testing → Released
Custom Fields: Business Value, Customer Segment, Revenue Impact, OKR Alignment
Documentation Focus: PRDs, roadmaps, feature specifications, market analysis
```

### **4. IT Service Management (ITSM)**

yaml

```yaml
Issue Types: Incident, Service Request, Problem, Change Request, Knowledge Article
Workflows: Open → Assigned → In Progress → Resolved → Closed
Custom Fields: SLA, Priority Matrix, Affected Services, Resolution Category
Documentation Focus: Runbooks, incident reports, change documentation, KB articles
```

### **5. HR/People Operations**

yaml

```yaml
Issue Types: Hiring Request, Onboarding Task, Performance Review, Policy Update
Workflows: Requested → Approved → In Progress → Completed → Archived
Custom Fields: Department, Role Level, Hiring Manager, Start Date, Budget Code
Documentation Focus: Job descriptions, policy documents, process guides, org charts
```

### **6. Legal/Compliance**

yaml

```yaml
Issue Types: Contract Review, Legal Request, Compliance Check, Risk Assessment
Workflows: Submitted → Under Review → Legal Review → Approved → Implemented
Custom Fields: Risk Level, Compliance Framework, Stakeholder, Due Date, Cost Center
Documentation Focus: Legal briefs, compliance reports, contract summaries, risk assessments
```

### **7. Finance/Procurement**

yaml

```yaml
Issue Types: Purchase Request, Invoice Processing, Budget Planning, Vendor Evaluation
Workflows: Requested → Budget Check → Approval → Procurement → Received → Paid
Custom Fields: Cost Center, Vendor, Amount, Approval Level, GL Account
Documentation Focus: Financial reports, vendor evaluations, budget summaries, audit trails
```

### **8. Content/Creative**

yaml

```yaml
Issue Types: Article, Video, Design Asset, Review, Publication
Workflows: Concept → Draft → Review → Revisions → Approval → Published
Custom Fields: Content Type, Target Audience, Publication Date, Brand Guidelines
Documentation Focus: Content briefs, brand guidelines, publication schedules, performance metrics
```

### **9. Operations/Facilities**

yaml

```yaml
Issue Types: Maintenance Request, Equipment Purchase, Space Planning, Vendor Management
Workflows: Requested → Assessed → Scheduled → In Progress → Completed → Verified
Custom Fields: Location, Equipment Type, Priority Level, Vendor, Cost
Documentation Focus: Maintenance logs, equipment manuals, vendor contracts, operational procedures
```

### **10. Sales/Customer Success**

yaml

```yaml
Issue Types: Lead, Opportunity, Customer Issue, Renewal, Upsell
Workflows: Qualified → Proposal → Negotiation → Closed Won/Lost
Custom Fields: Deal Size, Sales Stage, Account Owner, Close Date, Customer Segment
Documentation Focus: Sales playbooks, customer communications, deal summaries, renewal reports
```

## **How This Impacts Your Documentation Plugin**

### **1. Field Mapping Strategy**

python

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

python

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

python

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

python

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

javascript

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

python

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

Retry

K

Are these all the types of audiences they typically market to? What's the user base and TAM in each?

Edit

# Atlassian's Market Segmentation & TAM Analysis

You're asking a great strategic question. Atlassian targets a much broader market than just these project types. Let me break down their actual market segmentation and TAM:

## **Atlassian's Primary Market Segments**

### **1. Software Development Teams (Core Market)**

yaml

```yaml
TAM: ~$50B (Global DevOps/ALM market)
User Base: ~200M software developers globally
Atlassian Share: ~20M+ users (Jira Software, Confluence, Bitbucket)
Key Products: Jira Software, Confluence, Bitbucket, Bamboo
Growth Rate: 15-20% annually
Revenue per User: $50-200/user/year
```

### **2. IT Service Management (ITSM)**

yaml

```yaml
TAM: ~$15B (ITSM software market)
User Base: ~50M IT professionals globally
Atlassian Share: ~5M users (Jira Service Management)
Key Products: Jira Service Management, Opsgenie
Growth Rate: 25-30% annually
Revenue per User: $20-100/user/year
```

### **3. Business Teams (Fastest Growing)**

yaml

```yaml
TAM: ~$30B (Work management/collaboration)
User Base: ~500M knowledge workers globally
Atlassian Share: ~10M users (expanding rapidly)
Key Products: Jira Work Management, Confluence, Trello
Growth Rate: 40-50% annually
Revenue per User: $10-50/user/year
```

## **Detailed Market Breakdown**

### **Software Development (Established Market)**

**Industries:**

- Technology companies (SaaS, hardware, mobile)
- Financial services (fintech, banks)
- Healthcare tech
- Gaming
- E-commerce

**User Personas:**

- Software engineers (200M globally)
- DevOps engineers (50M globally)
- Product managers (10M globally)
- QA engineers (30M globally)

**Market Maturity:** Saturated in enterprise, growing in SMB **Competitive Landscape:** GitHub, Azure DevOps, GitLab, Linear

### **ITSM (Growing Market)**

**Industries:**

- Enterprise IT departments
- Managed service providers
- Government agencies
- Healthcare systems
- Educational institutions

**User Personas:**

- IT administrators (20M globally)
- Help desk agents (15M globally)
- Infrastructure engineers (10M globally)
- Security teams (5M globally)

**Market Maturity:** Moderate penetration, disrupting ServiceNow **Competitive Landscape:** ServiceNow, Remedy, Cherwell

### **Business Teams (Explosive Growth)**

**Industries & Functions:**

- **Marketing Teams**: 50M marketing professionals globally
- **HR/People Ops**: 30M HR professionals globally
- **Legal/Compliance**: 10M legal professionals globally
- **Finance/Operations**: 100M business operations roles
- **Sales Operations**: 20M sales professionals globally
- **Project Management**: 50M project managers globally

**Market Maturity:** Early adoption, massive greenfield opportunity **Competitive Landscape:** Monday.com, Asana, Smartsheet, Airtable

## **Regional TAM Distribution**

### **North America: ~40% of Global TAM**

yaml

```yaml
Software Dev: $20B TAM, 80M developers
ITSM: $6B TAM, 20M IT professionals  
Business Teams: $12B TAM, 200M knowledge workers
Atlassian Penetration: High in software, medium in ITSM, low in business
```

### **Europe: ~30% of Global TAM**

yaml

```yaml
Software Dev: $15B TAM, 60M developers
ITSM: $4.5B TAM, 15M IT professionals
Business Teams: $9B TAM, 150M knowledge workers
Atlassian Penetration: Medium across all segments
```

### **Asia-Pacific: ~25% of Global TAM**

yaml

```yaml
Software Dev: $12.5B TAM, 50M developers
ITSM: $3.75B TAM, 12M IT professionals
Business Teams: $7.5B TAM, 120M knowledge workers
Atlassian Penetration: Growing rapidly, especially in software
```

### **Rest of World: ~5% of Global TAM**

yaml

```yaml
Combined: $4.75B TAM
Atlassian Penetration: Early stage, high growth potential
```

## **Company Size Segmentation**

### **Enterprise (10,000+ employees)**

yaml

```yaml
Market Size: ~50,000 companies globally
Average Atlassian Spend: $100,000-1M+ annually
Total TAM: ~$20B
Current Penetration: ~30% (software), ~15% (ITSM), ~5% (business)
Key Challenge: Competing with Microsoft, ServiceNow
```

### **Mid-Market (500-10,000 employees)**

yaml

```yaml
Market Size: ~200,000 companies globally  
Average Atlassian Spend: $10,000-100,000 annually
Total TAM: ~$40B
Current Penetration: ~50% (software), ~25% (ITSM), ~10% (business)
Key Opportunity: Highest growth segment
```

### **SMB (10-500 employees)**

yaml

```yaml
Market Size: ~5M companies globally
Average Atlassian Spend: $500-10,000 annually
Total TAM: ~$35B
Current Penetration: ~20% (software), ~10% (ITSM), ~5% (business)
Key Challenge: Price sensitivity, simpler needs
```

## **Industry Vertical Breakdown**

### **Technology Sector (Core Strength)**

yaml

```yaml
TAM: $25B
Companies: ~500K globally
Atlassian Penetration: ~60%
Growth Rate: 15% annually
```

### **Financial Services**

yaml

```yaml
TAM: $15B  
Companies: ~200K globally
Atlassian Penetration: ~30%
Growth Rate: 20% annually
Key Players: Banks, fintech, insurance
```

### **Healthcare**

yaml

```yaml
TAM: $10B
Companies: ~150K globally  
Atlassian Penetration: ~15%
Growth Rate: 25% annually
Key Players: Hospitals, pharma, medtech
```

### **Government/Public Sector**

yaml

```yaml
TAM: $8B
Organizations: ~100K globally
Atlassian Penetration: ~20%
Growth Rate: 10% annually
Key Challenge: Security, compliance requirements
```

### **Manufacturing**

yaml

```yaml
TAM: $12B
Companies: ~300K globally
Atlassian Penetration: ~10%
Growth Rate: 30% annually
Key Opportunity: Digital transformation
```

## **Strategic Implications for Your Plugin**

### **Highest Value Segments:**

1. **Software Development** - Proven market, highest ARPU
2. **Mid-Market Business Teams** - Fastest growth, lower competition
3. **ITSM in Financial Services** - High compliance needs, good margins

### **Plugin Market Opportunity:**

yaml

```yaml
Total Addressable Market for Documentation AI:
- Software Teams: $2B (10% of dev market)
- ITSM Teams: $750M (5% of ITSM market)  
- Business Teams: $1.5B (5% of business market)
- Total Plugin TAM: ~$4.25B

Serviceable Addressable Market (SAM):
- Atlassian's current user base: ~35M users
- Documentation-heavy users: ~70% = 25M users
- Willing to pay for AI enhancement: ~20% = 5M users
- Average additional spend: $10-50/user/year
- Total SAM: $50M-250M annually
```

### **Go-to-Market Strategy:**

1. **Start with Software Development** (highest willingness to pay for AI)
2. **Expand to ITSM** (clear ROI on incident documentation)
3. **Target Mid-Market** (less competition, faster decisions)
4. **Geographic expansion** (North America → Europe → APAC)

The business team segment represents Atlassian's biggest growth opportunity and your plugin's highest potential market expansion beyond traditional software development use cases.

Retry

K

How could I easily bulk import a Jira? Give me 3 samples of what would go in a Jira with acceptance criteria etc

Edit

# Bulk Import Jira Issues - 3 Methods + Sample Data

## **Method 1: CSV Import (Easiest)**

### **Step-by-Step Process:**

1. **Go to Jira → Issues → Import Issues from CSV**
2. **Upload your CSV file**
3. **Map columns to Jira fields**
4. **Preview and import**

### **CSV Template Structure:**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Components,Epic Link,Story Points,Acceptance Criteria,Original Estimate,Status,Reporter
```

## **Sample Data for 3 Different Use Cases**

### **Sample 1: E-commerce Platform Development**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Components,Epic Link,Story Points,Acceptance Criteria,Original Estimate,Status,Reporter
Epic,User Account Management System,Implement comprehensive user account management including registration signup login and profile management,High,john.doe@company.com,user-management,Frontend,EP-001,,Create secure user registration and authentication system with profile management capabilities,40h,To Do,product.manager@company.com
Story,User Registration Form,Create user registration form with email verification,High,jane.smith@company.com,frontend user-auth,Frontend,EP-001,5,"GIVEN a new user visits the registration page
WHEN they fill out the form with valid information
THEN they should receive a verification email
AND their account should be created in pending status

GIVEN a user enters invalid email format
WHEN they submit the form
THEN they should see an error message

GIVEN a user tries to register with existing email
WHEN they submit the form
THEN they should see ""Email already exists"" error",8h,In Progress,john.doe@company.com
Story,Email Verification System,Implement email verification workflow for new user accounts,Medium,mike.wilson@company.com,backend user-auth email,Backend,EP-001,3,"GIVEN a user registers with valid email
WHEN they click the verification link in email
THEN their account status should change to active
AND they should be redirected to login page

GIVEN a verification link is older than 24 hours
WHEN user clicks the link
THEN they should see ""Link expired"" message
AND option to resend verification email",6h,To Do,john.doe@company.com
Bug,Login form not responsive on mobile,Login form elements overlap on mobile devices below 768px width,High,jane.smith@company.com,bug mobile-responsive,Frontend,EP-001,2,"GIVEN a user accesses login page on mobile device
WHEN screen width is below 768px
THEN form elements should stack vertically
AND all text should remain readable
AND buttons should be properly sized for touch

GIVEN a user tries to login on mobile
WHEN they tap input fields
THEN keyboard should not obscure the form
AND zoom should not be triggered",4h,Open,user.support@company.com
Task,Set up authentication database tables,Create user authentication related database schema and tables,Medium,mike.wilson@company.com,backend database setup,Backend,EP-001,2,"GIVEN database setup is complete
WHEN authentication system queries database
THEN all user data should be stored securely
AND passwords should be properly hashed
AND user sessions should be trackable

GIVEN database migration runs
WHEN existing data exists
THEN migration should complete without data loss",3h,Done,john.doe@company.com
```

### **Sample 2: Marketing Campaign Management**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Components,Epic Link,Story Points,Acceptance Criteria,Original Estimate,Status,Reporter
Epic,Q1 Product Launch Campaign,Comprehensive marketing campaign for new product launch including content creation social media and email marketing,High,marketing.lead@company.com,q1-launch product-marketing,Marketing,MC-001,,Execute multi-channel marketing campaign to drive product awareness and generate 1000 qualified leads,120h,In Progress,cmo@company.com
Story,Create Product Launch Landing Page,Design and develop dedicated landing page for product launch with conversion tracking,High,web.designer@company.com,landing-page conversion-tracking,Website,MC-001,8,"GIVEN a user visits the product launch URL
WHEN they scroll through the page
THEN they should see product benefits features and pricing
AND call-to-action buttons should be prominently displayed

GIVEN a user clicks ""Sign Up"" button
WHEN they complete the form
THEN their information should be captured in CRM
AND they should receive welcome email sequence

GIVEN page analytics are reviewed
WHEN campaign is active
THEN conversion rate should be tracked
AND A/B testing should be enabled for key elements",16h,In Progress,marketing.lead@company.com
Story,Email Marketing Sequence,Create automated email sequence for product launch nurturing leads through sales funnel,Medium,content.writer@company.com,email-marketing automation,Email Platform,MC-001,5,"GIVEN a user signs up for product updates
WHEN they enter email address
THEN they should receive welcome email within 5 minutes
AND be added to appropriate email list

GIVEN email sequence is active
WHEN user opens emails
THEN open rates should be tracked
AND click-through rates should be measured

GIVEN user clicks product links in email
WHEN they visit landing page
THEN their behavior should be tracked
AND sales team should be notified of hot leads",12h,To Do,marketing.lead@company.com
Task,Social Media Content Calendar,Develop 30-day social media content calendar with posts graphics and engagement strategy,Medium,social.manager@company.com,social-media content-planning,Social Media,MC-001,3,"GIVEN content calendar is created
WHEN posts are scheduled
THEN content should align with launch timeline
AND include variety of post types (educational promotional behind-scenes)

GIVEN posts are published
WHEN audience engages
THEN engagement metrics should be tracked
AND responses should be managed within 2 hours

GIVEN campaign period ends
WHEN performance is analyzed
THEN ROI should be calculated
AND insights should inform future campaigns",8h,To Do,marketing.lead@company.com
Bug,Email template rendering incorrectly in Outlook,Product announcement email template displays broken formatting in Microsoft Outlook clients,High,email.developer@company.com,bug email-template outlook,Email Platform,MC-001,1,"GIVEN email template is sent to Outlook users
WHEN they open the email
THEN formatting should display correctly
AND images should load properly
AND call-to-action buttons should be clickable

GIVEN template is tested across email clients
WHEN rendering is verified
THEN template should work in Outlook 2016 2019 and 365
AND mobile Outlook app should display correctly",4h,Open,social.manager@company.com
```

### **Sample 3: IT Service Management**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Components,Epic Link,Story Points,Acceptance Criteria,Original Estimate,Status,Reporter
Epic,Office Network Infrastructure Upgrade,Upgrade office network infrastructure to support remote work and increased bandwidth requirements,Critical,network.admin@company.com,infrastructure network-upgrade,IT Infrastructure,IT-001,,Upgrade network to support 500+ concurrent users with 99.9% uptime and improved security,200h,In Progress,it.manager@company.com
Incident,VPN connection timeouts for remote users,Multiple remote users reporting VPN connection drops and timeouts affecting productivity,Critical,network.admin@company.com,incident vpn remote-work,Network,IT-001,,"GIVEN incident is resolved
WHEN remote users connect to VPN
THEN connections should remain stable for 8+ hours
AND connection speed should meet minimum requirements

GIVEN monitoring is in place
WHEN VPN issues occur
THEN alerts should be sent to IT team within 5 minutes
AND automatic diagnostics should run

GIVEN post-incident review is complete
WHEN similar issues are detected
THEN preventive measures should activate
AND users should be proactively notified",8h,In Progress,remote.user@company.com
Service Request,Install new firewall appliance,Install and configure next-generation firewall to replace aging security appliance,High,security.admin@company.com,service-request firewall security,Security,IT-001,,"GIVEN firewall installation is complete
WHEN network traffic flows through device
THEN security policies should be properly enforced
AND network performance should not degrade

GIVEN firewall rules are configured
WHEN unauthorized access is attempted
THEN threats should be blocked and logged
AND security team should be alerted

GIVEN firewall is operational
WHEN monthly security review occurs
THEN threat reports should be generated
AND compliance requirements should be met",24h,To Do,it.manager@company.com
Problem,Recurring email server performance issues,Email server experiences periodic slowdowns causing delayed message delivery,Medium,email.admin@company.com,problem email-server performance,Email System,IT-001,,"GIVEN root cause analysis is complete
WHEN email server performance is optimized
THEN message delivery should occur within 30 seconds
AND server response time should be under 2 seconds

GIVEN monitoring solution is implemented
WHEN performance issues begin
THEN proactive alerts should be sent
AND automatic scaling should occur if possible

GIVEN problem is resolved
WHEN email volume increases
THEN server should handle peak loads
AND performance metrics should remain stable",16h,In Progress,multiple.users@company.com
Change Request,Migrate file server to cloud storage,Migrate on-premises file server to cloud-based storage solution for better accessibility,Medium,cloud.admin@company.com,change-request cloud-migration file-server,Cloud Services,IT-001,,"GIVEN migration plan is approved
WHEN file migration begins
THEN no data should be lost during transfer
AND user access should be maintained

GIVEN cloud storage is active
WHEN users access files
THEN performance should equal or exceed current system
AND file permissions should be preserved

GIVEN migration is complete
WHEN disaster recovery is tested
THEN cloud backup should restore successfully
AND RTO should meet business requirements",40h,To Do,it.manager@company.com
Knowledge Article,VPN Setup Guide for Remote Workers,Create comprehensive guide for setting up VPN access on various devices and operating systems,Low,documentation.specialist@company.com,knowledge-article vpn setup-guide,Documentation,IT-001,,"GIVEN setup guide is published
WHEN users follow the instructions
THEN VPN should be configured successfully on first attempt
AND guide should cover Windows Mac iOS and Android

GIVEN guide is accessed by users
WHEN they encounter issues
THEN troubleshooting section should resolve common problems
AND contact information should be provided for escalation

GIVEN guide is in use
WHEN feedback is collected
THEN user satisfaction should be 90%+
AND guide should be updated based on feedback",6h,To Do,it.manager@company.com
```

## **Method 2: Jira REST API (Programmatic)**

### **Python Script for Bulk Import:**

python

```python
import requests
import json
from requests.auth import HTTPBasicAuth

# Your Jira configuration
JIRA_URL = "https://your-domain.atlassian.net"
USERNAME = "your-email@company.com"  
API_TOKEN = "your-api-token"
PROJECT_KEY = "TEST"

# Sample issue data
issues_data = [
    {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": "User Registration Form",
            "description": "Create user registration form with email verification",
            "issuetype": {"name": "Story"},
            "priority": {"name": "High"},
            "assignee": {"accountId": "user-account-id"},
            "labels": ["frontend", "user-auth"],
            "customfield_10016": 5,  # Story Points
            "customfield_10017": "GIVEN a new user visits the registration page\nWHEN they fill out the form with valid information\nTHEN they should receive a verification email"  # Acceptance Criteria
        }
    },
    # Add more issues here...
]

# Function to create issues
def bulk_create_issues(issues_data):
    url = f"{JIRA_URL}/rest/api/3/issue/bulk"
    
    payload = {
        "issueUpdates": [{"fields": issue["fields"]} for issue in issues_data]
    }
    
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(USERNAME, API_TOKEN)
    )
    
    if response.status_code == 201:
        print("Issues created successfully!")
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Run the import
result = bulk_create_issues(issues_data)
```

## **Method 3: Third-Party Tools**

### **Recommended Tools:**

1. **CSV Importer for Jira (Atlassian Marketplace)**
    - Advanced field mapping
    - Validation before import
    - Bulk operations support
2. **ScriptRunner (Advanced)**
    - Custom import scripts
    - Data transformation
    - Automated workflows
3. **Jira Excel Plugin**
    - Direct Excel import
    - Template-based imports
    - Field validation

## **Key Tips for Successful Bulk Import:**

### **Data Preparation:**

yaml

```yaml
Required Fields:
  - Issue Type (must exist in project)
  - Summary (required)
  - Project Key (must have permission)

Optional but Recommended:
  - Description
  - Priority
  - Assignee (must be valid user)
  - Labels
  - Custom Fields (Story Points, etc.)
```

### **Common Pitfalls to Avoid:**

1. **Invalid user accounts** in Assignee field
2. **Non-existent issue types** for the project
3. **Custom field IDs** vs names (use names in CSV)
4. **Date formats** - use ISO format (YYYY-MM-DD)
5. **Large descriptions** - may hit character limits

### **Validation Before Import:**

1. Test with 5-10 issues first
2. Verify all users exist and have project access
3. Check custom field configurations
4. Validate issue type workflows

This approach gives you realistic, detailed sample data that demonstrates how different project types use Jira differently, which is crucial for your documentation plugin to handle various use cases effectively.

Retry

K

I just save 3 examples out into VSC as csv

But would it really work with all this in there? is there a table format thats easier for me to confirm formatting by pasting into excel first?

I also did map all the fields to other fields after uploading the file except for Summary which was required (was I supposed to do this first?)

WHEN they fill out the form with valid information THEN they should receive a verification email AND their account should be created in pending status GIVEN a user enters invalid email format WHEN they submit the form THEN they should see an error message GIVEN a user tries to register with existing email WHEN they submit the form THEN they should see ""Email already exists"" error",8h,In Progress,john.doe@company.com Story,Email Ve

Edit

You're absolutely right to be concerned! Let me give you properly formatted, Excel-friendly CSV data that will actually work.

# Simplified CSV Format for Easy Import

## **Issues with the Previous Format:**

1. **Multi-line acceptance criteria** break CSV parsing
2. **Commas within fields** break column alignment
3. **Too many columns** make it hard to validate
4. **Field mapping order** - you can map after upload, that's correct!

## **Simplified CSV Templates**

### **Template 1: Basic Software Issues**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Story Points,Status
Epic,User Account Management System,Implement comprehensive user account management system,High,john.doe@company.com,user-management,,To Do
Story,User Registration Form,Create user registration form with email verification,High,jane.smith@company.com,frontend;user-auth,5,In Progress
Story,Email Verification System,Implement email verification workflow for new accounts,Medium,mike.wilson@company.com,backend;email,3,To Do
Bug,Login form not responsive on mobile,Login form elements overlap on mobile devices below 768px,High,jane.smith@company.com,bug;mobile,2,Open
Task,Set up authentication database,Create user authentication database schema,Medium,mike.wilson@company.com,backend;database,2,Done
Story,Password Reset Functionality,Allow users to reset passwords via email,Medium,jane.smith@company.com,frontend;security,3,To Do
Bug,Session timeout too aggressive,Users getting logged out every 15 minutes,Low,mike.wilson@company.com,bug;session,1,Open
Story,User Profile Management,Enable users to update profile information,Low,jane.smith@company.com,frontend;profile,4,To Do
Task,API Documentation for Auth,Document authentication API endpoints,Low,john.doe@company.com,documentation;api,1,To Do
Story,Two-Factor Authentication,Implement 2FA using SMS or authenticator app,High,mike.wilson@company.com,security;2fa,8,To Do
```

### **Template 2: Marketing Campaign Issues**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Story Points,Status
Epic,Q1 Product Launch Campaign,Multi-channel marketing campaign for product launch,High,marketing.lead@company.com,q1-launch,,In Progress
Story,Create Landing Page,Design and build product launch landing page,High,web.designer@company.com,landing-page;design,8,In Progress
Story,Email Marketing Sequence,Create automated email nurture sequence,Medium,content.writer@company.com,email;automation,5,To Do
Task,Social Media Content Calendar,Develop 30-day social content calendar,Medium,social.manager@company.com,social;content,3,To Do
Bug,Email template broken in Outlook,Product email displays incorrectly in Outlook,High,email.developer@company.com,bug;email,1,Open
Story,Google Ads Campaign Setup,Create and launch Google Ads for product,High,ads.specialist@company.com,ads;google,5,To Do
Task,Competitor Analysis Report,Research competitor marketing strategies,Low,marketing.analyst@company.com,research;analysis,2,To Do
Story,Influencer Outreach Program,Identify and contact relevant influencers,Medium,partnerships.manager@company.com,influencer;outreach,4,To Do
Bug,Landing page slow on mobile,Page load time over 5 seconds on mobile,Medium,web.developer@company.com,bug;performance,2,Open
Story,Launch Event Planning,Plan virtual launch event and webinar,High,events.coordinator@company.com,event;webinar,6,To Do
```

### **Template 3: IT Service Management**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels,Story Points,Status
Epic,Network Infrastructure Upgrade,Upgrade office network for remote work support,Critical,network.admin@company.com,infrastructure,,In Progress
Incident,VPN connection timeouts,Remote users experiencing VPN disconnections,Critical,network.admin@company.com,incident;vpn,,In Progress
Service Request,Install new firewall,Install next-generation firewall appliance,High,security.admin@company.com,firewall;security,,To Do
Problem,Email server slow performance,Recurring email delivery delays,Medium,email.admin@company.com,email;performance,,In Progress
Change Request,Migrate to cloud storage,Move file server to cloud-based solution,Medium,cloud.admin@company.com,cloud;migration,,To Do
Knowledge Article,VPN Setup Guide,Create VPN configuration guide for users,Low,documentation.specialist@company.com,documentation;vpn,,To Do
Incident,Printer network connectivity,Office printers not connecting to network,Medium,desktop.support@company.com,printer;network,,Open
Service Request,New employee laptop setup,Configure laptop for new marketing hire,High,desktop.support@company.com,laptop;onboarding,,To Do
Problem,WiFi dead zones in office,Weak WiFi signal in conference rooms,Low,network.admin@company.com,wifi;coverage,,To Do
Change Request,Update antivirus software,Deploy new antivirus across all computers,High,security.admin@company.com,antivirus;security,,To Do
```

## **Excel-Friendly Format Check**

### **Paste this into Excel to verify formatting:**

|Issue Type|Summary|Description|Priority|Assignee|Labels|Story Points|Status|
|---|---|---|---|---|---|---|---|
|Epic|User Account Management|Implement user account system|High|[john.doe@company.com](mailto:john.doe@company.com)|user-management||To Do|
|Story|User Registration Form|Create registration form|High|[jane.smith@company.com](mailto:jane.smith@company.com)|frontend;user-auth|5|In Progress|
|Bug|Login form not responsive|Mobile display issues|High|[jane.smith@company.com](mailto:jane.smith@company.com)|bug;mobile|2|Open|

## **Jira Import Process (Correct Order)**

### **Step 1: Upload CSV File**

1. Go to **Issues → Import Issues from CSV**
2. **Upload your CSV file**
3. **Don't worry about field mapping yet**

### **Step 2: Field Mapping (After Upload)**

yaml

```yaml
Map These Fields:
  Column 1 "Issue Type" → Issue Type
  Column 2 "Summary" → Summary (Required)
  Column 3 "Description" → Description  
  Column 4 "Priority" → Priority
  Column 5 "Assignee" → Assignee
  Column 6 "Labels" → Labels
  Column 7 "Story Points" → Story Points (if available)
  Column 8 "Status" → Status
```

### **Step 3: Preview and Import**

- **Review the preview**
- **Check for validation errors**
- **Import in small batches** (10-20 issues first)

## **Pro Tips for CSV Success**

### **Data Formatting Rules:**

yaml

```yaml
Text Fields:
  - No commas in descriptions (use semicolons)
  - No line breaks (use spaces instead)
  - Use quotes for complex text: "This is a, complex description"

Multiple Values:
  - Labels: "frontend;backend;testing" (semicolon separated)
  - Components: "UI;API;Database"

User Fields:
  - Use email addresses: "john.doe@company.com"
  - Or display names: "John Doe"

Dates:
  - Use format: "2024-12-15" (YYYY-MM-DD)
```

### **Simplified Acceptance Criteria (Separate Field)**

If you want acceptance criteria, add it as a separate column:

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Acceptance Criteria
Story,User Registration Form,Create registration form,High,jane.smith@company.com,Form validates email format and sends verification email
Bug,Login not responsive,Mobile display broken,High,jane.smith@company.com,Form elements stack properly on mobile devices
```

### **Test with Small Batch First:**

csv

```csv
Issue Type,Summary,Description,Priority,Assignee,Labels
Story,Test Registration Form,Simple test story,Medium,your.email@company.com,test
Bug,Test Mobile Bug,Simple test bug,Low,your.email@company.com,test;mobile
Task,Test Documentation,Simple test task,Low,your.email@company.com,test;docs
```

## **Field Mapping Order (You Did It Right!)**

✅ **What you did is correct:**

1. Upload CSV file first
2. Map fields after upload
3. Jira shows you preview
4. You can adjust mappings
5. Then import

**Summary field being required is normal** - it's the only mandatory field in Jira.

Try the simplified format above - it should import cleanly and you can always add more complex data later through the UI or API!

Retry

K

Oh there's almost no actual content within the Jira itself - build this out to as if there were design and functionality and acceptance criteria details in there worth turning into product documentation

Edit

# Detailed Jira Issues with Rich Content for Documentation

Here are realistic, detailed Jira issues that would generate meaningful product documentation:

## **Template 1: E-commerce Platform - Software Development**

Retry

K

Ok I ran a test locally

Also how is this a Jira Plugin (how would a user trigger this from within their Jira Environment?)

Edit

# Making Your Code into a Jira Plugin

You're absolutely right - what you ran is a **standalone script**, not a Jira plugin. Let me show you how to turn it into an actual plugin that users can trigger from within Jira.

## **Current State vs Plugin State**

### **What You Have Now:**

yaml

```yaml
Current: Standalone Python script
Trigger: Manual execution (python main.py)
Access: Local computer only
Users: Just you
Integration: External API calls to Jira
```

### **What You Need for a Plugin:**

yaml

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

yaml

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

javascript

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

jsx

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

javascript

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

yaml

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

yaml

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

yaml

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

bash

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

Retry

### jira_processor.py

123 lines

py

### main.py

181 lines

py

K

Ok great - also for the CLI test I ran where would I find the downloaded issues?

How do I make sure I can test each functionality in isolation?

Edit

# Finding Your Downloaded Issues & Testing in Isolation

## **Where to Find Your Downloaded Issues**

Based on your code structure, the issues are saved in:

```
your-project-folder/
├── jira_md_output/           # 👈 Main output folder
│   ├── extreme_defects_with_code_changes/
│   │   ├── XCP-1234.md      # Individual issue files
│   │   ├── XCP-5678.md
│   │   └── ...
│   ├── defects_cwc_test/
│   ├── open_defects_test/
│   ├── processing_summary.json  # 👈 All results in JSON
│   └── SUMMARY_REPORT.md        # 👈 Human-readable summary
├── jira_backups/             # 👈 Raw JSON backups
│   ├── extreme_defects_20241215_143022.json
│   └── ...
```

### **Quick Check Commands:**

bash

```bash
# See what was created
ls jira_md_output/
ls jira_backups/

# Read the summary
cat jira_md_output/SUMMARY_REPORT.md

# Look at a specific processed issue
ls jira_md_output/*/
cat jira_md_output/extreme_defects_with_code_changes/XCP-*.md
```

## **Testing Each Function in Isolation**

### **Create test_functions.py**

python

```python
#!/usr/bin/env python3
"""
Isolated testing for each function
"""

import os
import json
from jira import JIRA
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Import your modules
from jira_processor import process_issue_with_ai, issue_to_enhanced_markdown
from ai_processor import extract_symptom_with_ai, extract_condition_with_ai, classify_issue_with_ai

# Setup Jira client
jira = JIRA(server=os.environ["JIRA_SERVER"], token_auth=os.environ["JIRA_PAT"])

def test_jira_connection():
    """Test 1: Basic Jira connection and issue retrieval"""
    print("🧪 Testing Jira Connection...")
    
    try:
        # Get a single issue to test with
        issues = jira.search_issues("ORDER BY created DESC", maxResults=1)
        if issues:
            issue = issues[0]
            print(f"✅ Connected! Found issue: {issue.key} - {issue.fields.summary}")
            return issue
        else:
            print("❌ No issues found")
            return None
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None

def test_basic_issue_extraction(issue):
    """Test 2: Basic issue data extraction (no AI)"""
    print(f"\n🧪 Testing Basic Issue Extraction for {issue.key}...")
    
    try:
        basic_info = {
            "key": issue.key,
            "summary": issue.fields.summary,
            "status": issue.fields.status.name,
            "type": issue.fields.issuetype.name,
            "priority": getattr(issue.fields.priority, 'name', 'Unknown'),
            "description": issue.fields.description or "No description"
        }
        
        print("✅ Basic extraction successful:")
        for key, value in basic_info.items():
            print(f"   {key}: {value}")
        
        return basic_info
    except Exception as e:
        print(f"❌ Basic extraction failed: {e}")
        return None

def test_ai_symptom_extraction(issue):
    """Test 3: AI symptom extraction only"""
    print(f"\n🧪 Testing AI Symptom Extraction for {issue.key}...")
    
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  OpenAI API key not found - skipping AI test")
        return None
    
    try:
        symptom = extract_symptom_with_ai(issue)
        print(f"✅ Symptom extracted: {symptom}")
        return symptom
    except Exception as e:
        print(f"❌ Symptom extraction failed: {e}")
        return None

def test_ai_condition_extraction(issue):
    """Test 4: AI condition extraction only"""
    print(f"\n🧪 Testing AI Condition Extraction for {issue.key}...")
    
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  OpenAI API key not found - skipping AI test")
        return None
    
    try:
        condition = extract_condition_with_ai(issue)
        print(f"✅ Condition extracted: {condition}")
        return condition
    except Exception as e:
        print(f"❌ Condition extraction failed: {e}")
        return None

def test_ai_classification(issue):
    """Test 5: AI classification only"""
    print(f"\n🧪 Testing AI Classification for {issue.key}...")
    
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  OpenAI API key not found - skipping AI test")
        return None
    
    try:
        category = classify_issue_with_ai(issue)
        print(f"✅ Category classified: {category}")
        return category
    except Exception as e:
        print(f"❌ Classification failed: {e}")
        return None

def test_full_ai_processing(issue):
    """Test 6: Full AI processing pipeline"""
    print(f"\n🧪 Testing Full AI Processing for {issue.key}...")
    
    try:
        processed_data = process_issue_with_ai(issue)
        print("✅ Full processing successful:")
        print(f"   Key: {processed_data['key']}")
        print(f"   Summary: {processed_data['summary']}")
        
        ai_analysis = processed_data.get('ai_analysis', {})
        if ai_analysis:
            print(f"   AI Symptom: {ai_analysis.get('symptom', 'None')}")
            print(f"   AI Condition: {ai_analysis.get('condition', 'None')}")
            print(f"   AI Category: {ai_analysis.get('category', 'None')}")
            print(f"   Confidence: {ai_analysis.get('confidence', 0):.2f}")
        else:
            print("   No AI analysis (OpenAI key missing?)")
        
        return processed_data
    except Exception as e:
        print(f"❌ Full processing failed: {e}")
        return None

def test_markdown_generation(processed_data):
    """Test 7: Markdown generation"""
    print(f"\n🧪 Testing Markdown Generation...")
    
    try:
        markdown = issue_to_enhanced_markdown(processed_data)
        print("✅ Markdown generated successfully")
        print("📄 Preview (first 300 chars):")
        print("-" * 40)
        print(markdown[:300] + "..." if len(markdown) > 300 else markdown)
        print("-" * 40)
        
        # Save test markdown
        test_file = f"test_output_{processed_data['key']}.md"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"📁 Full markdown saved to: {test_file}")
        
        return markdown
    except Exception as e:
        print(f"❌ Markdown generation failed: {e}")
        return None

def test_jql_queries():
    """Test 8: Your predefined JQL queries"""
    print(f"\n🧪 Testing JQL Queries...")
    
    from config import queries
    
    for query_name, jql in queries.items():
        print(f"\n   Testing: {query_name}")
        print(f"   JQL: {jql[:100]}{'...' if len(jql) > 100 else ''}")
        
        try:
            issues = jira.search_issues(jql, maxResults=3)
            print(f"   ✅ Found {len(issues)} issues")
            for issue in issues:
                print(f"      - {issue.key}: {issue.fields.summary[:50]}...")
        except Exception as e:
            print(f"   ❌ Query failed: {e}")

def test_file_operations():
    """Test 9: File saving and backup operations"""
    print(f"\n🧪 Testing File Operations...")
    
    # Test creating directories
    test_dirs = ["test_output", "test_backups"]
    for dir_name in test_dirs:
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"✅ Directory created: {dir_name}")
        except Exception as e:
            print(f"❌ Directory creation failed: {e}")
    
    # Test JSON saving
    test_data = {"test": "data", "timestamp": str(datetime.now())}
    try:
        with open("test_output/test_data.json", "w") as f:
            json.dump(test_data, f, indent=2)
        print("✅ JSON file saved successfully")
    except Exception as e:
        print(f"❌ JSON saving failed: {e}")

def run_all_tests():
    """Run all tests in sequence"""
    print("🚀 Starting Isolated Function Testing")
    print("=" * 60)
    
    # Test 1: Connection
    issue = test_jira_connection()
    if not issue:
        print("❌ Cannot proceed without Jira connection")
        return
    
    # Test 2: Basic extraction
    basic_info = test_basic_issue_extraction(issue)
    if not basic_info:
        print("❌ Cannot proceed without basic extraction")
        return
    
    # Test 3-5: Individual AI functions
    symptom = test_ai_symptom_extraction(issue)
    condition = test_ai_condition_extraction(issue)
    category = test_ai_classification(issue)
    
    # Test 6: Full processing
    processed_data = test_full_ai_processing(issue)
    if processed_data:
        # Test 7: Markdown generation
        test_markdown_generation(processed_data)
    
    # Test 8: JQL queries
    test_jql_queries()
    
    # Test 9: File operations
    test_file_operations()
    
    print("\n" + "=" * 60)
    print("🎉 All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tests()
```

### **Individual Test Commands**

bash

```bash
# Test everything
python test_functions.py

# Test just one function (create mini test files)
python -c "
from test_functions import test_jira_connection
test_jira_connection()
"

# Test AI processing on a specific issue
python -c "
from test_functions import *
from jira import JIRA
import os
jira = JIRA(server=os.environ['JIRA_SERVER'], token_auth=os.environ['JIRA_PAT'])
issue = jira.issue('XCP-1234')  # Replace with real issue key
test_full_ai_processing(issue)
"
```

### **Debug Specific Parts of Your Main Script**

#### **Test Just Query Execution:**

python

```python
# test_queries.py
from config import queries
from jira import JIRA
import os

jira = JIRA(server=os.environ["JIRA_SERVER"], token_auth=os.environ["JIRA_PAT"])

# Test one query at a time
query_name = "defects_cwc_test"  # Change this
jql = queries[query_name]

print(f"Testing query: {query_name}")
print(f"JQL: {jql}")

issues = jira.search_issues(jql, maxResults=5)
print(f"Found {len(issues)} issues:")

for issue in issues:
    print(f"- {issue.key}: {issue.fields.summary}")
```

#### **Test Just AI Processing:**

python

```python
# test_ai_only.py
from ai_processor import extract_symptom_with_ai
from jira import JIRA
import os

jira = JIRA(server=os.environ["JIRA_SERVER"], token_auth=os.environ["JIRA_PAT"])
issue = jira.issue("XCP-1234")  # Use a real issue key

print("Testing AI processing...")
symptom = extract_symptom_with_ai(issue)
print(f"Symptom: {symptom}")
```

### **Check Your Output Quality**

bash

```bash
# Count files created
find jira_md_output -name "*.md" | wc -l

# Check AI processing success rate
grep -r "Confidence:" jira_md_output/ | wc -l

# Find issues with no AI content
grep -L "AI-Generated" jira_md_output/*/*.md

# Check for quality issues
grep -r "Symptom ≠ Condition: ✗" jira_md_output/
```

### **Troubleshooting Common Issues**

yaml

```yaml
Issue: "No files created"
Check: 
  - Does jira_md_output/ folder exist?
  - Are there permission errors?
  - Did JQL queries return any results?

Issue: "AI content empty"
Check:
  - Is OPENAI_API_KEY set correctly?
  - Are you hitting rate limits?
  - Check OpenAI API quota

Issue: "JQL errors"
Check:
  - Do issue types exist in your Jira?
  - Do you have permission to see the issues?
  - Are field names correct for your Jira instance?
```

Run the isolated tests to pinpoint exactly where any issues occur!