/**
 * Auto Tag Script for Email Campaign JSON
 * Automatically adds channel_format tags to all email campaigns
 * 
 * Usage:
 * 1. Copy your JSON data into the campaignData variable
 * 2. Run the script
 * 3. Copy the output JSON
 */

// ===== PASTE YOUR JSON DATA HERE =====
const campaignData = {
  // Paste your email_campaigns JSON here
  // Example structure:
  "email_campaigns": [
    // Your campaigns...
  ],
  "metadata": {
    // Your metadata...
  }
};

// ===== CONFIGURATION =====
const DEFAULT_CHANNEL_FORMAT = {
  end_channel: "email",
  content_format: "html_email", 
  character_limit: null, // No limit for email
  visual_elements: "rich_formatting",
  platform_notes: {
    primary: "Email campaigns with full HTML formatting",
    reuse_potential: {
      linkedin: {
        adaptations_needed: ["Convert to plain text", "Add emojis/bullets", "Shorten to 3000 chars", "Break into 2-3 line paragraphs"],
        character_limit: 3000,
        visual_elements: "emojis_bullets"
      },
      facebook: {
        adaptations_needed: ["Convert to plain text", "Heavy emoji usage", "Very short paragraphs", "Mobile-first formatting"],
        character_limit: 63206,
        visual_elements: "emojis_bullets"
      },
      twitter: {
        adaptations_needed: ["Extreme condensing", "Thread format", "Heavy hashtag usage"],
        character_limit: 280,
        visual_elements: "minimal_formatting"
      },
      blog: {
        adaptations_needed: ["Expand content", "Add SEO elements", "Include images"],
        character_limit: null,
        visual_elements: "rich_formatting"
      }
    }
  }
};

// ===== SCRIPT FUNCTIONS =====

function addChannelFormatTags(data) {
  const campaigns = data.email_campaigns || data.campaigns || [];
  
  console.log(`Processing ${campaigns.length} campaigns...`);
  
  campaigns.forEach((campaign, index) => {
    // Add channel_format if it doesn't exist
    if (!campaign.channel_format) {
      campaign.channel_format = { ...DEFAULT_CHANNEL_FORMAT };
      
      // Update modified timestamp
      if (campaign.dublin_core) {
        campaign.dublin_core.modified = new Date().toISOString();
      }
      
      console.log(`✅ Added channel_format to: ${campaign.title || campaign.id}`);
    } else {
      console.log(`⏭️  Skipped (already has channel_format): ${campaign.title || campaign.id}`);
    }
  });
  
  // Update metadata
  if (data.metadata) {
    data.metadata.last_auto_tagged = new Date().toISOString();
    data.metadata.auto_tag_version = "1.0";
  }
  
  return data;
}

function validateAndCleanTags(data) {
  const campaigns = data.email_campaigns || data.campaigns || [];
  
  campaigns.forEach(campaign => {
    if (campaign.campaign_tags) {
      // Ensure arrays are actually arrays
      ['industry', 'functional_area', 'pain_category', 'solution_type', 'competitor_alternatives', 'objections'].forEach(field => {
        if (campaign.campaign_tags[field] && !Array.isArray(campaign.campaign_tags[field])) {
          campaign.campaign_tags[field] = [campaign.campaign_tags[field]];
        }
      });
      
      // Remove empty arrays
      Object.keys(campaign.campaign_tags).forEach(key => {
        if (Array.isArray(campaign.campaign_tags[key]) && campaign.campaign_tags[key].length === 0) {
          delete campaign.campaign_tags[key];
        }
      });
    }
  });
  
  return data;
}

function generateSummaryReport(data) {
  const campaigns = data.email_campaigns || data.campaigns || [];
  
  const summary = {
    total_campaigns: campaigns.length,
    channels: {},
    formats: {},
    missing_tags: [],
    campaign_types: {}
  };
  
  campaigns.forEach(campaign => {
    // Count channels
    const channel = campaign.channel_format?.end_channel || 'unknown';
    summary.channels[channel] = (summary.channels[channel] || 0) + 1;
    
    // Count formats  
    const format = campaign.channel_format?.content_format || 'unknown';
    summary.formats[format] = (summary.formats[format] || 0) + 1;
    
    // Count campaign types
    const type = campaign.source_data?.campaign_type || 'unknown';
    summary.campaign_types[type] = (summary.campaign_types[type] || 0) + 1;
    
    // Check for missing critical tags
    if (!campaign.campaign_tags?.industry || campaign.campaign_tags.industry.length === 0) {
      summary.missing_tags.push(`${campaign.id}: missing industry tags`);
    }
    if (!campaign.campaign_tags?.pain_category || campaign.campaign_tags.pain_category.length === 0) {
      summary.missing_tags.push(`${campaign.id}: missing pain_category tags`);
    }
  });
  
  return summary;
}

// ===== MAIN EXECUTION =====

function runAutoTagger() {
  console.log("🚀 Starting Auto Tag Script...");
  
  // Validate input
  if (!campaignData || (!campaignData.email_campaigns && !campaignData.campaigns)) {
    console.error("❌ Error: No valid campaign data found. Please paste your JSON data in the campaignData variable.");
    return null;
  }
  
  // Process the data
  let processedData = { ...campaignData };
  
  // Step 1: Add channel format tags
  processedData = addChannelFormatTags(processedData);
  
  // Step 2: Validate and clean existing tags  
  processedData = validateAndCleanTags(processedData);
  
  // Step 3: Generate summary
  const summary = generateSummaryReport(processedData);
  
  console.log("\n📊 SUMMARY REPORT:");
  console.log("==================");
  console.log(`Total Campaigns: ${summary.total_campaigns}`);
  console.log(`Channels:`, summary.channels);
  console.log(`Formats:`, summary.formats);
  console.log(`Campaign Types:`, summary.campaign_types);
  
  if (summary.missing_tags.length > 0) {
    console.log(`\n⚠️  Missing Tags (${summary.missing_tags.length}):`);
    summary.missing_tags.forEach(tag => console.log(`   - ${tag}`));
  }
  
  console.log("\n✅ Auto tagging complete!");
  console.log("📋 Copy the processedData object below to get your updated JSON");
  
  return processedData;
}

// ===== EXECUTION =====

// Run the script
const updatedData = runAutoTagger();

// Output for copying
if (updatedData) {
  console.log("\n" + "=".repeat(50));
  console.log("COPY THIS UPDATED JSON:");
  console.log("=".repeat(50));
  console.log(JSON.stringify(updatedData, null, 2));
}

// ===== HELPER FUNCTIONS FOR MANUAL USE =====

// Add specific tags to all campaigns
function addTagToAllCampaigns(tagCategory, tagValue) {
  const campaigns = campaignData.email_campaigns || campaignData.campaigns || [];
  
  campaigns.forEach(campaign => {
    if (!campaign.campaign_tags) campaign.campaign_tags = {};
    
    if (['urgency', 'buying_stage'].includes(tagCategory)) {
      campaign.campaign_tags[tagCategory] = tagValue;
    } else {
      if (!campaign.campaign_tags[tagCategory]) campaign.campaign_tags[tagCategory] = [];
      if (!campaign.campaign_tags[tagCategory].includes(tagValue)) {
        campaign.campaign_tags[tagCategory].push(tagValue);
      }
    }
  });
  
  console.log(`✅ Added ${tagCategory}: ${tagValue} to all campaigns`);
}

// Remove specific tags from all campaigns
function removeTagFromAllCampaigns(tagCategory, tagValue) {
  const campaigns = campaignData.email_campaigns || campaignData.campaigns || [];
  
  campaigns.forEach(campaign => {
    if (campaign.campaign_tags?.[tagCategory]) {
      if (Array.isArray(campaign.campaign_tags[tagCategory])) {
        campaign.campaign_tags[tagCategory] = campaign.campaign_tags[tagCategory].filter(tag => tag !== tagValue);
      } else if (campaign.campaign_tags[tagCategory] === tagValue) {
        delete campaign.campaign_tags[tagCategory];
      }
    }
  });
  
  console.log(`✅ Removed ${tagCategory}: ${tagValue} from all campaigns`);
}

// Update channel format for all campaigns
function updateChannelFormatAll(updates) {
  const campaigns = campaignData.email_campaigns || campaignData.campaigns || [];
  
  campaigns.forEach(campaign => {
    if (!campaign.channel_format) campaign.channel_format = {};
    Object.assign(campaign.channel_format, updates);
    
    if (campaign.dublin_core) {
      campaign.dublin_core.modified = new Date().toISOString();
    }
  });
  
  console.log(`✅ Updated channel format for all campaigns:`, updates);
}

// ===== EXAMPLE USAGE =====

/*
// Example 1: Add a tag to all campaigns
addTagToAllCampaigns('industry', 'SaaS');

// Example 2: Remove a tag from all campaigns  
removeTagFromAllCampaigns('pain_category', 'Old Tag Name');

// Example 3: Update channel format for all
updateChannelFormatAll({
  end_channel: 'email',
  content_format: 'html_email'
});

// Example 4: Add multiple tags
['SaaS', 'Technology', 'B2B Software'].forEach(tag => {
  addTagToAllCampaigns('industry', tag);
});
*/