#!/usr/bin/env python3
"""
JIRA Integration Priority Guide
Focus areas for transforming the documentation analysis code for direct JIRA integration
"""

# PRIORITY 1: JIRA API Integration Layer (Start Here)
# This is the foundation - focus 80% of effort here first

from jira import JIRA
import requests
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class JiraConfig:
    server: str
    username: str
    api_token: str
    project_key: str

class JiraDocumentationAnalyzer:
    """
    PRIORITY 1: Core JIRA integration - transform the release notes monitor
    This should be your first focus for transformation
    """
    
    def __init__(self, config: JiraConfig):
        self.jira = JIRA(
            server=config.server,
            basic_auth=(config.username, config.api_token)
        )
        self.project_key = config.project_key
        
    def get_epic_with_attachments(self, epic_key: str) -> Dict[str, Any]:
        """
        Transform your existing Epic analysis to work with live JIRA data
        This replaces the manual JSON parsing from your examples
        """
        try:
            # Get the Epic issue
            issue = self.jira.issue(epic_key, expand='attachment')
            
            # Extract Epic data in your existing format
            epic_data = {
                'key': issue.key,
                'Epic Name': getattr(issue.fields, 'customfield_10103', ''),  # Epic Name field
                'Description': issue.fields.description or '',
                'Target Version': self._extract_target_version(issue),
                'Issue Type': {'name': issue.fields.issuetype.name},
                'Component/s': self._extract_components(issue),
                'Acceptance Criteria': getattr(issue.fields, 'customfield_12961', ''),
                'Release Notes': getattr(issue.fields, 'customfield_14500', ''),
                'Release Notes Required': self._extract_release_notes_required(issue),
                'Attachment': self._extract_attachments(issue)
            }
            
            return epic_data
            
        except Exception as e:
            print(f"Error fetching Epic {epic_key}: {e}")
            return {}
    
    def _extract_target_version(self, issue) -> str:
        """Extract target version from various possible fields"""
        # Try multiple possible version fields
        if hasattr(issue.fields, 'fixVersions') and issue.fields.fixVersions:
            return issue.fields.fixVersions[0].name
        if hasattr(issue.fields, 'customfield_11211') and issue.fields.customfield_11211:
            return issue.fields.customfield_11211.name
        return ''
    
    def _extract_components(self, issue) -> List[Dict[str, str]]:
        """Extract components in your expected format"""
        if issue.fields.components:
            return [{'name': comp.name} for comp in issue.fields.components]
        return []
    
    def _extract_release_notes_required(self, issue) -> Dict[str, str]:
        """Extract release notes required field"""
        # This field varies by JIRA setup - adjust the customfield number
        rn_field = getattr(issue.fields, 'customfield_13017', None)
        if rn_field:
            return {'value': rn_field.value if hasattr(rn_field, 'value') else str(rn_field)}
        return {}
    
    def _extract_attachments(self, issue) -> List[Dict[str, Any]]:
        """
        Extract attachments in your expected format
        This handles the attachment analysis you mentioned
        """
        attachments = []
        for attachment in issue.fields.attachment:
            attachment_data = {
                'id': attachment.id,
                'filename': attachment.filename,
                'size': attachment.size,
                'mimeType': attachment.mimeType,
                'content': attachment.content,  # URL to download
                'created': attachment.created,
                'author': {
                    'displayName': attachment.author.displayName,
                    'emailAddress': getattr(attachment.author, 'emailAddress', '')
                }
            }
            attachments.append(attachment_data)
        return attachments
    
    def analyze_epic_attachments(self, epic_key: str) -> Dict[str, Any]:
        """
        PRIORITY 2: Analyze attachments like your specific_issues folder structure
        This should be your second focus area
        """
        epic_data = self.get_epic_with_attachments(epic_key)
        attachments = epic_data.get('Attachment', [])
        
        attachment_analysis = {
            'total_attachments': len(attachments),
            'attachment_types': {
                'images': [],
                'documents': [],
                'logs': [],
                'videos': [],
                'specs': [],
                'unknown': []
            },
            'documentation_value': 'low',  # low, medium, high
            'suggestions': []
        }
        
        # Analyze each attachment
        for attachment in attachments:
            filename = attachment['filename'].lower()
            mime_type = attachment.get('mimeType', '').lower()
            
            # Categorize attachments
            if any(ext in filename for ext in ['.png', '.jpg', '.jpeg', '.gif']) or 'image' in mime_type:
                attachment_analysis['attachment_types']['images'].append({
                    'filename': attachment['filename'],
                    'type': 'screenshot' if 'image-' in filename else 'diagram',
                    'documentation_value': 'high' if 'screenshot' in filename or 'diagram' in filename else 'medium'
                })
            elif any(ext in filename for ext in ['.pdf', '.doc', '.docx', '.md']):
                attachment_analysis['attachment_types']['documents'].append({
                    'filename': attachment['filename'],
                    'type': 'specification' if any(word in filename for word in ['spec', 'requirement', 'design']) else 'documentation',
                    'documentation_value': 'high'
                })
            elif any(ext in filename for ext in ['.txt', '.log', '.har']):
                attachment_analysis['attachment_types']['logs'].append({
                    'filename': attachment['filename'],
                    'type': 'troubleshooting_data',
                    'documentation_value': 'medium'
                })
            elif any(ext in filename for ext in ['.mp4', '.avi', '.mov', '.webm']):
                attachment_analysis['attachment_types']['videos'].append({
                    'filename': attachment['filename'],
                    'type': 'demo_or_training',
                    'documentation_value': 'very_high'
                })
            elif any(ext in filename for ext in ['.yaml', '.json', '.xml', '.spec']):
                attachment_analysis['attachment_types']['specs'].append({
                    'filename': attachment['filename'],
                    'type': 'technical_specification',
                    'documentation_value': 'very_high'
                })
            else:
                attachment_analysis['attachment_types']['unknown'].append({
                    'filename': attachment['filename'],
                    'type': 'unknown',
                    'documentation_value': 'unknown'
                })
        
        # Determine overall documentation value
        has_high_value = any(
            attachment_analysis['attachment_types']['videos'],
            attachment_analysis['attachment_types']['specs'],
            len(attachment_analysis['attachment_types']['images']) >= 3,
            len(attachment_analysis['attachment_types']['documents']) >= 1
        )
        
        if has_high_value:
            attachment_analysis['documentation_value'] = 'high'
        elif len(attachments) >= 2:
            attachment_analysis['documentation_value'] = 'medium'
        
        # Generate suggestions
        attachment_analysis['suggestions'] = self._generate_attachment_suggestions(attachment_analysis)
        
        return attachment_analysis
    
    def _generate_attachment_suggestions(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate suggestions based on attachment analysis"""
        suggestions = []
        
        if not analysis['attachment_types']['images']:
            suggestions.append("📸 Add screenshots of key UI elements or workflows")
        
        if not analysis['attachment_types']['videos']:
            suggestions.append("🎥 Consider adding a demo video of the main user workflow")
        
        if not analysis['attachment_types']['documents']:
            suggestions.append("📋 Attach any existing specifications or requirements documents")
        
        if analysis['attachment_types']['logs']:
            suggestions.append("🔧 Log files present - consider creating troubleshooting documentation")
        
        if len(analysis['attachment_types']['images']) >= 5:
            suggestions.append("✨ Great visual documentation! These images will enhance user guides")
        
        return suggestions

# PRIORITY 2: Batch Analysis for Testing (Transform your existing analysis scripts)
class JiraBatchAnalyzer:
    """
    Transform your existing release notes monitoring for batch testing
    Use this to analyze your existing JIRA export data
    """
    
    def __init__(self, jira_analyzer: JiraDocumentationAnalyzer):
        self.jira_analyzer = jira_analyzer
    
    def analyze_project_epics(self, project_key: str, target_version: str = None) -> Dict[str, Any]:
        """
        Analyze all Epics in a project - this is what you'd use for testing
        """
        # Build JQL query
        jql = f'project = {project_key} AND issuetype = Epic'
        if target_version:
            jql += f' AND fixVersion = "{target_version}"'
        
        # Get all matching Epics
        issues = self.jira_analyzer.jira.search_issues(jql, maxResults=100)
        
        analysis_results = {
            'total_epics': len(issues),
            'analyzed_epics': [],
            'summary_stats': {
                'with_attachments': 0,
                'high_doc_value': 0,
                'needs_improvement': 0
            }
        }
        
        # Analyze each Epic
        for issue in issues:
            epic_analysis = {
                'epic_key': issue.key,
                'epic_name': getattr(issue.fields, 'customfield_10103', 'No Name'),
                'description_length': len(issue.fields.description or ''),
                'attachment_analysis': self.jira_analyzer.analyze_epic_attachments(issue.key),
                'documentation_completeness': self._assess_completeness(issue)
            }
            
            # Update summary stats
            if epic_analysis['attachment_analysis']['total_attachments'] > 0:
                analysis_results['summary_stats']['with_attachments'] += 1
            
            if epic_analysis['attachment_analysis']['documentation_value'] == 'high':
                analysis_results['summary_stats']['high_doc_value'] += 1
            
            if epic_analysis['documentation_completeness'] < 60:
                analysis_results['summary_stats']['needs_improvement'] += 1
            
            analysis_results['analyzed_epics'].append(epic_analysis)
        
        return analysis_results
    
    def _assess_completeness(self, issue) -> int:
        """Assess Epic completeness percentage"""
        score = 0
        
        # Description present and substantial
        if issue.fields.description and len(issue.fields.description) > 100:
            score += 30
        elif issue.fields.description:
            score += 15
        
        # Epic name present
        epic_name = getattr(issue.fields, 'customfield_10103', '')
        if epic_name:
            score += 20
        
        # Target version specified
        if issue.fields.fixVersions:
            score += 15
        
        # Components specified
        if issue.fields.components:
            score += 10
        
        # Attachments present
        if issue.fields.attachment:
            score += 15
            
        # Acceptance criteria present
        acceptance_criteria = getattr(issue.fields, 'customfield_12961', '')
        if acceptance_criteria:
            score += 10
        
        return min(score, 100)

# PRIORITY 3: Reporting and Automation (Transform your reporting functions)
class JiraDocumentationReporter:
    """
    Transform your existing PM/QA reporting for JIRA integration
    """
    
    def __init__(self, batch_analyzer: JiraBatchAnalyzer):
        self.batch_analyzer = batch_analyzer
    
    def generate_project_report(self, project_key: str, target_version: str = None) -> str:
        """Generate documentation readiness report for PM/QA teams"""
        analysis = self.batch_analyzer.analyze_project_epics(project_key, target_version)
        
        report = f"📚 DOCUMENTATION READINESS REPORT - {project_key}\n"
        report += "=" * 60 + "\n\n"
        
        # Summary statistics
        total = analysis['total_epics']
        stats = analysis['summary_stats']
        
        report += f"📊 SUMMARY:\n"
        report += f"Total Epics Analyzed: {total}\n"
        report += f"Epics with Attachments: {stats['with_attachments']} ({(stats['with_attachments']/total*100):.1f}%)\n"
        report += f"High Documentation Value: {stats['high_doc_value']} ({(stats['high_doc_value']/total*100):.1f}%)\n"
        report += f"Need Improvement: {stats['needs_improvement']} ({(stats['needs_improvement']/total*100):.1f}%)\n\n"
        
        # Detailed Epic analysis
        report += "🔍 EPIC ANALYSIS:\n\n"
        
        for epic in analysis['analyzed_epics']:
            status_icon = "✅" if epic['documentation_completeness'] >= 80 else "⚠️" if epic['documentation_completeness'] >= 60 else "❌"
            
            report += f"{status_icon} {epic['epic_key']}: {epic['epic_name']}\n"
            report += f"   Completeness: {epic['documentation_completeness']}%\n"
            report += f"   Attachments: {epic['attachment_analysis']['total_attachments']} files\n"
            report += f"   Doc Value: {epic['attachment_analysis']['documentation_value']}\n"
            
            if epic['attachment_analysis']['suggestions']:
                report += f"   Suggestions: {epic['attachment_analysis']['suggestions'][0]}\n"
            
            report += "\n"
        
        return report

# Example Usage for Testing Your Current Data
def test_with_your_jira_data():
    """
    How to test this with your current JIRA setup
    Start here for immediate testing
    """
    
    # Configure your JIRA connection
    config = JiraConfig(
        server="https://jira.extremenetworks.com",
        username="your-email@extremenetworks.com", 
        api_token="your-api-token",  # Generate from JIRA profile
        project_key="XCO"  # Based on your examples
    )
    
    # Initialize analyzers
    jira_analyzer = JiraDocumentationAnalyzer(config)
    batch_analyzer = JiraBatchAnalyzer(jira_analyzer)
    reporter = JiraDocumentationReporter(batch_analyzer)
    
    # Test with your specific Epic examples
    test_epics = ["XCO-10595", "XCO-11218", "XIQ-5896"]
    
    print("🧪 TESTING INDIVIDUAL EPICS:")
    for epic_key in test_epics:
        print(f"\n--- Analyzing {epic_key} ---")
        epic_data = jira_analyzer.get_epic_with_attachments(epic_key)
        attachment_analysis = jira_analyzer.analyze_epic_attachments(epic_key)
        
        print(f"Epic Name: {epic_data.get('Epic Name', 'N/A')}")
        print(f"Description Length: {len(epic_data.get('Description', ''))}")
        print(f"Attachments: {attachment_analysis['total_attachments']}")
        print(f"Documentation Value: {attachment_analysis['documentation_value']}")
        
        if attachment_analysis['suggestions']:
            print("Suggestions:")
            for suggestion in attachment_analysis['suggestions']:
                print(f"  • {suggestion}")
    
    # Test project-wide analysis
    print(f"\n🎯 PROJECT-WIDE ANALYSIS:")
    report = reporter.generate_project_report("XCO", "XCO 4.0.0")
    print(report)

if __name__ == "__main__":
    # This is what you'd run to test with your actual JIRA data
    test_with_your_jira_data()
