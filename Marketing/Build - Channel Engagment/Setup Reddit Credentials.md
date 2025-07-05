To get your Reddit API credentials (CLIENT_ID, CLIENT_SECRET, and set up your USER_AGENT), you need to create a Reddit app. Here's how:

## Step 1: Create a Reddit App

1. **Go to Reddit App Preferences**: https://www.reddit.com/prefs/apps
2. **Log in** with your Reddit account
3. **Scroll down** and click **"Create App"** or **"Create Application"**

## Step 2: Fill Out the Application Form

When creating your app, you'll need to provide:

- **Name**: Choose any name for your app (e.g., "My Reddit Scraper")
- **App type**: Select **"script"** for personal use, or **"web app"** if it's a web application
- **Description**: Brief description of what your app does
- **About URL**: (Optional) Leave blank if you don't have a website
- **Redirect URI**: For scripts, you can use `http://localhost:8080` or `http://www.example.com/unused/redirect/uri`

## Step 3: Get Your Credentials

After creating the app, you'll see:

- **CLIENT_ID**: This is the string of characters directly under your app name (looks like a random string of letters/numbers)
- **CLIENT_SECRET**: This is labeled as "secret" in the app details

## Step 4: Set Up Your Environment Variables

```bash
CLIENT_ID=your_app_id_here
CLIENT_SECRET=your_secret_here
USER_AGENT=python:your-app-name:v1.0 (by /u/your_reddit_username)
```

## Important Notes:

- **Keep your CLIENT_SECRET private** - never share it publicly or commit it to version control
- **USER_AGENT format**: Reddit requires a unique User-Agent string in the format: `<platform>:<app ID>:<version string> (by /u/<reddit username>)`
- Replace `your_reddit_username` with your actual Reddit username
- Many default User-Agents (like "Python/urllib" or "Java") are drastically limited to encourage unique and descriptive user-agent strings

The app creation process is free and you'll have your credentials immediately after creating the app.