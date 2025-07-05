# Automated Workflows – From Commit to Content

Supercharge your documentation workflow by connecting development events directly to your Knowledge Management System (KMS). Stop chasing updates—let automation draft your release notes, help articles, and how-to guides in seconds.

#### Jira-to-Documentation Automation

Automatically convert resolved Jira tickets into draft content. When an issue moves to `Done`, our integration pulls in `ticket.summary`, `ticket.description` (ignoring internal fields like `story_points`), and any attachments—then spins up a well-structured draft in your KMS, tagged and assigned for review.

```python
# Connect Jira to your KMS
from your_kms_sdk import KMS
from your_jira_sdk import Jira

kms = KMS(api_key="YOUR_API_KEY")
jira = Jira(user="user@example.com", token="JIRA_TOKEN")

for issue in jira.search_issues('project = NEWFEAT AND status = Done'):
    kms.create_draft_from_ticket(
        ticket_id=issue.key,
        title=issue.summary,
        content=issue.description
    )
```

### Note
Teams using this integration report draft creation **75% faster**, freeing technical writers to focus on clarity and polish—not data gathering.

#### UI-Test Environment → “How-To” Guide

Generate user-facing documentation in parallel with development. Trigger our GitHub Action on pushes to your `staging` branch or UI test environment. When new buttons appear or menus shift, it detects component or localization changes (e.g. in `en.json`), captures screenshots from your test suite, and assembles a draft how-to guide.
### Important
**Secure & Configurable**: Choose which Jira projects, ticket types, or Git branches trigger drafts. Your API keys and secrets stay encrypted—and unwanted noise stays out.

Supercharge your workflows. [Get started today.](https://calendly.com/propel-flow/ai-use-case-discovery?month=2025-06)