/Users/katiepotter/0Code/eMumbaApr23-May2 (Green to keep) - pull more inc AIPS/content-translation-dev-Jun11/conversion_utilities/jira_to_md

you'd need to export AWS creds (as the output goes to the bucket) install jira (pip install jira) and export following env vars

Python export JIRA_SERVER="[https://jira.extremenetworks.com](https://jira.extremenetworks.com/)" export JIRA_EMAIL="<your-jira-email-address" export JIRA_PAT="<your-personal-access-token"

you can generat eyour token here: [https://jira.extremenetworks.com/secure/ViewProfile.jspa?selectedTab=com.atlassian.pats.pats-plugin:jira-user-personal-access-tokens](https://jira.extremenetworks.com/secure/ViewProfile.jspa?selectedTab=com.atlassian.pats.pats-plugin:jira-user-personal-access-tokens)