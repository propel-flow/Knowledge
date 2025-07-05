Not templates really yet

## 1. **N8N Jira Template URL**

The specific N8N Jira MCP Server template URL is:

**[https://n8n.io/workflows/3939-jira-mcp-server/](https://n8n.io/workflows/3939-jira-mcp-server/)**

This n8n workflow creates a powerful AI-powered Jira management system that allows you to use Claude or other AI assistants to create, update, and manage Jira tickets through natural language requests [Jira Software node documentation | n8n Docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/).

## 2. **Jira Forge Compatibility**

Based on my research, **N8N's MCP integration works with Jira Cloud APIs, but there's no specific evidence of direct Jira Forge app integration**. However, there are several approaches:

### **Current Status:**

- The workflow requires an active Jira Cloud account with admin access and n8n instance with the Langchain and MCP nodes installed [n8n-nodes-mcp - npm](https://www.npmjs.com/package/n8n-nodes-mcp)
- There are community discussions about integrating mcp-atlassian with n8n, though some users have reported challenges getting it working properly
- Atlassian has introduced their own Remote MCP Server in beta, which allows Jira and Confluence Cloud customers to interact with their data directly from Claude [Provide and use Model Context Protocol - Feature Requests - n8n Community](https://community.n8n.io/t/provide-and-use-model-context-protocol/63799)

### **Forge Integration Options:**

1. **Use Atlassian's Official MCP Server**: Atlassian's Remote MCP Server runs on Cloudflare infrastructure and serves as the bridge for Jira and Confluence Cloud customers [Provide and use Model Context Protocol - Feature Requests - n8n Community](https://community.n8n.io/t/provide-and-use-model-context-protocol/63799)
2. **Custom API Integration**: Build Forge apps that expose APIs, then connect those to N8N via HTTP Request nodes
3. **Webhook Integration**: Create Forge apps that send webhooks to N8N workflows

## **Summary**

- ✅ **N8N Jira Template**: Available at [https://n8n.io/workflows/3939-jira-mcp-server/](https://n8n.io/workflows/3939-jira-mcp-server/)
- ⚠️ **Jira Forge**: Not directly supported, but possible through Atlassian's MCP Server or custom API integration
- ⚠️ **Browser Plugins**: Limited direct support, but excellent browser automation via Puppeteer and potential webhook integration

The MCP ecosystem is rapidly evolving, so direct browser extension and Forge app support may improve in the near future as the protocol gains wider adoption.