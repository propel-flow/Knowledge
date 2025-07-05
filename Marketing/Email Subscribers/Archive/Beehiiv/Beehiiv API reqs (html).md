Great question! If your email drafts are generated in **Markdown format** (with headings, bold, images, URLs, etc.) and you want to integrate them via Beehiiv’s API or webhooks, here are key points and requirements to consider:

### 1. Beehiiv API & Content Format

- **Beehiiv’s API typically expects HTML content** for email bodies, not raw Markdown.
- You will need to **convert your Markdown drafts to HTML** before sending them via the API.
- This conversion ensures proper rendering of formatting, images, links, and styles in email clients.

### 2. Markdown to HTML Conversion

- Use a Markdown parser/converter in your workflow (e.g., `marked` in Node.js, `markdown-it`, or Python’s `markdown` library).
- Convert the entire draft to clean, email-friendly HTML.
- Make sure the HTML is **inline-styled** or compatible with email clients (some CSS may not be supported).

### 3. Image Handling

- Markdown image syntax (`![alt](url)`) converts to `<img src="url" alt="alt">`.
- Ensure images are hosted on publicly accessible URLs.
- Some email clients block external images by default; consider embedding images as base64 or using trusted hosts/CDNs.

### 4. URLs and Links

- Markdown links (`[text](url)`) convert to `<a href="url">text</a>`.
- Verify URLs are correct and use HTTPS where possible.
- Test links in the final HTML email.

### 5. Webhook Considerations

- If you use webhooks to trigger workflows (e.g., new draft generated → webhook fires → send to Beehiiv API):
    - Ensure your webhook payload includes the **HTML-converted content**, not raw Markdown.
    - Include metadata like subject, sender info, and any personalization tokens.
    - Handle webhook retries and failures gracefully.

### 6. Preformatting Flows

- Draft generation → Markdown output.
- Markdown → HTML conversion step.
- Optional: HTML sanitization to remove unsupported tags or scripts.
- Send HTML content via Beehiiv API to create or update newsletter drafts.
- Trigger send or schedule via API or Beehiiv dashboard.

---

### Summary Checklist

- Convert Markdown drafts to HTML before API submission.
- Host images on accessible URLs.
- Ensure links are valid and secure.
- Format HTML for email client compatibility.
- Include all necessary metadata in API calls.
- Use webhooks to automate flow triggers with HTML content payloads.

---

If you want, I can help you with sample code to convert Markdown to email-ready HTML and prepare API payloads for Beehiiv or similar platforms. Would you like that?