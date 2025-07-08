## **Ghost CMS:**

- Main repository: [https://github.com/TryGhost/Ghost](https://github.com/TryGhost/Ghost)
- Official website: [https://ghost.org](https://ghost.org)
- Documentation: [https://ghost.org/docs/](https://ghost.org/docs/)
- Self-hosting guide: [https://ghost.org/docs/install/](https://ghost.org/docs/install/)

## **Strapi:**

- Main repository: [https://github.com/strapi/strapi](https://github.com/strapi/strapi)
- Official website: [https://strapi.io](https://strapi.io)
- Documentation: [https://docs.strapi.io/](https://docs.strapi.io/)
- Quick start guide: [https://docs.strapi.io/dev-docs/quick-start](https://docs.strapi.io/dev-docs/quick-start)

Both are actively maintained open source projects with MIT licenses. Ghost is a Node.js publishing platform focused on content creation and blogging, while Strapi is a headless CMS that provides APIs for frontend applications. You can clone either repository directly or follow their respective installation guides for setting up local development environments.

## Ghost MCP

I'm not immediately familiar with a specific MCP (Model Context Protocol) implementation for Ghost CMS. Since MCP is a relatively recent protocol from Anthropic for connecting AI assistants to data sources, and my knowledge has a cutoff date, let me search for current information about Ghost MCP integrations.Great! I found several Ghost MCP implementations. Here are the main Ghost MCP servers available:

**Primary Ghost MCP Servers:**

1. **MFYDev/ghost-mcp** - A comprehensive Model Context Protocol server for Ghost CMS that provides secure access to your Ghost blog through JWT authentication, with tools for managing posts, users, members, tiers, offers, and newsletters
    
    - Repository: https://github.com/MFYDev/ghost-mcp
    - Features: Full Ghost Admin API integration, advanced search, robust error handling
2. **mtane0412/ghost-mcp-server** - Another MCP server that integrates with the Ghost Admin API, enabling programmatic access to Ghost CMS features including post management, page management, and member management
    
    - Repository: https://github.com/mtane0412/ghost-mcp-server
    - Available via npm: `@mtane0412/ghost-mcp-server`
3. **jgardner04/Ghost-MCP-Server** - An MCP Server specifically focused on managing posts on Ghost CMS, designed to work with MCP clients like Cursor or Claude Desktop
    
    - Repository: https://github.com/jgardner04/Ghost-MCP-Server

**Official MCP Servers Collection:** The official Model Context Protocol servers repository also lists Ghost as one of the available MCP servers for interacting with Ghost CMS through LLM interfaces like Claude

These MCP servers allow you to control your Ghost blog through conversational AI interfaces, enabling tasks like content creation, member management, and newsletter handling directly through Claude or other MCP-compatible AI tools.

---
Here are all the MCP URL sources from my search for your reference:

**Primary Articles & Blog Posts:**

- https://fanyangmeng.blog/introducing-ghost-mcp-a-model-context-protocol-server-for-ghost-cms/
- https://cline.ghost.io/forget-model-context-protocol-just-think-of-these-as-extra-tools-for-cline/
- https://ghost.codersera.com/blog/creating-a-model-context-protocol-mcp-server-in-c/

**GitHub Repositories:**

- https://github.com/MFYDev/ghost-mcp
- https://github.com/mtane0412/ghost-mcp-server
- https://github.com/jgardner04/Ghost-MCP-Server
- https://github.com/modelcontextprotocol/servers
- https://github.com/wong2/awesome-mcp-servers

**MCP Server Directory:**

- https://mcp.so/server/ghost-mcp-server

**Community Discussion:**

- https://news.ycombinator.com/item?id=43049408 (Hacker News - though this particular item wasn't accessible)

These sources should give you comprehensive information about Ghost MCP implementations, the broader MCP ecosystem, and community discussions around using MCP servers with various tools and platforms.