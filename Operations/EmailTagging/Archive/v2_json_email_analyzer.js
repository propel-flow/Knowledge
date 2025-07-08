/**
 * HTML Email Campaign Analyzer - Updated for Streamlined Tag Structure
 * Analyzes existing HTML email templates and applies standardized campaign tags
 * Aligned with recommended 6-category tag structure
 */

class EmailCampaignAnalyzer {
    constructor() {
        // Updated to match recommended tag structure
        this.DEFAULT_CHANNEL_FORMAT = {
            end_channel: "email",
            content_format: "html_email", 
            character_limit: null,
            visual_elements: "rich_formatting",
            platform_notes: {
                primary: "Email campaigns with full HTML formatting",
                reuse_potential: {
                    linkedin: {
                        adaptations_needed: ["Convert to plain text", "Add emojis/bullets", "Shorten to 3000 chars"],
                        character_limit: 3000,
                        visual_elements: "emojis_bullets"
                    },
                    facebook: {
                        adaptations_needed: ["Convert to plain text", "Heavy emoji usage", "Mobile-first formatting"],
                        character_limit: 63206,
                        visual_elements: "emojis_bullets"
                    },
                    twitter: {
                        adaptations_needed: ["Extreme condensing", "Thread format", "Heavy hashtag usage"],
                        character_limit: 280,
                        visual_elements: "minimal_formatting"
                    }
                }
            }
        };
        
        // UPDATED: Streamlined Pain Points (6 categories max)
        this.painPointKeywords = {
            'Scale': [
                'scale', 'scaling', 'growth', 'expand', 'global', 'international',
                'volume', 'capacity', 'bottleneck', 'limitation', 'constraint'
            ],
            'Efficiency': [
                'efficiency', 'optimize', 'streamline', 'automate', 'waste',
                'manual', 'process', 'workflow', 'cost', 'budget', 'expensive'
            ],
            'Innovation': [
                'innovation', 'competitive', 'advantage', 'technology', 'ai', 'ml',
                'digital transformation', 'modern', 'upgrade', 'cutting-edge'
            ],
            'Quality': [
                'quality', 'consistency', 'reliability', 'error', 'bug', 'issue',
                'standard', 'compliance', 'accuracy', 'precision'
            ],
            'Speed': [
                'speed', 'fast', 'quick', 'time-to-market', 'deadline', 'urgent',
                'delay', 'slow', 'bottleneck', 'accelerate'
            ],
            'Risk': [
                'risk', 'security', 'compliance', 'audit', 'breach', 'vulnerability',
                'threat', 'safety', 'protection', 'mitigation'
            ]
        };

        // UPDATED: Role Level Detection (4 levels)
        this.roleLevelKeywords = {
            'C-Suite': ['ceo', 'cto', 'cfo', 'coo', 'chief', 'president', 'founder'],
            'VP-Director': ['vp', 'vice president', 'director', 'head of', 'lead'],
            'Manager': ['manager', 'team lead', 'supervisor', 'coordinator'],
            'Individual': ['engineer', 'developer', 'analyst', 'specialist', 'consultant']
        };

        // UPDATED: Function Area Detection (5 areas)
        this.functionAreaKeywords = {
            'Technology': [
                'engineering', 'development', 'technical', 'code', 'software',
                'infrastructure', 'devops', 'architecture', 'api'
            ],
            'Operations': [
                'operations', 'ops', 'process', 'workflow', 'project management',
                'business operations', 'efficiency', 'optimization'
            ],
            'Growth': [
                'marketing', 'sales', 'growth', 'acquisition', 'conversion',
                'revenue', 'business development', 'customer acquisition'
            ],
            'Strategy': [
                'strategy', 'planning', 'transformation', 'consulting', 'vision',
                'roadmap', 'objectives', 'goals'
            ],
            'Support': [
                'support', 'customer success', 'help', 'service', 'training',
                'onboarding', 'documentation'
            ]
        };

        // UPDATED: Industry Detection (6 industries)
        this.industryKeywords = {
            'Enterprise': [
                'enterprise', 'corporation', 'large company', 'fortune 500',
                'multinational', 'big business'
            ],
            'Mid-Market': [
                'mid-market', 'growing company', 'scale-up', 'expanding',
                '100 employees', '1000 employees'
            ],
            'SMB': [
                'small business', 'smb', 'startup', 'small team', 'entrepreneur',
                'bootstrap', 'early stage'
            ],
            'Technology': [
                'tech', 'software', 'saas', 'platform', 'digital', 'app',
                'technology company'
            ],
            'Services': [
                'consulting', 'agency', 'professional services', 'service provider',
                'advisory'
            ],
            'Manufacturing': [
                'manufacturing', 'production', 'factory', 'industrial',
                'supply chain', 'logistics'
            ]
        };

        // UPDATED: Content Interest Areas (5 areas)
        this.contentInterestKeywords = {
            'AI-ML': [
                'ai', 'artificial intelligence', 'machine learning', 'ml',
                'automation', 'intelligent', 'smart', 'neural'
            ],
            'Localization': [
                'localization', 'translation', 'international', 'global',
                'multilingual', 'cultural', 'regional'
            ],
            'Content-Ops': [
                'content management', 'cms', 'workflow', 'content operations',
                'publishing', 'editorial'
            ],
            'Platform': [
                'platform', 'integration', 'api', 'architecture', 'infrastructure',
                'system', 'technical'
            ],
            'Strategy': [
                'strategy', 'business planning', 'market expansion', 'growth strategy',
                'roadmap'
            ]
        };

        // Keep existing urgency keywords - they're fine
        this.urgencyKeywords = {
            'Critical': ['critical', 'urgent', 'emergency', 'breaking', 'crisis'],
            'High': ['important', 'priority', 'asap', 'quickly', 'deadline'],
            'Medium': ['should', 'need', 'required', 'improvement'],
            'Low': ['nice to have', 'eventually', 'consider', 'future']
        };
    }

    /**
     * UPDATED: Analyze email with new tag structure
     * Can accept optional subscriber data from signup form
     */
    async analyzeEmail(htmlContent, emailId = null, subscriberData = null) {
        const analysis = {
            id: emailId || this.generateId(),
            dublin_core: {
                created: new Date().toISOString(),
                modified: new Date().toISOString(),
                issued: null
            },
            workflow_status: "auto_generated",
            content_analysis: {},
            channel_format: { ...this.DEFAULT_CHANNEL_FORMAT },
            
            // UPDATED: New tag structure
            campaign_tags: {
                industry: null,           // Single value from 6 options
                role_level: null,         // Single value from 4 options  
                function_area: null,      // Single value from 5 options
                pain_points: [],          // 1-2 values max from 6 options
                content_interests: [],    // Multiple values from 5 options
                engagement_level: "New"   // System managed
            },
            
            // Keep existing structure but simplified
            target_audience: {
                company_size: "Unknown",
                urgency: "Medium"
            },
            
            content_elements: {
                headline: "",
                hook: "",
                primary_cta: "",
                secondary_cta: "",
                stats_featured: [],
                testimonial_theme: ""
            }
        };

        const textContent = this.extractTextFromHtml(htmlContent);
        const lowerText = textContent.toLowerCase();

        // Extract content elements
        analysis.content_elements = this.extractContentElements(htmlContent);
        analysis.title = analysis.content_elements.headline || "Untitled Email";
        analysis.description = this.generateDescription(textContent);

        // UPDATED: Apply new detection methods (with subscriber data override)
        if (subscriberData) {
            // Use subscriber form data when available
            analysis.campaign_tags.role_level = this.mapSubscriberRole(subscriberData.role);
            analysis.campaign_tags.function_area = this.mapSubscriberFunction(subscriberData.role);
            analysis.campaign_tags.pain_points = this.mapSubscriberPainPoints(subscriberData.role);
        } else {
            // Fallback to content detection
            analysis.campaign_tags.role_level = this.detectSingleCategory(lowerText, this.roleLevelKeywords);  
            analysis.campaign_tags.function_area = this.detectSingleCategory(lowerText, this.functionAreaKeywords);
            analysis.campaign_tags.pain_points = this.detectMultipleCategories(lowerText, this.painPointKeywords, 2);
        }
        
        // Always detect from content
        analysis.campaign_tags.industry = this.detectSingleCategory(lowerText, this.industryKeywords);
        analysis.campaign_tags.content_interests = this.detectMultipleCategories(lowerText, this.contentInterestKeywords, 3);
        
        // Keep existing urgency detection
        analysis.target_audience.urgency = this.detectUrgency(lowerText);
        
        // Simplified company size detection
        analysis.target_audience.company_size = this.detectCompanySize(lowerText);
        
        // Content analysis
        analysis.content_analysis = this.analyzeContentMetrics(htmlContent, textContent);

        return analysis;
    }

    /**
     * NEW: Detect single category (pick best match)
     */
    detectSingleCategory(text, categoryKeywords) {
        let bestMatch = { category: null, score: 0 };
        
        for (const [category, keywords] of Object.entries(categoryKeywords)) {
            const score = keywords.reduce((acc, keyword) => {
                const regex = new RegExp(keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                const matches = text.match(regex);
                return acc + (matches ? matches.length : 0);
            }, 0);
            
            if (score > bestMatch.score) {
                bestMatch = { category, score };
            }
        }
        
        return bestMatch.category;
    }

    /**
     * NEW: Detect multiple categories (up to maxResults)
     */
    detectMultipleCategories(text, categoryKeywords, maxResults = 3) {
        const matches = [];
        
        for (const [category, keywords] of Object.entries(categoryKeywords)) {
            const score = keywords.reduce((acc, keyword) => {
                const regex = new RegExp(keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                const keywordMatches = text.match(regex);
                return acc + (keywordMatches ? keywordMatches.length : 0);
            }, 0);
            
            if (score > 0) {
                matches.push({ category, score });
            }
        }
        
        return matches
            .sort((a, b) => b.score - a.score)
            .slice(0, maxResults)
            .map(m => m.category);
    }

    /**
     * NEW: Map subscriber form roles to our tag structure
     */
    mapSubscriberRole(formRole) {
        const roleMapping = {
            'Product Manager': 'Manager',
            'Engineer': 'Individual', 
            'Content Writer': 'Individual',
            'Designer': 'Individual',
            'Founder/Executive': 'C-Suite'
        };
        return roleMapping[formRole] || 'Individual';
    }

    mapSubscriberFunction(formRole) {
        const functionMapping = {
            'Product Manager': 'Strategy',
            'Engineer': 'Technology',
            'Content Writer': 'Growth', 
            'Designer': 'Growth',
            'Founder/Executive': 'Strategy'
        };
        return functionMapping[formRole] || 'Technology';
    }

    mapSubscriberPainPoints(formRole) {
        const painMapping = {
            'Product Manager': ['Scale', 'Innovation'],
            'Engineer': ['Quality', 'Speed'],
            'Content Writer': ['Efficiency', 'Quality'],
            'Designer': ['Efficiency', 'Innovation'],
            'Founder/Executive': ['Scale', 'Risk', 'Innovation']
        };
        return painMapping[formRole] || ['Efficiency'];
    }
    /**
     * UPDATED: Simplified company size detection
     */
    detectCompanySize(text) {
        if (/startup|small.?team|bootstrap|early.?stage/i.test(text)) {
            return "SMB";
        } else if (/enterprise|large.?company|corporation|fortune/i.test(text)) {
            return "Enterprise";
        } else if (/growing|scale|expanding|mid.?market/i.test(text)) {
            return "Mid-Market";
        }
        return "Unknown";
    }

    // Keep existing helper methods (extractTextFromHtml, extractContentElements, etc.)
    extractTextFromHtml(html) {
        let text = html.replace(/<script[^>]*>.*?<\/script>/gis, '');
        text = text.replace(/<style[^>]*>.*?<\/style>/gis, '');
        text = text.replace(/<[^>]*>/g, ' ');
        text = text.replace(/&nbsp;/g, ' ');
        text = text.replace(/&amp;/g, '&');
        text = text.replace(/&lt;/g, '<');
        text = text.replace(/&gt;/g, '>');
        text = text.replace(/&quot;/g, '"');
        text = text.replace(/\s+/g, ' ').trim();
        return text;
    }

    extractContentElements(html) {
        const elements = {
            headline: "",
            hook: "",
            primary_cta: "",
            secondary_cta: "",
            stats_featured: [],
            testimonial_theme: ""
        };

        const h1Match = html.match(/<h1[^>]*>(.*?)<\/h1>/i);
        if (h1Match) {
            elements.headline = this.extractTextFromHtml(h1Match[1]);
        }

        const heroMatch = html.match(/<div[^>]*class="[^"]*hero[^"]*"[^>]*>.*?<p[^>]*>(.*?)<\/p>/is);
        if (heroMatch) {
            elements.hook = this.extractTextFromHtml(heroMatch[1]);
        }

        const ctaMatches = html.match(/<a[^>]*class="[^"]*cta[^"]*"[^>]*>(.*?)<\/a>/gi) || [];
        if (ctaMatches.length > 0) {
            elements.primary_cta = this.extractTextFromHtml(ctaMatches[0]);
            if (ctaMatches.length > 1) {
                elements.secondary_cta = this.extractTextFromHtml(ctaMatches[1]);
            }
        }

        return elements;
    }

    detectUrgency(text) {
        let urgencyScore = { Critical: 0, High: 0, Medium: 0, Low: 0 };
        
        for (const [level, keywords] of Object.entries(this.urgencyKeywords)) {
            keywords.forEach(keyword => {
                const regex = new RegExp(keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                const matches = text.match(regex);
                urgencyScore[level] += matches ? matches.length : 0;
            });
        }
        
        const maxLevel = Object.keys(urgencyScore).reduce((a, b) => 
            urgencyScore[a] > urgencyScore[b] ? a : b
        );
        
        return urgencyScore[maxLevel] > 0 ? maxLevel : 'Medium';
    }

    analyzeContentMetrics(html, text) {
        return {
            word_count: text.split(/\s+/).length,
            html_size: html.length,
            has_images: /<img/i.test(html),
            has_cta_buttons: /<a[^>]*class="[^"]*cta[^"]*"/i.test(html),
            has_testimonials: /<div[^>]*class="[^"]*quote[^"]*"/i.test(html),
            has_statistics: /<span[^>]*class="[^"]*stat[^"]*"/i.test(html),
            mobile_responsive: /@media.*max-width/i.test(html),
            estimated_read_time: Math.ceil(text.split(/\s+/).length / 200)
        };
    }

    generateDescription(text) {
        const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 10);
        if (sentences.length > 0) {
            return sentences[0].trim().substring(0, 200) + "...";
        }
        return "Email campaign content";
    }

    generateId() {
        return 'email_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    async readFile(file) {
        if (typeof window !== 'undefined' && window.fs) {
            return await window.fs.readFile(file, { encoding: 'utf8' });
        } else if (typeof require !== 'undefined') {
            const fs = require('fs').promises;
            return await fs.readFile(file, 'utf8');
        } else {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => resolve(e.target.result);
                reader.onerror = reject;
                reader.readAsText(file);
            });
        }
    }

    exportToJson(analysis, filename = null) {
        const exportData = {
            ...analysis,
            export_metadata: {
                exported_at: new Date().toISOString(),
                schema_version: "2.0", // Updated for new tag structure
                analyzer_version: "2.0.0"
            }
        };

        if (typeof window !== 'undefined') {
            const blob = new Blob([JSON.stringify(exportData, null, 2)], {
                type: 'application/json'
            });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename || `email_analysis_${Date.now()}.json`;
            a.click();
            URL.revokeObjectURL(url);
        }

        return exportData;
    }

    /**
     * NEW: Batch analysis with updated summary structure
     */
    async analyzeBatch(emailFiles) {
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

        for (const file of emailFiles) {
            try {
                const htmlContent = typeof file === 'string' ? file : await this.readFile(file);
                const analysis = await this.analyzeEmail(htmlContent, file.name || null);
                results.campaigns.push(analysis);
                
                this.updateSummaryStats(results.summary, analysis);
                
            } catch (error) {
                console.error(`Error analyzing email ${file.name || 'unknown'}:`, error);
            }
        }

        results.summary.total_analyzed = results.campaigns.length;
        return results;
    }

    updateSummaryStats(summary, analysis) {
        const tags = analysis.campaign_tags;
        
        // Count single-value tags
        if (tags.industry) summary.industries[tags.industry] = (summary.industries[tags.industry] || 0) + 1;
        if (tags.role_level) summary.role_levels[tags.role_level] = (summary.role_levels[tags.role_level] || 0) + 1;
        if (tags.function_area) summary.function_areas[tags.function_area] = (summary.function_areas[tags.function_area] || 0) + 1;
        
        // Count multi-value tags
        tags.pain_points?.forEach(pain => {
            summary.pain_points[pain] = (summary.pain_points[pain] || 0) + 1;
        });
        
        tags.content_interests?.forEach(interest => {
            summary.content_interests[interest] = (summary.content_interests[interest] || 0) + 1;
        });
        
        // Count channels and formats
        summary.channels.email = (summary.channels.email || 0) + 1;
        summary.formats.html_email = (summary.formats.html_email || 0) + 1;
    }
}

// Export for different environments
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EmailCampaignAnalyzer;
} else if (typeof window !== 'undefined') {
    window.EmailCampaignAnalyzer = EmailCampaignAnalyzer;
}
