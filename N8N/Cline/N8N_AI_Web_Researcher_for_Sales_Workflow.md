# AI Web Researcher for Sales - N8N Workflow

**Source**: https://n8n.io/workflows/2324-ai-web-researcher-for-sales/
**Creator**: Lucas Perret
**Last Updated**: 1 year ago
**Categories**: Sales, AI
**Status**: Free

---

## Who is this for?

This workflow is for all sales reps and lead generation managers who need to prepare their prospecting activities, and find relevant information to personalize their outreach.

## Use Case

This workflow allows you to do account research with the web using AI.

It has the potential to replace manual work done by sales rep when preparing their prospecting activities by searching complex information available online.

## What this workflow does

The advanced AI module has 2 capabilities:

* Research Google using SerpAPI
* Visit and get website content using a sub-workflow

From an unstructured input like a domain or a company name.

It will return the following properties:

* domain
* company LinkedIn URL
* cheapest plan
* has free trial
* has enterprise plan
* has API
* market (B2B or B2C)

The strength of n8n here is that you can adapt this workflow to research whatever information you need.

You just have to precise it in the prompt and to precise the output format in the "Structured Output Parser" module.

## Key Features

- **Google Research**: Uses SerpAPI for web search
- **Website Content Analysis**: Visits and extracts website content
- **AI-Powered Analysis**: Processes unstructured data into structured output
- **Customizable Output**: Adaptable to research any information you need
- **Structured Data**: Returns organized company intelligence

## Business Value

- **Time Savings**: Automates hours of manual research per prospect
- **Consistency**: Standardized research process across all prospects
- **Scalability**: Can research hundreds of companies automatically
- **Personalization**: Provides specific data points for targeted outreach
- **Competitive Intelligence**: Gathers pricing, features, and market positioning

## Technical Requirements

- **SerpAPI**: For Google search functionality
- **OpenAI API**: For AI analysis and structured output
- **N8N**: Workflow automation platform
- **HTTP Request capabilities**: For website content extraction

## Implementation Notes

- Detailed instructions + video guide available at: https://lempire.notion.site/AI-Web-research-with-n8n-a25aae3258d0423481a08bd102f16906
- Customizable prompts for different research needs
- Structured Output Parser for consistent data format
- Sub-workflow architecture for modular design

## Recommended Priority

⭐⭐⭐⭐⭐ **IMMEDIATE PRIORITY** - Essential for sales teams doing prospect research

## Integration with Your Stack

- **Input**: Company domain or name
- **Processing**: AI research and analysis
- **Output**: Structured data to Google Sheets CRM
- **Follow-up**: Use data for personalized Brevo email campaigns

This workflow is perfect for your Google Sheets + LinkedIn + Brevo stack as it provides the intelligence layer for highly personalized outreach.
