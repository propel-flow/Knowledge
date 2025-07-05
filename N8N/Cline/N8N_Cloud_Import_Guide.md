# N8N Cloud Import Guide - Marketing Workflows

## Overview
This guide will help you import the 3 essential marketing workflows into your N8N Cloud instance at `https://propel-flow.app.n8n.cloud`.

**Workflows to Import:**
1. AI-powered email processing autoresponder
2. Auto-label incoming Gmail messages with AI
3. CV Screening with OpenAI (for lead qualification)

## Prerequisites
- Access to your N8N Cloud account: `https://propel-flow.app.n8n.cloud`
- Gmail account: `katie.potter@propel-flow.com`
- OpenAI API key (for AI functionality)
- Downloaded workflow files in your Downloads folder

## Step-by-Step Import Process

### Step 1: Access Your N8N Cloud Instance
1. Open your browser and go to: `https://propel-flow.app.n8n.cloud`
2. Log in with your credentials
3. You should see your N8N dashboard

### Step 2: Import First Workflow - Gmail Auto-Responder

#### 2.1 Create New Workflow
1. Click the **"+ New Workflow"** button (usually in top-right corner)
2. In the new workflow editor, look for **"Import"** option
   - This might be in a menu (three dots) or as a direct button
   - Or look for **"File"** → **"Import"**

#### 2.2 Import the File
1. Click **"Import from File"** or **"Import Workflow"**
2. Navigate to your Downloads folder
3. Select: **"AI-powered email processing autoresponder and response approval (Yes_No).txt"**
4. Click **"Open"** or **"Import"**

#### 2.3 Rename the Workflow
1. Once imported, click on the workflow name (usually at the top)
2. Rename it to: **"Gmail Auto-Responder - Propel Flow"**
3. Save the workflow (Ctrl+S or Cmd+S)

### Step 3: Import Second Workflow - Email Labeling

#### 3.1 Create Another New Workflow
1. Go back to your workflows list (click "Workflows" in sidebar)
2. Click **"+ New Workflow"** again

#### 3.2 Import Email Labeling Workflow
1. Click **"Import from File"**
2. Select: **"Auto-label incoming Gmail messages with AI nodes.txt"**
3. Import the file
4. Rename to: **"Gmail Lead Labeling - Propel Flow"**
5. Save the workflow

### Step 4: Import Third Workflow - Lead Qualification

#### 4.1 Create Third New Workflow
1. Return to workflows list
2. Click **"+ New Workflow"**

#### 4.2 Import Lead Qualification Workflow
1. Click **"Import from File"**
2. Select: **"CV Screening with OpenAI.txt"**
3. Import the file
4. Rename to: **"Lead Qualification - Propel Flow"**
5. Save the workflow

## Step 5: Set Up Credentials

### 5.1 Gmail OAuth2 Setup
1. Go to **"Settings"** → **"Credentials"** (or look for a credentials section)
2. Click **"Add Credential"**
3. Search for **"Gmail OAuth2 API"**
4. Click on it to start setup

#### Gmail OAuth2 Configuration:
1. **Client ID**: You'll need to create this in Google Cloud Console
2. **Client Secret**: From Google Cloud Console
3. **Scope**: `https://www.googleapis.com/auth/gmail.modify`

#### Quick Google Cloud Setup:
1. Go to: https://console.cloud.google.com
2. Create a new project or select existing one
3. Enable Gmail API
4. Create OAuth2 credentials
5. Add your N8N redirect URL (N8N will show you this)
6. Copy Client ID and Secret back to N8N

### 5.2 OpenAI API Setup
1. In N8N Credentials, click **"Add Credential"**
2. Search for **"OpenAI"**
3. Enter your OpenAI API key
4. Test the connection
5. Save the credential

### 5.3 Google Sheets Setup (for lead tracking)
1. Add **"Google Sheets OAuth2 API"** credential
2. Use the same Google Cloud project as Gmail
3. Enable Google Sheets API
4. Use the same OAuth2 credentials

## Step 6: Configure Each Workflow

### 6.1 Gmail Auto-Responder Configuration
1. Open the **"Gmail Auto-Responder - Propel Flow"** workflow
2. Click on each node that shows a red error indicator
3. For Gmail nodes:
   - Select your Gmail OAuth2 credential
   - Configure the email filters (which emails to respond to)
4. For OpenAI nodes:
   - Select your OpenAI credential
   - Customize the response prompt for Propel Flow

#### Sample Auto-Responder Prompt:
```
You are a helpful assistant for Propel Flow. We help startups and businesses automate their workflows and processes. 

Respond professionally to this email inquiry. Mention our key benefits:
- Workflow automation expertise
- AI-powered solutions
- Rapid implementation

Always end with: "Would you like to schedule a brief call to discuss how Propel Flow can help automate your business processes?"

Keep responses under 150 words and maintain a friendly, professional tone.
```

### 6.2 Email Labeling Configuration
1. Open the **"Gmail Lead Labeling - Propel Flow"** workflow
2. Configure Gmail credential
3. Set up label categories:
   - "Hot Lead" - Immediate interest, budget mentioned
   - "Warm Lead" - Interest shown, needs nurturing
   - "Cold Lead" - General inquiry
   - "Partnership" - Business partnership inquiries
   - "Support" - Customer support requests

### 6.3 Lead Qualification Configuration
1. Open the **"Lead Qualification - Propel Flow"** workflow
2. Configure OpenAI credential
3. Adapt the qualification criteria:

#### Lead Qualification Prompt:
```
Analyze this lead information and score from 1-10 based on:

1. Budget: Do they mention budget or pricing? (0-2 points)
2. Authority: Are they a decision maker? (0-2 points)  
3. Need: Do they have a clear automation problem? (0-2 points)
4. Timeline: When do they need a solution? (0-2 points)
5. Fit: Are they a good fit for workflow automation? (0-2 points)

Provide:
- Total Score (1-10)
- Qualification Status (Hot: 8-10, Warm: 5-7, Cold: 1-4)
- Key insights
- Recommended next steps

Lead Information: {input_data}
```

## Step 7: Create Lead Tracking Sheet

### 7.1 Create Google Sheet
1. Go to Google Sheets: https://sheets.google.com
2. Create a new sheet named: **"Propel Flow Leads Master"**
3. Add these columns:
   - A: Timestamp
   - B: Email Address
   - C: Name
   - D: Company
   - E: Lead Score (1-10)
   - F: Status (Hot/Warm/Cold)
   - G: Source
   - H: Notes
   - I: Follow-up Date

### 7.2 Connect Workflows to Sheet
1. In each workflow, add a **"Google Sheets"** node at the end
2. Configure it to append new rows to your tracking sheet
3. Map the data fields from the workflow to the sheet columns

## Step 8: Test Each Workflow

### 8.1 Test Auto-Responder
1. **IMPORTANT**: Set to manual execution first (don't activate automatically)
2. Send yourself a test email to katie.potter@propel-flow.com
3. Manually trigger the workflow
4. Check if:
   - Email is detected
   - AI response is generated
   - Response matches your brand voice
   - Data is logged to Google Sheets

### 8.2 Test Email Labeling
1. Send test emails with different content types
2. Run the workflow manually
3. Check if labels are applied correctly
4. Adjust AI prompts if needed

### 8.3 Test Lead Qualification
1. Create sample lead data
2. Run the qualification workflow
3. Verify scoring works correctly
4. Check that results go to Google Sheets

## Step 9: Gradual Activation

### 9.1 Start with Email Labeling (Lowest Risk)
1. Activate the email labeling workflow first
2. Monitor for 24-48 hours
3. Ensure it's working correctly

### 9.2 Activate Lead Qualification
1. Once labeling is stable, activate qualification
2. Monitor lead scoring accuracy
3. Adjust prompts as needed

### 9.3 Finally Activate Auto-Responder
1. **Keep manual approval enabled initially**
2. Review each auto-generated response before sending
3. Once confident, enable automatic sending

## Step 10: Webhook Setup for Future GitHub Integration

### 10.1 Create Webhook Endpoints
1. In each workflow, add a **"Webhook"** trigger node at the beginning
2. N8N will generate webhook URLs like:
   - `https://propel-flow.app.n8n.cloud/webhook/auto-responder`
   - `https://propel-flow.app.n8n.cloud/webhook/lead-labeling`
   - `https://propel-flow.app.n8n.cloud/webhook/lead-qualification`

### 10.2 Save Webhook URLs
Keep these URLs for future GitHub Actions integration:
- Auto-Responder Webhook: `[URL from N8N]`
- Lead Labeling Webhook: `[URL from N8N]`
- Lead Qualification Webhook: `[URL from N8N]`

## Troubleshooting

### Common Issues:

#### 1. Gmail Authentication Fails
- Ensure Gmail API is enabled in Google Cloud
- Check OAuth2 redirect URL matches N8N's requirement
- Verify scopes include `gmail.modify`

#### 2. OpenAI API Errors
- Check API key is valid and has credits
- Verify the model (GPT-3.5-turbo or GPT-4) is accessible
- Check rate limits

#### 3. Workflow Doesn't Trigger
- Verify trigger conditions (email filters, etc.)
- Check if workflow is activated
- Look at execution logs for errors

#### 4. Google Sheets Connection Issues
- Ensure Google Sheets API is enabled
- Check OAuth2 permissions include Sheets access
- Verify sheet sharing permissions

### Getting Help:
- Check N8N execution logs for detailed error messages
- Use N8N's built-in testing features
- Start with manual execution before enabling automatic triggers

## Success Checklist

- [ ] All 3 workflows imported successfully
- [ ] Gmail OAuth2 credential configured and tested
- [ ] OpenAI credential configured and tested
- [ ] Google Sheets credential configured and tested
- [ ] Lead tracking sheet created with proper columns
- [ ] Auto-responder prompt customized for Propel Flow
- [ ] Email labeling categories configured
- [ ] Lead qualification criteria adapted
- [ ] All workflows tested manually
- [ ] Email labeling workflow activated
- [ ] Lead qualification workflow activated
- [ ] Auto-responder workflow activated (with manual approval)
- [ ] Webhook URLs saved for future GitHub integration

## Next Steps After Setup

1. **Monitor Performance**: Check Google Sheets daily for lead data
2. **Refine Prompts**: Adjust AI prompts based on actual responses
3. **Scale Gradually**: Add more automation as you get comfortable
4. **GitHub Integration**: Connect your existing scripts via webhooks
5. **Advanced Features**: Add more sophisticated workflows as needed

Your marketing automation system is now ready to help Propel Flow capture and qualify leads 24/7!
