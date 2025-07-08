# Local Download Version of Your Enhanced Code

Absolutely! Here's your code modified to work entirely locally without AWS dependency:

## Modified main.py (Local Version)

```python
import os
import json
from jira import JIRA
from datetime import datetime
import openai
from typing import Dict, List, Optional
from pathlib import Path

# === Enhanced CONFIG ===
JIRA_SERVER = os.environ["JIRA_SERVER"]
JIRA_EMAIL = os.environ["JIRA_EMAIL"] 
JIRA_PAT = os.environ["JIRA_PAT"]

# Add OpenAI for testing AI processing
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# Local output configuration
OUTPUT_FOLDER = "jira_md_output"
BACKUP_FOLDER = "jira_backups"

# === Setup Clients ===
jira = JIRA(server=JIRA_SERVER, token_auth=JIRA_PAT)

# === Create Output Folders ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)

# === Enhanced JQL Queries ===
queries = {
    # Your existing queries
    "extreme_defects_with_code_changes": (
        'project = "Extreme Cloud Platform" AND "Target Version/s" in ("XCP 25.1.0", "XCP 24.6", "XCP 24.5", "XCP 25.2.0") '
        'AND resolution = "Resolved With Code" AND "Release Notes Required" = Yes'
    ),
    "workspace_release_notes": (
        'project = Workspace AND type in (Epic, Story) AND "Target Version" = "WS 25.1.0" '
        'AND resolution = Done AND "Release Notes Required" = Yes'
    ),
    
    # New test queries for your plugin development
    "defects_cwc_test": (
        'issuetype in (Bug, Defect) AND status in (Closed, Resolved) '
        'AND resolution in (Fixed, Done) AND priority in (High, Highest) '
        'ORDER BY priority DESC, key ASC'
    ),
    "defects_cwoc_test": (
        'issuetype in (Bug, Defect) AND status = Closed '
        'AND resolution in ("Won\'t Fix", Duplicate, "Cannot Reproduce") '
        'ORDER BY key ASC'
    ),
    "open_defects_test": (
        'issuetype in (Bug, Defect) AND status not in (Closed, Resolved, Done) '
        'AND priority in (High, Highest, Critical) '
        'ORDER BY priority DESC, created ASC'
    ),
    "platform_epics_test": (
        'issuetype = Epic AND (summary ~ "Introduction.*" OR summary ~ "Prerequisites.*" '
        'OR summary ~ "Supported Applications.*" OR summary ~ "Features.*")'
    )
}

# === AI Processing Functions ===
def extract_symptom_with_ai(issue) -> Optional[str]:
    """Extract customer-facing symptom using AI"""
    if not OPENAI_API_KEY:
        return None
        
    prompt = f"""
    Extract a concise symptom description for release notes:
    
    Summary: {issue.fields.summary}
    Description: {issue.fields.description or 'No description'}
    
    Requirements:
    - 1-2 sentences maximum
    - Customer-facing language
    - Focus on what the user observes
    
    Symptom:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error for {issue.key}: {e}")
        return None

def extract_condition_with_ai(issue) -> Optional[str]:
    """Extract condition when issue occurs using AI"""
    if not OPENAI_API_KEY:
        return None
        
    prompt = f"""
    Extract the specific condition when this issue occurs:
    
    Summary: {issue.fields.summary}
    Description: {issue.fields.description or 'No description'}
    
    Requirements:
    - Explain when/how the issue happens
    - Must be different from the symptom
    - Customer-facing language
    
    Condition:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error for {issue.key}: {e}")
        return None

def classify_issue_with_ai(issue) -> str:
    """Classify issue for documentation category"""
    if not OPENAI_API_KEY:
        return "unknown"
        
    prompt = f"""
    Classify this Jira issue for release notes:
    
    Issue Type: {issue.fields.issuetype.name}
    Status: {issue.fields.status.name}
    Resolution: {getattr(issue.fields.resolution, 'name', 'Unresolved')}
    Priority: {getattr(issue.fields.priority, 'name', 'Unknown')}
    Summary: {issue.fields.summary}
    
    Categories: defect-cwc, defect-cwoc, open-defect, enhancement, known-issue, exclude
    
    Category:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.1
        )
        return response.choices[0].message.content.strip().lower()
    except Exception as e:
        print(f"AI Classification Error for {issue.key}: {e}")
        return "unknown"

# === Enhanced Issue Processing ===
def process_issue_with_ai(issue) -> Dict:
    """Process issue with AI enhancements - this is your core plugin logic"""
    
    # Basic issue info (your existing approach)
    basic_info = {
        "key": issue.key,
        "summary": issue.fields.summary,
        "status": issue.fields.status.name,
        "type": issue.fields.issuetype.name,
        "priority": getattr(issue.fields.priority, 'name', 'Unknown'),
        "resolution": getattr(issue.fields.resolution, 'name', 'Unresolved'),
        "description": issue.fields.description or "No description provided",
        "created": str(issue.fields.created),
        "updated": str(issue.fields.updated),
        "assignee": issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned"
    }
    
    # AI-enhanced content (new capabilities)
    ai_content = {}
    if OPENAI_API_KEY:
        print(f"  Processing {issue.key} with AI...")
        symptom = extract_symptom_with_ai(issue)
        condition = extract_condition_with_ai(issue)
        category = classify_issue_with_ai(issue)
        
        ai_content = {
            "symptom": symptom,
            "condition": condition,
            "category": category,
            "confidence": calculate_confidence(basic_info, {"symptom": symptom, "condition": condition})
        }
    
    return {**basic_info, "ai_analysis": ai_content}

def calculate_confidence(basic_info: Dict, ai_content: Dict) -> float:
    """Calculate confidence score for AI-generated content"""
    score = 0.5  # Base score
    
    # Boost for good description
    if basic_info.get("description") and len(basic_info["description"]) > 50:
        score += 0.2
    
    # Boost for clear summary  
    if len(basic_info.get("summary", "")) > 20:
        score += 0.1
        
    # Boost for different symptom/condition
    symptom = ai_content.get("symptom", "")
    condition = ai_content.get("condition", "")
    if symptom and condition and symptom != condition:
        score += 0.2
        
    return min(score, 1.0)

# === Enhanced Markdown Generation ===
def issue_to_enhanced_markdown(issue_data: Dict) -> str:
    """Generate enhanced markdown with AI content"""
    
    md = f"""# {issue_data['key']} - {issue_data['summary']}

**Status**: {issue_data['status']}  
**Type**: {issue_data['type']}  
**Priority**: {issue_data['priority']}  
**Resolution**: {issue_data['resolution']}  
**Assignee**: {issue_data['assignee']}  

## Original Description
{issue_data['description']}

"""
    
    # Add AI analysis if available
    ai_analysis = issue_data.get("ai_analysis", {})
    if ai_analysis:
        md += f"""## AI-Generated Release Notes Content

**Category**: {ai_analysis.get('category', 'Unknown')}  
**Confidence**: {ai_analysis.get('confidence', 0):.2f}  

### Symptom
{ai_analysis.get('symptom', 'Not generated')}  

### Condition  
{ai_analysis.get('condition', 'Not generated')}  

### Release Notes Quality Check
- Symptom ≠ Condition: {'✓' if ai_analysis.get('symptom') != ai_analysis.get('condition') else '✗'}
- Has Workaround Info: {'✓' if 'workaround' in issue_data['description'].lower() else '✗'}
- Customer Impact: {issue_data['priority']}

"""
    
    md += f"""## Metadata
- **Created**: {issue_data['created']}
- **Updated**: {issue_data['updated']}
- **Key**: {issue_data['key']}
- **Direct Link**: {os.environ['JIRA_SERVER']}/browse/{issue_data['key']}
"""
    
    return md

# === Local File Management ===
def save_raw_data_backup(query_tag: str, issues: List) -> str:
    """Save raw Jira data as JSON backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_FOLDER, f"{query_tag}_{timestamp}.json")
    
    # Convert issues to serializable format
    backup_data = []
    for issue in issues:
        backup_data.append({
            "key": issue.key,
            "raw": issue.raw,
            "fields": {
                "summary": issue.fields.summary,
                "description": issue.fields.description,
                "status": issue.fields.status.name,
                "priority": getattr(issue.fields.priority, 'name', None),
                "resolution": getattr(issue.fields.resolution, 'name', None),
                "issuetype": issue.fields.issuetype.name,
                "created": str(issue.fields.created),
                "updated": str(issue.fields.updated)
            }
        })
    
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(backup_data, f, indent=2, default=str)
    
    return backup_file

def generate_summary_report(all_results: Dict) -> str:
    """Generate a summary report of all processing"""
    
    report = f"""# Jira Documentation Processing Summary
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Processing Overview
"""
    
    total_issues = 0
    ai_processed = 0
    
    for query_tag, results in all_results.items():
        count = len(results)
        ai_count = sum(1 for r in results if r.get("ai_analysis", {}).get("symptom"))
        total_issues += count
        ai_processed += ai_count
        
        report += f"""
### {query_tag.replace('_', ' ').title()}
- **Issues Found**: {count}
- **AI Processed**: {ai_count}
- **Success Rate**: {(ai_count/count*100) if count > 0 else 0:.1f}%
"""
    
    report += f"""
## Overall Statistics
- **Total Issues**: {total_issues}
- **AI Processing Success**: {ai_processed}/{total_issues} ({(ai_processed/total_issues*100) if total_issues > 0 else 0:.1f}%)
- **Average Confidence**: {sum(r.get('ai_analysis', {}).get('confidence', 0) for results in all_results.values() for r in results if r.get('ai_analysis', {}).get('confidence')) / max(ai_processed, 1):.2f}

## Quality Metrics
"""
    
    # Quality analysis
    symptom_condition_different = 0
    high_confidence = 0
    
    for results in all_results.values():
        for result in results:
            ai = result.get("ai_analysis", {})
            if ai.get("symptom") and ai.get("condition"):
                if ai["symptom"] != ai["condition"]:
                    symptom_condition_different += 1
                if ai.get("confidence", 0) > 0.7:
                    high_confidence += 1
    
    report += f"""
- **Symptom ≠ Condition**: {symptom_condition_different}/{ai_processed} ({(symptom_condition_different/max(ai_processed,1)*100):.1f}%)
- **High Confidence (>0.7)**: {high_confidence}/{ai_processed} ({(high_confidence/max(ai_processed,1)*100):.1f}%)

## Next Steps for Plugin Development
1. Review generated content in `{OUTPUT_FOLDER}/`
2. Check quality of AI categorization
3. Validate JQL queries against your requirements
4. Test with different issue types and priorities

## Files Generated
"""
    
    for query_tag in all_results.keys():
        report += f"- `{OUTPUT_FOLDER}/{query_tag}/` - Individual issue markdown files\n"
    
    report += f"- `{BACKUP_FOLDER}/` - Raw JSON backups\n"
    report += f"- `{OUTPUT_FOLDER}/processing_summary.json` - Detailed results\n"
    
    return report

# === Main Processing Loop ===
def main():
    """Enhanced main function with local processing"""
    
    print(f"{'='*60}")
    print("JIRA DOCUMENTATION INTELLIGENCE - LOCAL TESTING")
    print(f"{'='*60}")
    print(f"Output folder: {OUTPUT_FOLDER}")
    print(f"Backup folder: {BACKUP_FOLDER}")
    print(f"OpenAI enabled: {'Yes' if OPENAI_API_KEY else 'No'}")
    print(f"{'='*60}")
    
    all_results = {}
    
    for tag, jql in queries.items():
        print(f"\n{'='*50}")
        print(f"Query: {tag}")
        print(f"JQL: {jql[:100]}{'...' if len(jql) > 100 else ''}")
        print(f"{'='*50}")
        
        # Create directory for each query
        query_folder = os.path.join(OUTPUT_FOLDER, tag)
        os.makedirs(query_folder, exist_ok=True)
        
        try:
            # Fetch issues
            print("Fetching issues from Jira...")
            issues = jira.search_issues(jql, maxResults=20, fields="*all")
            print(f"Found {len(issues)} issues")
            
            if issues:
                # Save raw backup
                backup_file = save_raw_data_backup(tag, issues)
                print(f"Raw data backed up to: {backup_file}")
                
                query_results = []
                
                for i, issue in enumerate(issues, 1):
                    print(f"Processing {i}/{len(issues)}: {issue.key}")
                    
                    # Process with AI (your future plugin logic)
                    issue_data = process_issue_with_ai(issue)
                    query_results.append(issue_data)
                    
                    # Generate enhanced markdown
                    markdown_content = issue_to_enhanced_markdown(issue_data)
                    
                    # Save locally
                    filename = f"{issue.key}.md"
                    local_path = os.path.join(query_folder, filename)
                    with open(local_path, "w", encoding="utf-8") as f:
                        f.write(markdown_content)
                    
                    print(f"  ✓ Saved: {filename}")
                
                all_results[tag] = query_results
                print(f"✓ Completed {tag}: {len(query_results)} issues processed")
            else:
                print("No issues found for this query")
                all_results[tag] = []
                
        except Exception as e:
            print(f"✗ Error processing {tag}: {e}")
            all_results[tag] = []
    
    # Save summary results
    summary_path = os.path.join(OUTPUT_FOLDER, "processing_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, default=str)
    
    # Generate and save summary report
    summary_report = generate_summary_report(all_results)
    report_path = os.path.join(OUTPUT_FOLDER, "SUMMARY_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(summary_report)
    
    print(f"\n{'='*60}")
    print("🎉 PROCESSING COMPLETE!")
    print(f"{'='*60}")
    print(f"📁 Results: {OUTPUT_FOLDER}/")
    print(f"📄 Summary: {report_path}")
    print(f"💾 Backups: {BACKUP_FOLDER}/")
    print(f"📊 Total Issues: {sum(len(results) for results in all_results.values())}")
    print(f"🤖 AI Processing: {'Enabled' if OPENAI_API_KEY else 'Disabled (add OPENAI_API_KEY)'}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
```

## Updated requirements.txt

```txt
jira==3.5.0
openai==1.3.0
python-dotenv==1.0.0
requests==2.31.0
```

## Updated .env file

```bash
# Your existing Jira config
JIRA_SERVER=https://your-company.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_PAT=your_api_token

# Add OpenAI for AI processing (optional)
OPENAI_API_KEY=your_openai_api_key

# Remove AWS variables (not needed for local)
# AWS_ACCESS_KEY_ID=...
# AWS_SECRET_ACCESS_KEY=...
```

## Local Folder Structure After Running

```
your-project/
├── main.py
├── requirements.txt
├── .env
├── jira_md_output/           # All generated content
│   ├── extreme_defects_with_code_changes/
│   │   ├── XCP-1234.md
│   │   └── XCP-5678.md
│   ├── defects_cwc_test/
│   ├── open_defects_test/
│   ├── processing_summary.json
│   └── SUMMARY_REPORT.md     # Overview of everything
├── jira_backups/             # Raw JSON backups
│   ├── extreme_defects_20241215_143022.json
│   └── defects_cwc_test_20241215_143045.json
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your Jira credentials

# Run processing
python main.py

# Check results
ls jira_md_output/
cat jira_md_output/SUMMARY_REPORT.md
```

## What You Get Locally

✅ **All Jira Data**: Downloaded and processed locally  
✅ **AI Analysis**: If OpenAI key provided, enhanced content generation  
✅ **Markdown Files**: Individual files for each issue  
✅ **JSON Backups**: Raw Jira data preserved  
✅ **Summary Report**: Overall processing statistics  
✅ **Quality Metrics**: Validation of AI-generated content  
✅ **No AWS Dependency**: Everything stored locally

This gives you the same capabilities as the AWS version but keeps everything on your local machine for development and testing!