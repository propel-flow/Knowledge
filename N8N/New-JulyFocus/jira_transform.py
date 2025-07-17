import json
import csv
from datetime import datetime

def transform_to_jira_format(input_file, output_type="api"):
    """
    Transform the project JSONs to Jira-compatible format
    Split by teams: A, B, C, D (no leads)
    Add placeholder fields for intern ownership
    """
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    teams = {
        "A": {"name": "A - Jira Development", "email": "team-a@company.com", "members": 2},
        "B": {"name": "B - CMS Research", "email": "team-b@company.com", "members": 1}, 
        "C": {"name": "C - Outreach", "email": "team-c@company.com", "members": 2},
        "D": {"name": "D - Analytics", "email": "team-d@company.com", "members": 1}
    }
    
    def get_team_from_assignee(assignee):
        """Extract team letter from assignee field"""
        if "Team A" in assignee or "A -" in assignee:
            return "A"
        elif "Team B" in assignee or "B -" in assignee:
            return "B"
        elif "Team C" in assignee or "C -" in assignee:
            return "C"
        elif "Team D" in assignee or "D -" in assignee:
            return "D"
        return "A"  # default
    
    def create_jira_issue(item, issue_type, epic_key=None, parent_key=None):
        """Create a Jira-compatible issue object"""
        team = get_team_from_assignee(item.get('assignee', ''))
        
        # Base issue structure
        issue = {
            "fields": {
                "project": {"key": "N8N"},
                "summary": item['summary'],
                "description": create_description(item, team),
                "issuetype": {"name": issue_type},
                "priority": {"name": item.get('priority', 'Medium')},
                "labels": item.get('labels', []) + [f"team-{team.lower()}", "CHANGE_TO_YOUR_NAME"],
                
                # Team email assignment (shared account)
                "assignee": {"name": teams[team]["email"]},  # Team shared email
                "customfield_10001": "Add your name when taking ownership (e.g., 'Working on this - Sarah')",  # Custom text field
                
                # Story points if available
                "customfield_10016": item.get('storyPoints', 0),  # Story Points field
                
                # Team assignment
                "customfield_10002": teams[team]["name"],  # Team assignment field
            }
        }
        
        # Add epic link if this is a story
        if epic_key and issue_type == "Story":
            issue["fields"]["customfield_10014"] = epic_key  # Epic Link field
            
        # Add parent link if this is a task/subtask
        if parent_key and issue_type in ["Task", "Sub-task"]:
            issue["fields"]["parent"] = {"key": parent_key}
            issue["fields"]["issuetype"] = {"name": "Sub-task"}
        
        return issue
    
    def create_description(item, team):
        """Create enhanced description with ownership instructions"""
        base_desc = item.get('description', '')
        
        ownership_section = f"""
## 🔥 ACTION REQUIRED 🔥

**WHEN YOU TAKE THIS TICKET:**
1. Remove the "CHANGE_TO_YOUR_NAME" label
2. Add your name label: `member-yourname` (e.g., `member-sarah`)
3. Update "Working On" field: Add your full name
4. Add comment: "Taking this - [Your Name]"

**Team**: {teams[team]["name"]} ({teams[team]["email"]})
**Story Points**: {item.get('storyPoints', 'TBD')}

---

{base_desc}
"""
        
        # Add technical notes if available
        if 'technicalNotes' in item:
            ownership_section += f"\n\n**Technical Notes**: {item['technicalNotes']}"
            
        # Add acceptance criteria if available
        if 'acceptanceCriteria' in item:
            criteria = '\n'.join([f"- {criteria}" for criteria in item['acceptanceCriteria']])
            ownership_section += f"\n\n**Acceptance Criteria**:\n{criteria}"
            
        return ownership_section
    
    # Transform data by teams
    team_issues = {"A": [], "B": [], "C": [], "D": []}
    epic_keys = {}  # Store epic keys for linking
    story_keys = {}  # Store story keys for linking tasks
    
    # First pass: Create epics
    if 'epics' in data:
        for i, epic in enumerate(data['epics']):
            team = get_team_from_assignee(epic.get('team', ''))
            epic_key = f"N8N-{i+1}"
            epic_keys[epic['summary']] = epic_key
            
            epic_issue = create_jira_issue(epic, "Epic")
            epic_issue["key"] = epic_key  # Pre-assign key for reference
            team_issues[team].append(epic_issue)
    
    # Second pass: Create stories
    if 'stories' in data:
        for i, story in enumerate(data['stories']):
            team = get_team_from_assignee(story.get('assignee', ''))
            story_key = f"N8N-{len(data.get('epics', [])) + i + 1}"
            story_keys[story['summary']] = story_key
            
            # Find epic key
            epic_key = epic_keys.get(story.get('epic', ''))
            
            story_issue = create_jira_issue(story, "Story", epic_key)
            story_issue["key"] = story_key
            team_issues[team].append(story_issue)
    
    # Third pass: Create tasks
    if 'tasks' in data:
        for i, task in enumerate(data['tasks']):
            # Find team from parent story
            parent_story = next((s for s in data.get('stories', []) if s['summary'] == task.get('parent', '')), None)
            team = get_team_from_assignee(parent_story.get('assignee', '')) if parent_story else 'A'
            
            parent_key = story_keys.get(task.get('parent', ''))
            task_issue = create_jira_issue(task, "Task", parent_key=parent_key)
            team_issues[team].append(task_issue)
    
    return team_issues

def save_team_files(team_issues, output_format="api"):
    """Save separate files for each team"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
    for team, issues in team_issues.items():
        if not issues:  # Skip empty teams
            continue
            
        if output_format == "api":
            # Save as JSON for API import
            filename = f"team_{team}_jira_import_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump({"issues": issues}, f, indent=2)
                
        elif output_format == "csv":
            # Save as CSV for manual import
            filename = f"team_{team}_jira_import_{timestamp}.csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # CSV Headers
                writer.writerow([
                    'Summary', 'Issue Type', 'Priority', 'Assignee', 'Description', 
                    'Labels', 'Story Points', 'Epic Link', 'Team', 'Working On'
                ])
                
                # Write issues
                for issue in issues:
                    fields = issue['fields']
                    writer.writerow([
                        fields['summary'],
                        fields['issuetype']['name'],
                        fields['priority']['name'], 
                        fields['assignee']['name'],
                        fields['description'],
                        ';'.join(fields['labels']),
                        fields.get('customfield_10016', 0),
                        fields.get('customfield_10014', ''),
                        fields.get('customfield_10002', ''),
                        fields.get('customfield_10001', '')
                    ])
        
        print(f"✅ Created {filename} with {len(issues)} issues")

# Example usage
if __name__ == "__main__":
    # Transform both JSON files
    files_to_process = [
        "pain_point_jira_tickets.json",
        "jira_import_plan1+2_v2.json"
    ]
    
    all_team_issues = {"A": [], "B": [], "C": [], "D": []}
    
    for file in files_to_process:
        try:
            team_issues = transform_to_jira_format(file)
            
            # Merge issues from both files
            for team in all_team_issues:
                all_team_issues[team].extend(team_issues[team])
                
            print(f"✅ Processed {file}")
        except FileNotFoundError:
            print(f"❌ File {file} not found")
    
    # Save combined results
    print("\n🚀 Saving team files...")
    save_team_files(all_team_issues, "api")    # JSON for API
    save_team_files(all_team_issues, "csv")    # CSV for manual import
    
    # Print summary
    print(f"\n📊 SUMMARY:")
    for team, issues in all_team_issues.items():
        print(f"Team {team}: {len(issues)} issues")
    
    print(f"\n🔥 TEAM MEMBER INSTRUCTIONS:")
    print("1. Each team gets their own Jira instance (free tier)")
    print("2. Import your team's JSON/CSV file") 
    print("3. When taking a ticket:")
    print("   - Assignee: Already set to team email (don't change)")
    print("   - Labels: Remove 'CHANGE_TO_YOUR_NAME', add 'member-yourname'")
    print("   - Working On field: Add your full name")
    print("   - Comment: 'Taking this - [Your Name]'")
    print("4. Use Discord for cross-team coordination")
    print("\n📧 Team Emails:")
    print("   - Team A: team-a@company.com")
    print("   - Team B: team-b@company.com") 
    print("   - Team C: team-c@company.com")
    print("   - Team D: team-d@company.com")
