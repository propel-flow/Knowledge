# Generate & Enrich LinkedIn Leads with Apollo.io, LinkedIn API, Mail.so & GPT-3.5

**Source**: https://n8n.io/workflows/3791-generate-and-enrich-linkedin-leads-with-apolloio-linkedin-api-mailso-and-gpt-35/
**Creator**: Joseph
**Last Updated**: 2 months ago
**Categories**: Sales, AI, Marketing
**Status**: Free

---

## Overview

This n8n workflow automates **LinkedIn lead generation, enrichment, and activity analysis** using **Apollo.io**, **RapidAPI**, **Google Sheets** and **Mail.so**.

Perfect for **sales teams, founders, B2B marketers**, and cold outreach pros who want **personalized lead insights** to drive better conversion rates.

---

## ⚙️ How This Workflow Works

The workflow is broken down into several key steps, each designed to help you build and enrich a valuable list of LinkedIn leads:

### 1. 🔑 Lead Discovery (Keyword Search via Apollo)

* Pulls leads using **Apollo.io's API** based on keywords, industries, or job titles.
* Saves lead name, title, company, and LinkedIn URL to your Google Sheet.
* You can replace the trigger node from the form node to a webhook, whatsapp, telegram, etc, any way for you to send over your query variables over to initiate the workflow.

### 2. 🧠 Username Extraction (from LinkedIn URL)

* Extracts the **LinkedIn username** from profile URLs using a simple script node.
* This is required for further enrichment via RapidAPI.

### 3. ✉️ Email Lookup (via Apollo User ID)

* Uses the **Apollo User ID** to retrieve the lead's **verified work email**.
* Ensures high-quality leads with reliable contact info.
* To double check that the email is currently valid, we use the **mail.so** api and filter out emails that fail deliverability and mx-record check. We don't wanna risk sending emails to no longer existent addresses, right?

### 4. 🧾 Profile Summary Enrichment (via RapidAPI)

* Queries the **LinkedIn Data API** to fetch a lead's **profile summary/bio**.
* Gives you a deeper understanding of their background and expertise.

### 5. 📰 Recent Activity Collection (Posts & Reposts)

* Retrieves **recent posts or reposts** from each lead's profile.
* Great for tailoring outreach with reference to what they're currently talking about.

### 6. 🗂️ Leads Database Update

* All enriched data is written to the same Google Sheet.
* New columns are filled in without overwriting existing data.

---

## ✅ Smart Retry & Row Status Logic

Every subworkflow includes a **fail-safe mechanism** to ensure:

* ✅ Each row has status columns (e.g., `done`, `failed`, `pending`).
* 🕒 A **scheduled retry workflow** resets failed rows to `pending` after **2 weeks** (customizable).
* 💬 This gives failed enrichments another chance to be processed later, reducing data loss.

---

## 📋 Google Sheets Setup

**Template 1**: [Apollo Leads Scraping & Enrichment](https://docs.google.com/spreadsheets/d/1d99PlHkp9RPeSAtmATgQ4OC4Selcp8JSFLNuKx-n1EQ/edit?gid=0#gid=0)

**Template 2**: [Enriched Leads Database](https://docs.google.com/spreadsheets/d/1c5USULUPS-2_RdNf29cyDguuHH7A7JNwzFCjQQUJTvE/edit?gid=0#gid=0)

Make a copy to your Drive and use.

Columns will be filled as each subworkflow runs (email, summary, interests, etc.)

---

## 🔐 Required API Keys

To use this workflow, you'll need the following credentials:

### 🧩 Apollo.io

* Sign up and get your key here: [Apollo.io API Keys](https://developer.apollo.io/keys/)
* ⚠️ **Important:** Toggle the **"Master API Key"** option to **ON** when generating your key.
* This ensures the same key can be used for all Apollo endpoints in this workflow.

### 🌐 RapidAPI (LinkedIn Data API)

* Subscribe to the API here: [LinkedIn Data API on RapidAPI](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api)
* Use the key in the `x-rapidapi-key` header in the relevant nodes.

### ✉️ Mail.so

* Sign up and get your key here: [Mail.so API](https://mails.so/dashboard/api)

> 💡 For both APIs, set up the credentials in **n8n as "Generic Credential"** types.
> This way, you won't need to reconfigure the headers in each node.

---

## 🆕 Apify Alternative Option

**Note:** *Now includes an Apify alternative for Rapid API (Some users can't create new accounts on Rapid API, so I have added an alternative for you. But immediately you are able to get access to Rapid API, please use that option, it returns more detailed data).*

### Apify Setup Guide

To use this workflow, you'll need the following credentials:

1. Login to Apify, then open this link: https://console.apify.com/actors/2SyF0bVxmgGr8IVCZ/
2. Click on integrations and scroll down to API Solutions and select "Use API endpoints"
3. Scroll to "Run Actor synchronously and get dataset items" and copy the actor endpoint url
4. Paste it in the placeholder inside the http node of Apify alternative flow "apify-actor-endpoint"

---

## 🛠️ Customization Options

* Modify the Apollo filters (location, industry, seniority) to target your ideal customers.
* Change retry interval in the scheduler (e.g., weekly instead of 2 weeks).
* Connect the database to your email campaign tool like Mailchimp or Instantly.ai.
* Replace the AI nodes with your desired AI agents and customize the system messages further to get desired results.

---

## Key Features

- **Complete Lead Pipeline**: From discovery to enrichment to validation
- **Email Verification**: Built-in email validation using Mail.so
- **Activity Intelligence**: Recent posts and activity for personalization
- **Smart Retry Logic**: Automatic retry for failed enrichments
- **Dual API Options**: RapidAPI or Apify for LinkedIn data
- **Google Sheets Integration**: Ready-to-use templates provided

## Business Value

- **Time Savings**: Automates entire lead research and enrichment process
- **Data Quality**: Email verification ensures deliverable contacts
- **Personalization**: Recent activity data for targeted outreach
- **Scalability**: Process hundreds of leads automatically
- **Reliability**: Built-in retry mechanisms prevent data loss

## Technical Requirements

- **Apollo.io API**: For lead discovery and email lookup
- **RapidAPI or Apify**: For LinkedIn profile data
- **Mail.so API**: For email verification
- **Google Sheets**: For data storage and management
- **N8N**: Workflow automation platform

## Recommended Priority

⭐⭐⭐⭐⭐ **HIGH PRIORITY** - Complete lead generation and enrichment solution

## Integration with Your Stack

- **Input**: Keywords, industries, job titles
- **Processing**: Lead discovery, enrichment, validation
- **Output**: Enriched leads in Google Sheets
- **Follow-up**: Use enriched data for personalized Brevo email campaigns

This workflow is perfect for your Google Sheets + LinkedIn + Brevo stack as it provides the complete lead generation and enrichment pipeline with verified contact data.

---

## Cost Considerations

- **Apollo.io**: Free plan available, paid plans from $49/month
- **RapidAPI**: Pay-per-use, typically $0.01-0.05 per request
- **Mail.so**: Email verification, pricing varies
- **Apify**: Alternative option with different pricing structure

## Setup Complexity

**Intermediate to Advanced** - Requires multiple API setups and credential management, but provides comprehensive lead generation solution.
