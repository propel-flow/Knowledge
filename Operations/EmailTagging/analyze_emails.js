/**
 * Email Campaign Analyzer - Simple Runner Script
 * 
 * This script analyzes HTML email files and generates tag metadata.
 * Customize the input and output paths below.
 */

const fs = require('fs').promises;
const path = require('path');
const EmailCampaignAnalyzer = require('./json_email_analyzer.js');

// ===== CONFIGURATION =====
// Change these paths to match your needs
const CONFIG = {
  // Directory containing HTML email files to analyze
  emailsDirectory: '/Users/katiepotter/0Code/Marketing/Emails/Emails-to-Review',
  
  // Where to save the analysis results
  outputFile: '/Users/katiepotter/0Code/Marketing/Emails/EmailTagging/email_analysis_results.json',
  
  // File pattern to match (e.g., '*.html' for all HTML files)
  filePattern: '.html',
  
  // Whether to print detailed logs
  verbose: true
};

// ===== MAIN FUNCTION =====
async function analyzeEmails() {
  try {
    console.log('Starting email analysis...');
    
    // Create analyzer instance
    const analyzer = new EmailCampaignAnalyzer();
    
    // Get list of email files
    const files = await fs.readdir(CONFIG.emailsDirectory);
    const htmlFiles = files.filter(file => file.endsWith(CONFIG.filePattern));
    
    console.log(`Found ${htmlFiles.length} HTML email files to analyze.`);
    
    // Read and analyze each file
    const emailContents = [];
    for (const file of htmlFiles) {
      const filePath = path.join(CONFIG.emailsDirectory, file);
      if (CONFIG.verbose) console.log(`Reading file: ${file}`);
      
      try {
        const content = await fs.readFile(filePath, 'utf8');
        emailContents.push({
          name: file,
          content: content
        });
      } catch (error) {
        console.error(`Error reading file ${file}:`, error.message);
      }
    }
    
    // Analyze all emails
    console.log('Analyzing emails...');
    
    // Create results structure
    const results = {
      campaigns: [],
      summary: {
        total_analyzed: 0,
        industries: {},
        role_levels: {},
        function_areas: {},
        pain_points: {},
        content_interests: {},
        channels: { email: 0 },
        formats: { html_email: 0 },
        generated_at: new Date().toISOString()
      }
    };
    
    // Process each email individually
    for (const emailFile of emailContents) {
      try {
        if (CONFIG.verbose) console.log(`Analyzing: ${emailFile.name}`);
        const analysis = await analyzer.analyzeEmail(emailFile.content, emailFile.name);
        results.campaigns.push(analysis);
        
        // Update summary stats
        analyzer.updateSummaryStats(results.summary, analysis);
      } catch (error) {
        console.error(`Error analyzing email ${emailFile.name}:`, error.message);
      }
    }
    
    results.summary.total_analyzed = results.campaigns.length;
    
    // Write results to file
    console.log('Writing analysis results to file...');
    await fs.writeFile(CONFIG.outputFile, JSON.stringify(results, null, 2));
    
    // Print summary
    console.log('\n=== ANALYSIS SUMMARY ===');
    console.log(`Total emails analyzed: ${results.summary.total_analyzed}`);
    
    console.log('\nIndustry Distribution:');
    Object.entries(results.summary.industries || {}).forEach(([industry, count]) => {
      console.log(`  ${industry}: ${count}`);
    });
    
    console.log('\nRole Level Distribution:');
    Object.entries(results.summary.role_levels || {}).forEach(([role, count]) => {
      console.log(`  ${role}: ${count}`);
    });
    
    console.log('\nFunction Area Distribution:');
    Object.entries(results.summary.function_areas || {}).forEach(([area, count]) => {
      console.log(`  ${area}: ${count}`);
    });
    
    console.log('\nPain Points Distribution:');
    Object.entries(results.summary.pain_points || {}).forEach(([pain, count]) => {
      console.log(`  ${pain}: ${count}`);
    });
    
    console.log('\nContent Interests Distribution:');
    Object.entries(results.summary.content_interests || {}).forEach(([interest, count]) => {
      console.log(`  ${interest}: ${count}`);
    });
    
    console.log('\nAnalysis complete! Results saved to:', CONFIG.outputFile);
    
  } catch (error) {
    console.error('Error during analysis:', error);
  }
}

// Run the analysis
analyzeEmails();
