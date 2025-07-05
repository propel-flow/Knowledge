## **🎯 Brevo API Setup Guide**

Great choice! Let me walk you through setting up Brevo API integration step by step.

## **Phase 1: Basic API Setup**

### **1. Get Your API Key**

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

```javascript
// Steps in Brevo dashboard:
1. Login to your Brevo account
2. Go to "Account" → "SMTP & API" 
3. Click "Generate a new API key"
4. Name it (e.g., "SaaS Launch Integration")
5. Copy and save the key securely
```

### **2. Install Brevo SDK**

```bash
# Initialize npm 
npm init -y

# Install the current package 
npm install @getbrevo/brevo


```

### **3. Basic API Connection Test**

```javascript
// test-connection.js
const SibApiV3Sdk = require('@sendinblue/client');

// Initialize API client
const apiInstance = new SibApiV3Sdk.AccountApi();

// Set API key
const apiKey = apiInstance.authentications['apiKey'];
apiKey.apiKey = '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';

// Test connection
async function testConnection() {
  try {
    const accountInfo = await apiInstance.getAccount();
    console.log('✅ Connected to Brevo successfully!');
    console.log('Account:', accountInfo.body.companyName);
    console.log('Email:', accountInfo.body.email);
  } catch (error) {
    console.error('❌ Connection failed:', error);
  }
}

testConnection();
```

---

## **Phase 2: Basic Email Integration**

### **4. Send Your First Email via API**

```javascript
// send-email.js
const SibApiV3Sdk = require('@sendinblue/client');

// Initialize
const apiInstance = new SibApiV3Sdk.TransactionalEmailsApi();
const apiKey = apiInstance.authentications['apiKey'];
apiKey.apiKey = 'YOUR_API_KEY_HERE';

async function sendWelcomeEmail(subscriberEmail, subscriberName) {
  const sendSmtpEmail = new SibApiV3Sdk.SendSmtpEmail();
  
  // Your custom HTML template
  const htmlContent = `
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Welcome to Propel Flow</title>
    </head>
    <body>
        <!-- Your HTML template from earlier goes here -->
        <div style="max-width: 600px; margin: 0 auto; font-family: Arial, sans-serif;">
            <div style="background: #3c4656; color: white; padding: 25px; text-align: center;">
                <div style="font-size: 24px; font-weight: 700; border: 2px solid white; padding: 12px 20px; display: inline-block;">
                    PROPEL FLOW
                </div>
            </div>
            <div style="padding: 40px 30px;">
                <h1 style="color: #3c4656; font-size: 36px; text-align: center;">
                    Welcome ${subscriberName}!
                </h1>
                <p style="font-size: 18px; color: #666; text-align: center;">
                    You've joined the SaaS operations revolution. Get ready for insights that will transform your business.
                </p>
                <!-- Rest of your template -->
            </div>
        </div>
    </body>
    </html>
  `;

  sendSmtpEmail.sender = {
    name: "Propel Flow",
    email: "hello@propel-flow.com"
  };
  
  sendSmtpEmail.to = [{
    email: subscriberEmail,
    name: subscriberName
  }];
  
  sendSmtpEmail.subject = "Welcome! The $2.3M problem 87% of SaaS companies ignore";
  sendSmtpEmail.htmlContent = htmlContent;

  try {
    const result = await apiInstance.sendTransacEmail(sendSmtpEmail);
    console.log('✅ Email sent successfully:', result.body.messageId);
    return result;
  } catch (error) {
    console.error('❌ Email failed:', error);
    throw error;
  }
}

// Test the function
sendWelcomeEmail('test@example.com', 'John Doe');
```

### **5. Create and Manage Contacts** (NOTE: UPDATE TO BREVO CONNECTIONS!!!!!)

```javascript
// contact-management.js
const SibApiV3Sdk = require('@sendinblue/client');

class BrevoContactManager {
  constructor(apiKey) {
    this.contactsApi = new SibApiV3Sdk.ContactsApi();
    this.contactsApi.authentications['apiKey'].apiKey = apiKey;
  }

  async createContact(email, attributes = {}) {
    const createContact = new SibApiV3Sdk.CreateContact();
    
    createContact.email = email;
    createContact.attributes = {
      FIRSTNAME: attributes.firstName || '',
      LASTNAME: attributes.lastName || '',
      COMPANY: attributes.company || '',
      // SaaS-specific attributes
      SIGNUP_SOURCE: attributes.signupSource || 'website',
      LEAD_SCORE: attributes.leadScore || 0,
      DEMO_INTEREST: attributes.demoInterest || false,
      SECURITY_FOCUS: attributes.securityFocus || false,
      ...attributes
    };

    try {
      const result = await this.contactsApi.createContact(createContact);
      console.log('✅ Contact created:', result.body.id);
      return result.body;
    } catch (error) {
      if (error.status === 400 && error.body.code === 'duplicate_parameter') {
        console.log('Contact already exists, updating...');
        return await this.updateContact(email, attributes);
      }
      throw error;
    }
  }

  async updateContact(email, attributes) {
    const updateContact = new SibApiV3Sdk.UpdateContact();
    updateContact.attributes = attributes;

    try {
      await this.contactsApi.updateContact(email, updateContact);
      console.log('✅ Contact updated:', email);
      return { email, updated: true };
    } catch (error) {
      console.error('❌ Update failed:', error);
      throw error;
    }
  }

  async getContact(email) {
    try {
      const result = await this.contactsApi.getContactInfo(email);
      return result.body;
    } catch (error) {
      console.error('❌ Get contact failed:', error);
      throw error;
    }
  }
}

// Usage example
const contactManager = new BrevoContactManager('YOUR_API_KEY');

// Create a new SaaS prospect
contactManager.createContact('prospect@techcorp.com', {
  firstName: 'Sarah',
  lastName: 'Chen',
  company: 'TechCorp',
  signupSource: 'ai-landing-page',
  leadScore: 25,
  demoInterest: false,
  securityFocus: true
});
```

---

## **Phase 3: Auto-tagging & Behavioral Tracking**

### **6. Behavioral Tracking System**

```javascript
// behavioral-tracking.js
const SibApiV3Sdk = require('@sendinblue/client');

class BehavioralTracker {
  constructor(apiKey) {
    this.contactsApi = new SibApiV3Sdk.ContactsApi();
    this.contactsApi.authentications['apiKey'].apiKey = apiKey;
  }

  async trackBehavior(email, behaviorType, metadata = {}) {
    const behaviorMap = {
      'email_opened': {
        LAST_EMAIL_OPEN: new Date().toISOString(),
        EMAIL_ENGAGEMENT: 'active',
        LEAD_SCORE_DELTA: 5
      },
      'demo_page_viewed': {
        DEMO_INTEREST: true,
        LAST_DEMO_PAGE_VIEW: new Date().toISOString(),
        LEAD_SCORE_DELTA: 15
      },
      'security_content_clicked': {
        SECURITY_FOCUS: true,
        LAST_SECURITY_ENGAGEMENT: new Date().toISOString(),
        LEAD_SCORE_DELTA: 10
      },
      'pricing_page_viewed': {
        PRICING_AWARE: true,
        PURCHASE_INTENT: 'medium',
        LEAD_SCORE_DELTA: 20
      },
      'demo_booked': {
        DEMO_SCHEDULED: true,
        SALES_QUALIFIED: true,
        DEMO_BOOK_DATE: new Date().toISOString(),
        LEAD_SCORE_DELTA: 50
      },
      'inactive_14_days': {
        EMAIL_ENGAGEMENT: 'at_risk',
        LAST_ACTIVITY: new Date(Date.now() - 14*24*60*60*1000).toISOString(),
        LEAD_SCORE_DELTA: -10
      }
    };

    const behaviorData = behaviorMap[behaviorType];
    if (!behaviorData) {
      throw new Error(`Unknown behavior type: ${behaviorType}`);
    }

    try {
      // Get current contact to calculate new lead score
      const contact = await this.contactsApi.getContactInfo(email);
      const currentScore = contact.body.attributes.LEAD_SCORE || 0;
      const newScore = Math.max(0, currentScore + behaviorData.LEAD_SCORE_DELTA);

      // Update contact with behavior data
      const updateData = {
        ...behaviorData,
        LEAD_SCORE: newScore,
        LAST_ACTIVITY: new Date().toISOString(),
        ...metadata
      };

      await this.contactsApi.updateContact(email, {
        attributes: updateData
      });

      console.log(`✅ Behavior tracked: ${behaviorType} for ${email}`);
      
      // Trigger automation if high score
      if (newScore >= 75 && !contact.body.attributes.SALES_QUALIFIED) {
        await this.triggerSalesQualified(email);
      }

      return { behaviorType, newScore, email };
    } catch (error) {
      console.error('❌ Behavior tracking failed:', error);
      throw error;
    }
  }

  async triggerSalesQualified(email) {
    // Add to high-intent list for sales follow-up
    await this.addToList(email, 'sales-qualified');
    console.log(`🎯 Sales qualified trigger: ${email}`);
  }

  async addToList(email, listName) {
    // This would add contact to specific list for automation
    // Lists trigger different email sequences
    const listIds = {
      'sales-qualified': 4,
      'demo-interested': 5,
      'security-focused': 6,
      'at-risk': 7
    };

    const listId = listIds[listName];
    if (listId) {
      await this.contactsApi.addContactToList(listId, {
        emails: [email]
      });
    }
  }
}

// Usage examples
const tracker = new BehavioralTracker('YOUR_API_KEY');

// Track various behaviors
tracker.trackBehavior('user@company.com', 'demo_page_viewed');
tracker.trackBehavior('user@company.com', 'security_content_clicked');
tracker.trackBehavior('user@company.com', 'demo_booked', {
  DEMO_DATE: '2025-01-30',
  DEMO_TYPE: 'enterprise'
});
```

### **7. Webhook Integration for Real-time Tracking**

```javascript
// webhook-server.js
const express = require('express');
const app = express();
app.use(express.json());

const tracker = new BehavioralTracker('YOUR_API_KEY');

// Webhook endpoints for different behaviors
app.post('/webhook/email-opened', async (req, res) => {
  const { email, campaign } = req.body;
  await tracker.trackBehavior(email, 'email_opened', { campaign });
  res.json({ success: true });
});

app.post('/webhook/demo-page-view', async (req, res) => {
  const { email, source } = req.body;
  await tracker.trackBehavior(email, 'demo_page_viewed', { source });
  res.json({ success: true });
});

app.post('/webhook/demo-booking', async (req, res) => {
  const { email, demoDate, demoType } = req.body;
  await tracker.trackBehavior(email, 'demo_booked', {
    DEMO_DATE: demoDate,
    DEMO_TYPE: demoType
  });
  res.json({ success: true });
});

app.listen(3000, () => {
  console.log('🚀 Webhook server running on port 3000');
});
```

---

## **Phase 4: Automation Workflows**

### **8. Automated Email Sequences**

```javascript
// automation-manager.js
class AutomationManager {
  constructor(apiKey) {
    this.emailApi = new SibApiV3Sdk.TransactionalEmailsApi();
    this.emailApi.authentications['apiKey'].apiKey = apiKey;
    this.contactsApi = new SibApiV3Sdk.ContactsApi();
    this.contactsApi.authentications['apiKey'].apiKey = apiKey;
  }

  async triggerWelcomeSequence(email) {
    // Email 1: Immediate welcome
    await this.sendTemplateEmail(email, 'welcome-template', {
      FIRSTNAME: await this.getContactName(email)
    });

    // Schedule follow-up emails
    setTimeout(() => {
      this.sendTemplateEmail(email, 'skills-gap-template');
    }, 2 * 24 * 60 * 60 * 1000); // 2 days

    setTimeout(() => {
      this.sendTemplateEmail(email, 'security-template');
    }, 4 * 24 * 60 * 60 * 1000); // 4 days
  }

  async sendTemplateEmail(email, templateId, params = {}) {
    const sendSmtpEmail = new SibApiV3Sdk.SendSmtpEmail();
    
    sendSmtpEmail.to = [{ email }];
    sendSmtpEmail.templateId = templateId;
    sendSmtpEmail.params = params;

    try {
      const result = await this.emailApi.sendTransacEmail(sendSmtpEmail);
      console.log(`✅ Template email sent: ${templateId} to ${email}`);
      return result;
    } catch (error) {
      console.error('❌ Template email failed:', error);
      throw error;
    }
  }
}
```

---

## **🚀 Next Steps & Advanced Features**

### **Phase 5: Advanced Implementation**

1. **Create email templates** in Brevo dashboard
2. **Set up automation workflows** in Brevo UI
3. **Implement SMS integration** for high-intent prospects
4. **Add Facebook Ads retargeting** for non-converters
5. **Build analytics dashboard** for tracking performance

### **Phase 6: Scaling Features**

1. **A/B testing** implementation
2. **Advanced segmentation** based on behavior
3. **Predictive lead scoring** algorithms
4. **Multi-channel attribution** tracking
5. **Revenue attribution** to marketing activities

### **🔧 Development Environment Setup**

```bash
# Create project structure
mkdir propel-flow-email-automation
cd propel-flow-email-automation
npm init -y
npm install @sendinblue/client express dotenv cron

# Create environment file
echo "BREVO_API_KEY=your_api_key_here" > .env
```

Want me to help you implement any specific part of this integration? I can provide more detailed code for:

- **Email template integration** with your HTML
- **Advanced behavioral tracking** for SaaS metrics
- **Automated sequence management**
- **Analytics and reporting** setup

Which part would you like to tackle first?