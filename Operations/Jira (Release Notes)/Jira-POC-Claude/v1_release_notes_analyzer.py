#!/usr/bin/env python3
"""
Release Notes Quality Analyzer
Focuses on Epic-level documentation quality for release notes generation
"""

import re
import json
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict

class ReleaseNoteQuality(Enum):
    RELEASE_READY = "Release Ready"
    NEEDS_REVIEW = "Needs Review"
    MISSING_INFO = "Missing Info"
    NOT_APPLICABLE = "Not Applicable"

@dataclass
class ReleaseNoteScore:
    component: str
    epic_id: str
    epic_name: str
    quality: ReleaseNoteQuality
    user_impact: str
    technical_details: str
    gaps: List[str]
    qa_vetted: bool
    dev_vetted: bool
    ready_for_docs: bool

class ReleaseNotesAnalyzer:
    def __init__(self):
        # Release notes critical fields
        self.release_critical_fields = {
            'epic_name': 'Epic Name',
            'description': 'Description', 
            'acceptance_criteria': 'Acceptance Criteria',
            'release_notes': 'Release Notes',
            'release_notes_required': 'Release Notes Required',
            'customer_impact': 'Customer Impact',
            'component': 'Component/s',
            'fix_versions': 'Fix Version/s',
            'target_version': 'Target Version',
            'qa_verified': 'QA Analysis',
            'dev_complete': 'Dev Complete Date'
        }
        
        # User-facing language patterns
        self.user_facing_patterns = {
            'new_feature': r'(new|added|introduce|enable|support)',
            'improvement': r'(improve|enhance|better|faster|optimiz)',
            'fix': r'(fix|resolve|correct|address)',
            'change': r'(change|modif|updat|replac)',
            'deprecation': r'(deprecat|remov|discontinu|end.*support)'
        }
        
        # Technical jargon that needs translation
        self.technical_jargon = [
            'API', 'CLI', 'endpoint', 'microservice', 'backend', 'frontend',
            'database', 'cache', 'queue', 'thread', 'mutex', 'semaphore'
        ]

    def extract_epic_hierarchy(self, jira_data: Dict) -> Dict[str, Any]:
        """Extract Epic and its related issues"""
        epic_info = {
            'epic_id': jira_data.get('key', ''),
            'epic_name': jira_data.get('Epic Name', ''),
            'issue_type': jira_data.get('Issue Type', {}).get('name', ''),
            'component': self._extract_components(jira_data),
            'fix_versions': self._extract_versions(jira_data),
            'subtasks': jira_data.get('Sub-Tasks', []),
            'linked_issues': jira_data.get('Linked Issues', [])
        }
        return epic_info

    def _extract_components(self, jira_data: Dict) -> List[str]:
        """Extract component information"""
        components = jira_data.get('Component/s', [])
        if isinstance(components, list):
            return [comp.get('name', '') for comp in components if comp.get('name')]
        return []

    def _extract_versions(self, jira_data: Dict) -> List[str]:
        """Extract version information"""
        versions = jira_data.get('Fix Version/s', [])
        if isinstance(versions, list):
            return [ver.get('name', '') for ver in versions if ver.get('name')]
        return []

    def analyze_user_impact(self, description: str, epic_name: str) -> Dict[str, Any]:
        """Analyze and score user-facing impact"""
        impact_analysis = {
            'has_user_perspective': False,
            'impact_type': 'unknown',
            'user_benefit': '',
            'technical_complexity': 'medium',
            'customer_facing': False
        }
        
        text = f"{epic_name} {description}".lower()
        
        # Check for user perspective
        user_indicators = ['user', 'customer', 'admin', 'operator', 'developer']
        if any(indicator in text for indicator in user_indicators):
            impact_analysis['has_user_perspective'] = True
            impact_analysis['customer_facing'] = True
        
        # Categorize impact type
        for impact_type, pattern in self.user_facing_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                impact_analysis['impact_type'] = impact_type
                break
        
        # Extract user benefit
        benefit_patterns = [
            r'so that (.+?)(?:\.|$)',
            r'benefit[s]? (.+?)(?:\.|$)',
            r'allow[s]? (.+?) to (.+?)(?:\.|$)',
            r'enable[s]? (.+?)(?:\.|$)'
        ]
        
        for pattern in benefit_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                impact_analysis['user_benefit'] = match.group(1).strip()
                break
        
        return impact_analysis

    def assess_release_note_readiness(self, jira_data: Dict) -> ReleaseNoteScore:
        """Assess if Epic is ready for release notes"""
        epic_info = self.extract_epic_hierarchy(jira_data)
        
        # Core information extraction
        description = jira_data.get('Description', '')
        release_notes_field = jira_data.get('Release Notes', '')
        release_notes_required = jira_data.get('Release Notes Required', {})
        customer_impact = jira_data.get('Customer Impact', '')
        
        # Check if release notes are required
        rn_required = True  # Default assumption
        if isinstance(release_notes_required, dict):
            rn_value = release_notes_required.get('value', '').lower()
            if rn_value in ['no', 'false', 'not required']:
                rn_required = False
        
        if not rn_required:
            return ReleaseNoteScore(
                component=', '.join(epic_info['component']),
                epic_id=epic_info['epic_id'],
                epic_name=epic_info['epic_name'],
                quality=ReleaseNoteQuality.NOT_APPLICABLE,
                user_impact="Release notes not required",
                technical_details="",
                gaps=[],
                qa_vetted=False,
                dev_vetted=False,
                ready_for_docs=False
            )
        
        # Analyze user impact
        impact_analysis = self.analyze_user_impact(description, epic_info['epic_name'])
        
        # Check vetting status
        qa_vetted = bool(jira_data.get('QA Analysis') or jira_data.get('QA Testcase'))
        dev_vetted = bool(jira_data.get('Dev Complete Date') or jira_data.get('Fixed By'))
        
        # Identify gaps
        gaps = []
        
        if not description or len(description.strip()) < 50:
            gaps.append("Description too brief for release notes")
        
        if not impact_analysis['has_user_perspective']:
            gaps.append("No clear user perspective or benefit")
        
        if not impact_analysis['user_benefit']:
            gaps.append("User benefit not clearly articulated")
        
        if not epic_info['component']:
            gaps.append("Component not specified")
        
        if not epic_info['fix_versions']:
            gaps.append("Target version not specified")
        
        if not release_notes_field and not customer_impact:
            gaps.append("No dedicated release notes content")
        
        # Determine quality level
        if len(gaps) == 0 and qa_vetted and dev_vetted:
            quality = ReleaseNoteQuality.RELEASE_READY
        elif len(gaps) <= 2 and (qa_vetted or dev_vetted):
            quality = ReleaseNoteQuality.NEEDS_REVIEW
        else:
            quality = ReleaseNoteQuality.MISSING_INFO
        
        # Generate user-friendly impact description
        user_impact = self._generate_user_impact_description(
            impact_analysis, epic_info['epic_name'], description
        )
        
        # Extract technical details
        technical_details = self._extract_technical_details(description)
        
        return ReleaseNoteScore(
            component=', '.join(epic_info['component']),
            epic_id=epic_info['epic_id'],
            epic_name=epic_info['epic_name'],
            quality=quality,
            user_impact=user_impact,
            technical_details=technical_details,
            gaps=gaps,
            qa_vetted=qa_vetted,
            dev_vetted=dev_vetted,
            ready_for_docs=(quality == ReleaseNoteQuality.RELEASE_READY)
        )

    def _generate_user_impact_description(self, impact_analysis: Dict, epic_name: str, description: str) -> str:
        """Generate user-friendly impact description for release notes"""
        impact_type = impact_analysis['impact_type']
        user_benefit = impact_analysis['user_benefit']
        
        templates = {
            'new_feature': f"New feature: {epic_name}",
            'improvement': f"Enhancement: {epic_name}",
            'fix': f"Bug fix: {epic_name}",
            'change': f"Change: {epic_name}",
            'deprecation': f"Deprecation: {epic_name}"
        }
        
        base_description = templates.get(impact_type, f"Update: {epic_name}")
        
        if user_benefit:
            return f"{base_description}. {user_benefit.capitalize()}."
        else:
            # Extract first meaningful sentence from description
            sentences = description.split('.')
            if sentences and len(sentences[0]) > 10:
                return f"{base_description}. {sentences[0].strip()}."
        
        return base_description

    def _extract_technical_details(self, description: str) -> str:
        """Extract technical implementation details"""
        technical_sentences = []
        sentences = description.split('.')
        
        for sentence in sentences:
            # Look for technical keywords
            if any(jargon.lower() in sentence.lower() for jargon in self.technical_jargon):
                technical_sentences.append(sentence.strip())
            # Look for CLI commands or code
            elif re.search(r'`[^`]+`|--\w+|\w+\.\w+\(', sentence):
                technical_sentences.append(sentence.strip())
        
        return '. '.join(technical_sentences[:2])  # Limit to 2 sentences

    def generate_release_notes_report(self, epic_scores: List[ReleaseNoteScore]) -> Dict[str, Any]:
        """Generate comprehensive release notes readiness report"""
        
        # Group by component
        by_component = defaultdict(list)
        for score in epic_scores:
            by_component[score.component or 'Unspecified'].append(score)
        
        # Calculate statistics
        total_epics = len(epic_scores)
        ready_count = sum(1 for score in epic_scores if score.quality == ReleaseNoteQuality.RELEASE_READY)
        needs_review_count = sum(1 for score in epic_scores if score.quality == ReleaseNoteQuality.NEEDS_REVIEW)
        missing_info_count = sum(1 for score in epic_scores if score.quality == ReleaseNoteQuality.MISSING_INFO)
        
        # Identify most common gaps
        all_gaps = []
        for score in epic_scores:
            all_gaps.extend(score.gaps)
        
        gap_frequency = defaultdict(int)
        for gap in all_gaps:
            gap_frequency[gap] += 1
        
        common_gaps = sorted(gap_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'summary': {
                'total_epics': total_epics,
                'release_ready': ready_count,
                'needs_review': needs_review_count,
                'missing_info': missing_info_count,
                'readiness_percentage': round((ready_count / total_epics) * 100, 1) if total_epics > 0 else 0
            },
            'by_component': dict(by_component),
            'common_gaps': common_gaps,
            'recommended_actions': self._generate_recommendations(epic_scores)
        }

    def _generate_recommendations(self, epic_scores: List[ReleaseNoteScore]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        missing_user_impact = sum(1 for score in epic_scores 
                                 if "No clear user perspective" in score.gaps)
        if missing_user_impact > 0:
            recommendations.append(
                f"Add user perspective to {missing_user_impact} epics using 'As a [user] I can [action] so that [benefit]' format"
            )
        
        missing_components = sum(1 for score in epic_scores 
                               if "Component not specified" in score.gaps)
        if missing_components > 0:
            recommendations.append(
                f"Specify components for {missing_components} epics to enable proper release note categorization"
            )
        
        unvetted_items = sum(1 for score in epic_scores 
                           if not (score.qa_vetted and score.dev_vetted))
        if unvetted_items > 0:
            recommendations.append(
                f"Complete QA/Dev vetting for {unvetted_items} epics before release"
            )
        
        return recommendations

def analyze_release_readiness(jira_files: List[str]) -> None:
    """Main function to analyze release notes readiness"""
    analyzer = ReleaseNotesAnalyzer()
    epic_scores = []
    
    # In real implementation, you'd parse actual Jira files
    # This is a demonstration with sample data based on your examples
    
    sample_epics = [
        {
            'key': 'XCO-10595',
            'Epic Name': 'XCO TOS Integration : Tenant : VRF',
            'Issue Type': {'name': 'Epic'},
            'Description': '''XCO TOS Integration : Tenant support - VRF
            
            XCO 3.7.0 Supported CLI
            efa tenant vrf create [ --name vrf-name | --tenant tenant-name | --rttype { both | import | export } | --rt value...]
            
            This feature enables network administrators to create and manage VRF instances for tenant isolation in data center fabrics.
            Users can now configure VRF routing policies, static routes, and BGP settings through the EFA CLI interface.
            ''',
            'Component/s': [{'name': 'Tenant Service'}],
            'Fix Version/s': [{'name': 'XCO 4.0.0'}],
            'Release Notes Required': {'value': 'Yes'},
            'QA Analysis': 'Completed',
            'Dev Complete Date': '2025-03-15',
            'Customer Impact': 'High - New tenant VRF management capabilities'
        }
    ]
    
    for epic_data in sample_epics:
        score = analyzer.assess_release_note_readiness(epic_data)
        epic_scores.append(score)
    
    # Generate report
    report = analyzer.generate_release_notes_report(epic_scores)
    
    # Print results
    print("=" * 70)
    print("RELEASE NOTES READINESS REPORT")
    print("=" * 70)
    
    print(f"\n📊 SUMMARY:")
    print(f"Total Epics: {report['summary']['total_epics']}")
    print(f"Release Ready: {report['summary']['release_ready']} ({report['summary']['readiness_percentage']}%)")
    print(f"Needs Review: {report['summary']['needs_review']}")
    print(f"Missing Info: {report['summary']['missing_info']}")
    
    print(f"\n🔍 BY COMPONENT:")
    for component, scores in report['by_component'].items():
        print(f"\n{component}:")
        for score in scores:
            status_icon = "✅" if score.ready_for_docs else "⚠️" if score.quality == ReleaseNoteQuality.NEEDS_REVIEW else "❌"
            print(f"  {status_icon} {score.epic_id}: {score.epic_name}")
            print(f"     Impact: {score.user_impact}")
            if score.gaps:
                print(f"     Gaps: {', '.join(score.gaps)}")
    
    print(f"\n🔧 COMMON ISSUES:")
    for gap, count in report['common_gaps']:
        print(f"  • {gap}: {count} epics")
    
    print(f"\n💡 RECOMMENDATIONS:")
    for rec in report['recommended_actions']:
        print(f"  • {rec}")

if __name__ == "__main__":
    analyze_release_readiness(['epic_data.json'])
