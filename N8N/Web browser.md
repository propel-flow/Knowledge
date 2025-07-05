What’s the url link to N8N Jira template?

Also does this work with Jira Forge?

And what about with webbrowser plugins?

## 3. **Web Browser Plugin Compatibility**

N8N has **excellent browser automation capabilities** but **limited direct browser extension integration**:

### **Current Browser Automation:**

- **Puppeteer Integration**: N8N has a community node for browser automation using Puppeteer that can execute custom scripts, capture screenshots and PDFs, scrape content, and automate web interactions using Chrome/Chromium's DevTools Protocol
- **HTTP Request Nodes**: Can interact with web APIs that browser extensions might use

### **Browser Extension Integration:**

- There's a community feature request for a Chrome Extension that could send POST requests to N8N Trigger nodes and await responses, potentially sending context like the current URL or additional settings
- **MCP Browser Integration**: While not explicitly confirmed, MCP's architecture could potentially support browser-based MCP clients

### **Workarounds for Browser Integration:**

1. **Browser Automation**: Use Puppeteer nodes to control browsers programmatically
2. **Webhook Triggers**: Browser extensions could send data to N8N via webhooks
3. **API Integration**: Extensions could interact with N8N's REST API
4. **Bookmarklets**: Simple JavaScript bookmarklets could trigger N8N workflows
K

Does it have it for selenium or playwright?


Great! Based on my research, I can now provide you with comprehensive information about N8N's support for Selenium and Playwright.

## **Selenium Support in N8N**

### **Current Status: Limited Direct Support**

- **No official Selenium node**: There is a community feature request to include a selenium node that will extend n8n's webscraping abilities, where users can write their own webdriver commands in javascript and send it to selenium [toema/n8n-playwright | DeepWiki](https://deepwiki.com/toema/n8n-playwright)
- **Workaround available**: You can use Selenium through the **Execute Command** node or **Code** node to run Selenium scripts

### **Alternative: Browserless with Selenium**

N8N has community nodes for Browserless, which provides first-class integrations for Puppeteer, Playwright, Selenium WebDriver, and several REST APIs for common tasks

**Installation:**

bash

```bash
# Run Browserless with Selenium support
docker run --rm -p 3000:3000 -e "CONCURRENT=10" -e "TOKEN=6R0W53R135510" ghcr.io/browserless/chromium

# Install in N8N
# Visit n8n > Settings > Community Nodes > Install n8n-nodes-browserless
```

## **Playwright Support in N8N**

### **Community Node Available**

There is an n8n community node for browser automation using Playwright that lets you automate browser actions using Playwright in your n8n workflows

**GitHub Repository:** `toema/n8n-playwright`

### **Browserless + Playwright Integration**

There are detailed community guides for integrating n8n with self-hosted Browserless and Playwright to generate PDFs, create screenshots, and more

**Setup Process:**

1. **Docker Setup**: Use Browserless with Playwright support
2. **Authentication**: Set up Header Auth with your Playwright token
3. **Workflows**: Create workflows for:
    - Screenshots
    - PDF generation
    - Content retrieval
    - File downloads
    - Web scraping

## **Browser Automation Options in N8N**

### **1. Puppeteer (Most Mature)**

- **Official community node**: `n8n-nodes-puppeteer`
- **Full Puppeteer API access**
- **Custom scripts supported**
- **Screenshots, PDFs, scraping**

### **2. Browserless (Recommended for Production)**

Browserless offers first-class integrations for puppeteer, playwright, selenium's webdriver, and handles common issues like missing system-fonts, missing external libraries, and performance improvements

**Advantages:**

- Supports **all three**: Puppeteer, Playwright, AND Selenium
- Docker-based scaling
- Handles browser infrastructure
- Session management
- File downloads
- Performance optimizations

### **3. Direct Integration Options**

**For Selenium:**

javascript

```javascript
// In Code Node or Execute Command Node
const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

const driver = new Builder()
  .forBrowser('chrome')
  .setChromeOptions(new chrome.Options().headless())
  .build();

// Your Selenium automation code
```

**For Playwright:**

javascript

```javascript
// In Code Node
const { chromium } = require('playwright');

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
// Your Playwright automation code
```

## **Recommendations**

### **For Production Use:**

1. **Browserless** - Best overall solution supporting all three frameworks
2. **Self-hosted setup** with Docker for better control
3. **N8N Browserless community node** for easy integration

### **For Simple Tasks:**

1. **Puppeteer node** - Most mature and stable
2. **Direct code integration** via Code nodes

### **For Selenium Specifically:**

1. **Browserless with Selenium support** (recommended)
2. **Execute Command node** to run Selenium scripts
3. **Code node** with Selenium WebDriver installed

## **Current Limitations**

- **No native Selenium node** (community requested feature)
- **Playwright node is community-maintained** (not official)
- **Browser infrastructure setup** can be complex without Browserless

The **Browserless approach** is currently the most comprehensive solution since it provides first-class integrations for Puppeteer, Playwright, Selenium WebDriver, and addresses common issues like missing system fonts, external libraries, and performance improvements.

Retry