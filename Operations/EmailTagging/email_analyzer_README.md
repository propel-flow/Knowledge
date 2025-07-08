# Email Campaign Analyzer

This system analyzes HTML email templates and applies standardized campaign tags using the updated tag structure. It includes tools for both batch processing of multiple emails and analyzing individual emails.

## Files Overview

- **json_email_analyzer.js**: The core analyzer class that processes HTML emails and extracts metadata
- **run_email_analysis.js**: A script to run batch analysis on a directory of HTML emails
- **apply_tags.js**: A script to apply channel_format tags to existing email_campaigns_metadata.json

## How to Run the Analyzer

### Option 1: Analyze a Directory of Emails (Recommended)

This option uses the `run_email_analysis.js` script to process multiple HTML emails at once.

1. Open your terminal
2. Navigate to the directory containing the script
3. Run the script with Node.js:

```bash
node run_email_analysis.js
```

By default, the script:
- Reads all HTML files from `/Users/katiepotter/0Code/Marketing/Emails/Emails-to-Review`
- Saves results to `/Users/katiepotter/Desktop/email_analysis_results.json`

To analyze a different directory or save to a different location, modify these lines in the script:

```javascript
// Paths
const emailsDir = '/path/to/your/emails';
const outputFile = '/path/to/save/results.json';
```

### Option 2: Use the Analyzer Directly in Your Own Scripts

You can import the `EmailCampaignAnalyzer` class directly and use it in your own code:

```javascript
const EmailCampaignAnalyzer = require('/path/to/json_email_analyzer.js');

// Create analyzer instance
const analyzer = new EmailCampaignAnalyzer();

// Analyze a single email
async function analyzeOneEmail() {
  const htmlContent = '...your HTML content...';
  const analysis = await analyzer.analyzeEmail(htmlContent, 'email_name');
  console.log(analysis);
}

// Optional: Add subscriber data for more accurate tagging
async function analyzeWithSubscriberData() {
  const htmlContent = '...your HTML content...';
  const subscriberData = {
    role: 'Product Manager'
  };
  const analysis = await analyzer.analyzeEmail(htmlContent, 'email_name', subscriberData);
  console.log(analysis);
}
```

### Option 3: Apply Channel Format Tags to Existing JSON

If you have an existing `email_campaigns_metadata.json` file and want to add channel_format tags:

```bash
node apply_tags.js
```

## Customizing the Analyzer

### Modifying Tag Categories

The analyzer uses keyword-based detection for various tag categories. You can modify these in the constructor:

```javascript
// Example: Adding new keywords to the 'Innovation' pain point
this.painPointKeywords = {
  'Innovation': [
    'innovation', 'competitive', 'advantage', 'technology', 'ai', 'ml',
    'digital transformation', 'modern', 'upgrade', 'cutting-edge',
    'new-keyword-1', 'new-keyword-2' // Add your new keywords here
  ],
  // Other categories...
};
```

### Adding New Tag Categories

To add entirely new tag categories:

1. Add the new category and keywords in the constructor
2. Update the `analyzeEmail` method to include the new category in the returned object
3. Update the `updateSummaryStats` method to count the new category

## Output Format

The analyzer generates a JSON structure with:

- **campaigns**: Array of analyzed emails with detailed tags
- **summary**: Statistical breakdown of tag distributions
  - industries
  - role_levels
  - function_areas
  - pain_points
  - content_interests
  - channels
  - formats

## Tag Structure

Each analyzed email includes these tag categories:

- **industry**: Single value from 6 options (Technology, Enterprise, SMB, etc.)
- **role_level**: Single value from 4 options (C-Suite, VP-Director, Manager, Individual)
- **function_area**: Single value from 5 options (Technology, Operations, Growth, Strategy, Support)
- **pain_points**: 1-2 values from 6 options (Scale, Efficiency, Innovation, Quality, Speed, Risk)
- **content_interests**: Multiple values from 5 options (AI-ML, Localization, Content-Ops, Platform, Strategy)
- **channel_format**: Email format details including adaptation notes for other platforms

## Troubleshooting

- **Syntax Error**: If you encounter a syntax error, check the json_email_analyzer.js file for any missing function declarations or brackets.
- **Path Error**: Make sure the paths in the scripts point to the correct locations on your system.
- **Empty Results**: If you get empty results, check that the HTML files contain the expected content structure.
