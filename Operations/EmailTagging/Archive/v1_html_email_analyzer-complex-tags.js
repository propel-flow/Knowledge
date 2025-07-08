/**
 * HTML Email Campaign Analyzer
 * Analyzes existing HTML email templates and applies standardized campaign tags
 * 
 * Usage:
 * const analyzer = new EmailCampaignAnalyzer();
 * const analysis = await analyzer.analyzeEmail(htmlContent, emailId);
 * 
 * Or analyze multiple emails:
 * const results = await analyzer.analyzeBatch(emailFiles);
 */

class EmailCampaignAnalyzer {
    constructor() {
        // Default channel format for email campaigns
        this.DEFAULT_CHANNEL_FORMAT = {
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
        
        this.painPointKeywords = {
            'Technical Debt': [
                'bug', 'error', '500', 'production', 'testing', 'test coverage', 
                'documentation', 'tech debt', 'refactor', 'legacy', 'integration',
                'api', 'sdk', 'deploy', 'deployment', 'monitoring', 'reliability',
                'uptime', 'downtime', 'incident', 'fire drill', 'outage'
            ],
            'Product Management': [
                'backlog', 'priorit', 'roadmap', 'stakeholder', 'feature', 
                'sprint', 'scrum', 'agile', 'requirement', 'epic', 'story',
                'pm', 'product manager', 'strategy', 'vision', 'goal',
                'metric', 'kpi', 'analytics', 'user story', 'acceptance criteria'
            ],
            'Revenue Leakage': [
                'revenue', 'payment', 'billing', 'subscription', 'churn',
                'fraud', 'abuse', 'gaming', 'multiple accounts', 'free tier',
                'upgrade', 'conversion', 'monetization', 'pricing', 'freemium',
                'validation', 'verification', 'account', 'user abuse'
            ],
            'AI Tools': [
                'ai', 'artificial intelligence', 'machine learning', 'ml',
                'automation', 'chatgpt', 'gpt', 'llm', 'neural', 'algorithm',
                'intelligent', 'smart', 'automated', 'bot', 'assistant',
                'prediction', 'recommendation', 'nlp', 'computer vision'
            ],
            'Startup Operations': [
                'startup', 'scale', 'scaling', 'growth', 'seed', 'series a',
                'funding', 'runway', 'burn rate', 'mvp', 'pivot', 'launch',
                'go-to-market', 'gtm', 'early stage', 'founder', 'bootstrap'
            ],
            'Team Management': [
                'team', 'hiring', 'onboard', 'remote', 'culture', 'communication',
                'collaboration', 'workflow', 'process', 'management', 'leadership',
                'burnout', 'productivity', 'efficiency', 'developer', 'engineer'
            ],
            'Security & Compliance': [
                'security', 'compliance', 'gdpr', 'hipaa', 'soc2', 'audit',
                'breach', 'vulnerability', 'encryption', 'authentication',
                'authorization', 'privacy', 'data protection', 'cyber',
                'penetration', 'threat', 'risk'
            ],
            'Customer Support': [
                'support', 'ticket', 'help desk', 'customer service', 'faq',
                'knowledge base', 'documentation', 'training', 'onboarding',
                'success', 'satisfaction', 'nps', 'feedback', 'complaint'
            ]
        };

        this.urgencyKeywords = {
            'Critical': ['critical', 'urgent', 'emergency', 'breaking', 'down', 'failed', 'crisis'],
            'High': ['important', 'priority', 'asap', 'quickly', 'soon', 'deadline', 'pressure'],
            'Medium': ['should', 'need', 'required', 'necessary', 'improvement'],
            'Low': ['nice to have', 'eventually', 'consider', 'future', 'maybe']
        };

        this.personaKeywords = {
            'Technical Founder': ['cto', 'technical founder', 'lead developer', 'architect', 'senior engineer'],
            'Product Manager': ['pm', 'product manager', 'product owner', 'product lead'],
            'Startup Founder': ['founder', 'ceo', 'entrepreneur', 'startup owner'],
            'Engineering Manager': ['engineering manager', 'dev manager', 'team lead', 'tech lead'],
            'Growth Manager': ['growth', 'marketing', 'acquisition', 'retention', 'conversion'],
            'Operations Manager': ['ops', 'operations', 'devops', 'infrastructure', 'systems']
        };

        this.solutionTypes = {
            'Automation': ['automat', 'ai', 'intelligent', 'smart', 'workflow'],
            'Monitoring': ['monitor', 'alert', 'track', 'observ', 'dashboard'],
            'Analytics': ['analyt', 'insight', 'data', 'report', 'metric'],
            'Integration': ['integrat', 'connect', 'api', 'sync', 'workflow'],
            'Security': ['secur', 'protect', 'encrypt', 'auth', 'compliance'],
            'Optimization': ['optim', 'improve', 'enhance', 'boost', 'increase']
        };
    }

    /**
     * Analyze a single HTML email and generate campaign metadata
     */
    async analyzeEmail(htmlContent, emailId = null) {
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
            campaign_tags: {
                industry: [],
                functional_area: [],
                pain_category: [],
                urgency: "Medium",
                solution_type: [],
                buying_stage: "Unknown",
                objections: []
            },
            target_audience: {
                primary_personas: [],
                company_size: "Unknown",
                stage: "Unknown",
                pain_level: "Unknown"
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

        // Extract text content from HTML
        const textContent = this.extractTextFromHtml(htmlContent);
        const lowerText = textContent.toLowerCase();

        // Analyze content elements
        analysis.content_elements = this.extractContentElements(htmlContent);
        analysis.title = analysis.content_elements.headline || "Untitled Email";
        analysis.description = this.generateDescription(textContent);

        // Detect pain points
        analysis.campaign_tags.pain_category = this.detectPainPoints(lowerText);
        
        // Detect urgency
        analysis.campaign_tags.urgency = this.detectUrgency(lowerText);
        
        // Detect personas
        analysis.target_audience.primary_personas = this.detectPersonas(lowerText);
        
        // Detect solution types
        analysis.campaign_tags.solution_type = this.detectSolutionTypes(lowerText);
        
        // Infer industry and functional areas
        analysis.campaign_tags.industry = this.inferIndustry(lowerText);
        analysis.campaign_tags.functional_area = this.inferFunctionalArea(lowerText);
        
        // Estimate company details
        analysis.target_audience = {
            ...analysis.target_audience,
            ...this.estimateCompanyDetails(lowerText)
        };
        
        // Detect buying stage
        analysis.campaign_tags.buying_stage = this.detectBuyingStage(lowerText);
        
        // Extract performance indicators
        analysis.content_analysis = this.analyzeContentMetrics(htmlContent, textContent);

        return analysis;
    }

    /**
     * Analyze multiple emails in batch
     */
    async analyzeBatch(emailFiles) {
        const results = {
            campaigns: [],
            summary: {
                total_analyzed: 0,
                pain_categories: {},
                personas: {},
                industries: {},
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
                
                // Update summary statistics
                this.updateSummaryStats(results.summary, analysis);
                
            } catch (error) {
                console.error(`Error analyzing email ${file.name || 'unknown'}:`, error);
            }
        }

        results.summary.total_analyzed = results.campaigns.length;
        return results;
    }

    /**
     * Extract plain text from HTML content
     */
    extractTextFromHtml(html) {
        // Remove script and style elements
        let text = html.replace(/<script[^>]*>.*?<\/script>/gis, '');
        text = text.replace(/<style[^>]*>.*?<\/style>/gis, '');
        
        // Remove HTML tags
        text = text.replace(/<[^>]*>/g, ' ');
        
        // Decode HTML entities
        text = text.replace(/&nbsp;/g, ' ');
        text = text.replace(/&amp;/g, '&');
        text = text.replace(/&lt;/g, '<');
        text = text.replace(/&gt;/g, '>');
        text = text.replace(/&quot;/g, '"');
        
        // Clean up whitespace
        text = text.replace(/\s+/g, ' ').trim();
        
        return text;
    }

    /**
     * Extract key content elements from HTML
     */
    extractContentElements(html) {
        const elements = {
            headline: "",
            hook: "",
            primary_cta: "",
            secondary_cta: "",
            stats_featured: [],
            testimonial_theme: ""
        };

        // Extract headlines (h1, h2 in hero sections or prominent divs)
        const h1Match = html.match(/<h1[^>]*>(.*?)<\/h1>/i);
        if (h1Match) {
            elements.headline = this.extractTextFromHtml(h1Match[1]);
        }

        // Extract hero paragraph (often the hook)
        const heroMatch = html.match(/<div[^>]*class="[^"]*hero[^"]*"[^>]*>.*?<p[^>]*>(.*?)<\/p>/is);
        if (heroMatch) {
            elements.hook = this.extractTextFromHtml(heroMatch[1]);
        }

        // Extract CTAs
        const ctaMatches = html.match(/<a[^>]*class="[^"]*cta[^"]*"[^>]*>(.*?)<\/a>/gi) || [];
        if (ctaMatches.length > 0) {
            elements.primary_cta = this.extractTextFromHtml(ctaMatches[0]);
            if (ctaMatches.length > 1) {
                elements.secondary_cta = this.extractTextFromHtml(ctaMatches[1]);
            }
        }

        // Extract statistics
        const statMatches = html.match(/<span[^>]*class="[^"]*stat-number[^"]*"[^>]*>(.*?)<\/span>/gi) || [];
        elements.stats_featured = statMatches.map(match => this.extractTextFromHtml(match));

        // Extract testimonial themes
        const testimonialMatch = html.match(/<div[^>]*class="[^"]*quote[^"]*"[^>]*>.*?<div[^>]*class="[^"]*quote-text[^"]*"[^>]*>(.*?)<\/div>/is);
        if (testimonialMatch) {
            elements.testimonial_theme = this.extractTextFromHtml(testimonialMatch[1]);
        }

        return elements;
    }

    /**
     * Detect pain points based on keyword analysis
     */
    detectPainPoints(text) {
        const detectedPains = [];
        
        for (const [painCategory, keywords] of Object.entries(this.painPointKeywords)) {
            const score = keywords.reduce((acc, keyword) => {
                const regex = new RegExp(keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                const matches = text.match(regex);
                return acc + (matches ? matches.length : 0);
            }, 0);
            
            if (score > 0) {
                detectedPains.push({
                    category: painCategory,
                    confidence: Math.min(score / keywords.length, 1.0),
                    keyword_matches: score
                });
            }
        }
        
        return detectedPains
            .sort((a, b) => b.confidence - a.confidence)
            .slice(0, 3)
            .map(p => p.category);
    }

    /**
     * Detect urgency level
     */
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

    /**
     * Detect target personas
     */
    detectPersonas(text) {
        const detectedPersonas = [];
        
        for (const [persona, keywords] of Object.entries(this.personaKeywords)) {
            const score = keywords.reduce((acc, keyword) => {
                const regex = new RegExp(keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                const matches = text.match(regex);
                return acc + (matches ? matches.length : 0);
            }, 0);
            
            if (score > 0) {
                detectedPersonas.push(persona);
            }
        }
        
        return detectedPersonas.length > 0 ? detectedPersonas : ['Unknown'];
    }

    /**
     * Detect solution types
     */
    detectSolutionTypes(text) {
        const detectedSolutions = [];
        
        for (const [solution, keywords] of Object.entries(this.solutionTypes)) {
            const score = keywords.reduce((acc, keyword) => {
                const regex = new RegExp(keyword, 'gi');
                const matches = text.match(regex);
                return acc + (matches ? matches.length : 0);
            }, 0);
            
            if (score > 0) {
                detectedSolutions.push(solution);
            }
        }
        
        return detectedSolutions;
    }

    /**
     * Infer industry based on content
     */
    inferIndustry(text) {
        const industries = [];
        
        if (/saas|software as a service|b2b|enterprise/i.test(text)) {
            industries.push('SaaS');
        }
        if (/fintech|financial|banking|payment/i.test(text)) {
            industries.push('FinTech');
        }
        if (/healthtech|health|medical|hipaa/i.test(text)) {
            industries.push('HealthTech');
        }
        if (/edtech|education|learning|student/i.test(text)) {
            industries.push('EdTech');
        }
        if (/startup|early.?stage|seed|series/i.test(text)) {
            industries.push('Startup');
        }
        if (/enterprise|corporation|large.?company/i.test(text)) {
            industries.push('Enterprise');
        }
        
        return industries.length > 0 ? industries : ['Technology'];
    }

    /**
     * Infer functional area
     */
    inferFunctionalArea(text) {
        const areas = [];
        
        if (/engineering|development|technical|code/i.test(text)) {
            areas.push('Engineering');
        }
        if (/product|pm|roadmap|feature/i.test(text)) {
            areas.push('Product Management');
        }
        if (/marketing|growth|acquisition/i.test(text)) {
            areas.push('Marketing');
        }
        if (/sales|revenue|conversion/i.test(text)) {
            areas.push('Sales');
        }
        if (/operations|ops|infrastructure/i.test(text)) {
            areas.push('Operations');
        }
        if (/support|customer.?success|help/i.test(text)) {
            areas.push('Customer Success');
        }
        
        return areas.length > 0 ? areas : ['General'];
    }

    /**
     * Estimate company details
     */
    estimateCompanyDetails(text) {
        let companySize = "Unknown";
        let stage = "Unknown";
        let painLevel = "Medium";
        
        // Company size estimation
        if (/startup|small.?team|6.?person|early/i.test(text)) {
            companySize = "5-50 employees";
        } else if (/mid.?size|growing|scale/i.test(text)) {
            companySize = "50-200 employees";
        } else if (/enterprise|large|corporation/i.test(text)) {
            companySize = "200+ employees";
        }
        
        // Stage estimation
        if (/seed|pre.?seed|bootstrap/i.test(text)) {
            stage = "Seed";
        } else if (/series.?a|early.?stage/i.test(text)) {
            stage = "Series A";
        } else if (/series.?b|growth/i.test(text)) {
            stage = "Series B+";
        }
        
        // Pain level estimation
        if (/critical|urgent|emergency|breaking|crisis/i.test(text)) {
            painLevel = "Critical";
        } else if (/important|priority|problem|issue|challenge/i.test(text)) {
            painLevel = "High";
        } else if (/improve|optimize|enhance|better/i.test(text)) {
            painLevel = "Medium";
        }
        
        return { company_size: companySize, stage, pain_level: painLevel };
    }

    /**
     * Detect buying stage
     */
    detectBuyingStage(text) {
        if (/compare|vs|alternative|competitor/i.test(text)) {
            return "Solution Aware";
        } else if (/problem|challenge|issue|pain|struggle/i.test(text)) {
            return "Problem Aware";
        } else if (/solution|tool|platform|service/i.test(text)) {
            return "Solution Aware";
        } else if (/buy|purchase|pricing|cost|demo/i.test(text)) {
            return "Purchase Ready";
        }
        return "Unaware";
    }

    /**
     * Analyze content metrics
     */
    analyzeContentMetrics(html, text) {
        return {
            word_count: text.split(/\s+/).length,
            html_size: html.length,
            has_images: /<img/i.test(html),
            has_cta_buttons: /<a[^>]*class="[^"]*cta[^"]*"/i.test(html),
            has_testimonials: /<div[^>]*class="[^"]*quote[^"]*"/i.test(html),
            has_statistics: /<span[^>]*class="[^"]*stat[^"]*"/i.test(html),
            mobile_responsive: /@media.*max-width/i.test(html),
            estimated_read_time: Math.ceil(text.split(/\s+/).length / 200) // 200 words per minute
        };
    }

    /**
     * Generate a description from content
     */
    generateDescription(text) {
        const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 10);
        if (sentences.length > 0) {
            return sentences[0].trim().substring(0, 200) + "...";
        }
        return "Email campaign content";
    }

    /**
     * Update summary statistics
     */
    updateSummaryStats(summary, analysis) {
        // Count pain categories
        analysis.campaign_tags.pain_category.forEach(pain => {
            summary.pain_categories[pain] = (summary.pain_categories[pain] || 0) + 1;
        });
        
        // Count personas
        analysis.target_audience.primary_personas.forEach(persona => {
            summary.personas[persona] = (summary.personas[persona] || 0) + 1;
        });
        
        // Count industries
        analysis.campaign_tags.industry.forEach(industry => {
            summary.industries[industry] = (summary.industries[industry] || 0) + 1;
        });
        
        // Count channels and formats
        if (analysis.channel_format) {
            const channel = analysis.channel_format.end_channel || 'email';
            const format = analysis.channel_format.content_format || 'html_email';
            
            summary.channels[channel] = (summary.channels[channel] || 0) + 1;
            summary.formats[format] = (summary.formats[format] || 0) + 1;
        }
    }

    /**
     * Generate unique ID
     */
    generateId() {
        return 'email_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    /**
     * Read file content (for Node.js environments)
     */
    async readFile(file) {
        if (typeof window !== 'undefined' && window.fs) {
            // Browser environment with fs API
            return await window.fs.readFile(file, { encoding: 'utf8' });
        } else if (typeof require !== 'undefined') {
            // Node.js environment
            const fs = require('fs').promises;
            return await fs.readFile(file, 'utf8');
        } else {
            // File object from input
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => resolve(e.target.result);
                reader.onerror = reject;
                reader.readAsText(file);
            });
        }
    }

    /**
     * Export analysis results to JSON
     */
    exportToJson(analysis, filename = null) {
        const exportData = {
            ...analysis,
            export_metadata: {
                exported_at: new Date().toISOString(),
                schema_version: "1.0",
                analyzer_version: "1.1.0" // Updated version with channel_format support
            }
        };

        if (typeof window !== 'undefined') {
            // Browser download
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
}

// Usage examples:
/*

// Browser usage:
const analyzer = new EmailCampaignAnalyzer();

// Analyze single email
document.getElementById('htmlInput').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    const analysis = await analyzer.analyzeEmail(await file.text(), file.name);
    console.log(analysis);
    analyzer.exportToJson(analysis);
});

// Analyze multiple emails
document.getElementById('batchInput').addEventListener('change', async (e) => {
    const files = Array.from(e.target.files);
    const results = await analyzer.analyzeBatch(files);
    console.log(results);
    analyzer.exportToJson(results, 'batch_analysis.json');
});

// Node.js usage:
const fs = require('fs');
const analyzer = new EmailCampaignAnalyzer();

(async () => {
    const htmlContent = fs.readFileSync('email.html', 'utf8');
    const analysis = await analyzer.analyzeEmail(htmlContent, 'my_email');
    
    fs.writeFileSync('analysis.json', JSON.stringify(analysis, null, 2));
    console.log('Analysis complete!');
})();

*/

// Export for different environments
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EmailCampaignAnalyzer;
} else if (typeof window !== 'undefined') {
    window.EmailCampaignAnalyzer = EmailCampaignAnalyzer;
}
