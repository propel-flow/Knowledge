#!/usr/bin/env python3
"""
Release Notes Field Completeness Monitor
Automated checking and reminders for PM/QA teams based on standardized Epic structure
"""

import json
import re
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta

class FieldStatus(Enum):
    COMPLETE = "Complete"
    MISSING = "Missing" 
    INCOMPLETE = "Incomplete"
    NEEDS_REVIEW = "Needs Review"

class ReminderUrgency(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

@dataclass
class ReleaseNotesRequirement:
    epic_name: str
    field_name: str
    required: bool
    min_length: int
    patterns: List[str]
    examples: List[str]
    reminder_text: str

@dataclass
class ComplianceCheck:
    epic_id: str
    epic_name: str
    target_version: str
    field_status: Dict[str, FieldStatus]
    missing_fields: List[str]
    incomplete_fields: List[str]
    overall_completeness: float
    urgency: ReminderUrgency
    days_to_release: int
    reminder_actions: List[str]

class ReleaseNotesMonitor:
    def __init__(self):
        # Based on your standardized Epic structure
        self.required_epics = {
            "Introduction to Extreme Platform ONE": {
                "description": {
                    "required": True,
                    "min_length": 100,
                    "patterns": ["purpose", "key features", "benefits"],
                    "examples": [
                        "unified touchpoint for applications",
                        "comprehensive UI, real-time notifications",
                        "single sign-on (SSO) capabilities"
                    ],
                    "reminder_text": "Provide overview highlighting purpose, key features, and benefits"
                }
            },
            
            "Supported Applications": {
                "description": {
                    "required": True,
                    "min_length": 200,
                    "patterns": ["ExtremeCloud", "application", "management"],
                    "examples": [
                        "ExtremeCloud IQ: Centralized configuration",
                        "ExtremeCloud SD-WAN: Unified management",
                        "ExtremeCloud Universal ZTNA: Security"
                    ],
                    "reminder_text": "List all applications with brief descriptions of their capabilities"
                }
            },
            
            "Prerequisites": {
                "description": {
                    "required": True,
                    "min_length": 150,
                    "patterns": ["supported device", "OS version", "version"],
                    "examples": [
                        "VOSS or Fabric Engine devices must be 9.1.0.1 or later",
                        "EXOS or Switch Engine must be 33.2.1.12 or later"
                    ],
                    "reminder_text": "Specify supported device OS versions and device models"
                }
            },
            
            "Features Supported for this Release": {
                "description": {
                    "required": True,
                    "min_length": 100,
                    "patterns": ["feature", "description", "table"],
                    "examples": [
                        "Feature: Backup & Restore | Description: Manual backup and restore",
                        "Feature: Subscriptions & Licensing | Description: View subscriptions"
                    ],
                    "reminder_text": "Create tabular format listing features with descriptions"
                }
            },
            
            "Features not supported in this Release": {
                "description": {
                    "required": True,
                    "min_length": 50,
                    "patterns": ["not supported", "limitation", "feature"],
                    "examples": [
                        "Feature: Correlation of Physical View | Description: Not supported"
                    ],
                    "reminder_text": "List unsupported features in tabular format with explanations"
                }
            },
            
            "Known Issues and Limitations": {
                "description": {
                    "required": True,
                    "min_length": 50,
                    "patterns": ["issue", "limitation", "caveat"],
                    "examples": [
                        "Trial Subscriptions are only available for SD-WAN",
                        "Intermittent issue - topology gets distorted"
                    ],
                    "reminder_text": "Document all caveats, limitations, and known issues for this release"
                }
            }
        }
        
        # Defect-related fields (existing JIRA structure)
        self.defect_fields = {
            "Defects Closed with Code Changes": {
                "fields": ["symptom", "condition", "workaround"],
                "required": False,  # Only if defects exist
                "reminder_text": "For each defect: provide symptom, condition, and workaround"
            },
            "Defects Closed without Code Changes": {
                "fields": ["symptom", "reason"],
                "required": False,
                "reminder_text": "For each defect: provide symptom and reason for no code changes"
            },
            "Open Defects": {
                "fields": ["symptom", "condition", "status"],
                "required": False,
                "reminder_text": "For each open defect: provide symptom, condition, and current status"
            }
        }

    def check_epic_compliance(self, epic_data: Dict, target_release_date: str) -> ComplianceCheck:
        """Check if Epic meets release notes requirements"""
        epic_id = epic_data.get('key', 'UNKNOWN')
        epic_name = epic_data.get('Epic Name', '')
        target_version = epic_data.get('Target Version', '')
        
        # Calculate days to release
        days_to_release = self._calculate_days_to_release(target_release_date)
        
        field_status = {}
        missing_fields = []
        incomplete_fields = []
        
        # Check if this is a required Epic type
        if epic_name in self.required_epics:
            requirements = self.required_epics[epic_name]
            
            for field_name, field_req in requirements.items():
                status = self._check_field_status(epic_data, field_name, field_req)
                field_status[field_name] = status
                
                if status == FieldStatus.MISSING:
                    missing_fields.append(field_name)
                elif status == FieldStatus.INCOMPLETE:
                    incomplete_fields.append(field_name)
        
        # Calculate overall completeness
        total_fields = len(field_status)
        complete_fields = sum(1 for status in field_status.values() if status == FieldStatus.COMPLETE)
        completeness = (complete_fields / total_fields * 100) if total_fields > 0 else 0
        
        # Determine urgency based on completeness and time to release
        urgency = self._determine_urgency(completeness, days_to_release)
        
        # Generate reminder actions
        reminder_actions = self._generate_reminder_actions(
            epic_name, missing_fields, incomplete_fields, days_to_release
        )
        
        return ComplianceCheck(
            epic_id=epic_id,
            epic_name=epic_name,
            target_version=target_version,
            field_status=field_status,
            missing_fields=missing_fields,
            incomplete_fields=incomplete_fields,
            overall_completeness=completeness,
            urgency=urgency,
            days_to_release=days_to_release,
            reminder_actions=reminder_actions
        )

    def _check_field_status(self, epic_data: Dict, field_name: str, requirements: Dict) -> FieldStatus:
        """Check status of a specific field"""
        field_content = epic_data.get('Description', '')
        
        if not field_content or len(field_content.strip()) < 10:
            return FieldStatus.MISSING
        
        # Check minimum length
        if len(field_content) < requirements.get('min_length', 50):
            return FieldStatus.INCOMPLETE
        
        # Check for required patterns
        required_patterns = requirements.get('patterns', [])
        found_patterns = 0
        
        for pattern in required_patterns:
            if re.search(pattern, field_content, re.IGNORECASE):
                found_patterns += 1
        
        pattern_coverage = found_patterns / len(required_patterns) if required_patterns else 1
        
        if pattern_coverage >= 0.8:
            return FieldStatus.COMPLETE
        elif pattern_coverage >= 0.5:
            return FieldStatus.NEEDS_REVIEW
        else:
            return FieldStatus.INCOMPLETE

    def _calculate_days_to_release(self, target_release_date: str) -> int:
        """Calculate days until target release"""
        try:
            release_date = datetime.strptime(target_release_date, '%Y-%m-%d')
            today = datetime.now()
            return (release_date - today).days
        except:
            return 30  # Default to 30 days if date parsing fails

    def _determine_urgency(self, completeness: float, days_to_release: int) -> ReminderUrgency:
        """Determine reminder urgency based on completeness and time"""
        if days_to_release <= 7:
            if completeness < 80:
                return ReminderUrgency.CRITICAL
            elif completeness < 95:
                return ReminderUrgency.HIGH
            else:
                return ReminderUrgency.MEDIUM
        elif days_to_release <= 14:
            if completeness < 60:
                return ReminderUrgency.HIGH
            elif completeness < 80:
                return ReminderUrgency.MEDIUM
            else:
                return ReminderUrgency.LOW
        elif days_to_release <= 30:
            if completeness < 40:
                return ReminderUrgency.MEDIUM
            else:
                return ReminderUrgency.LOW
        else:
            return ReminderUrgency.LOW

    def _generate_reminder_actions(self, epic_name: str, missing_fields: List[str], 
                                 incomplete_fields: List[str], days_to_release: int) -> List[str]:
        """Generate specific reminder actions for PM/QA team"""
        actions = []
        
        if epic_name in self.required_epics:
            requirements = self.required_epics[epic_name]
            
            for field in missing_fields:
                if field in requirements:
                    action = f"📝 MISSING: {requirements[field]['reminder_text']}"
                    actions.append(action)
                    
                    # Add examples for clarity
                    examples = requirements[field].get('examples', [])
                    if examples:
                        actions.append(f"   💡 Example: {examples[0]}")
            
            for field in incomplete_fields:
                if field in requirements:
                    action = f"⚠️ INCOMPLETE: {requirements[field]['reminder_text']}"
                    actions.append(action)
        
        # Add urgency-based actions
        if days_to_release <= 7:
            actions.append("🚨 URGENT: Release in ≤ 7 days - immediate action required!")
            actions.append("📞 Escalate to release manager if blockers exist")
        elif days_to_release <= 14:
            actions.append("⏰ HIGH PRIORITY: Release in ≤ 14 days")
            actions.append("📅 Schedule Epic review meeting this week")
        
        return actions

    def generate_pm_qa_report(self, epic_checks: List[ComplianceCheck]) -> str:
        """Generate actionable report for PM/QA teams"""
        
        # Sort by urgency and completeness
        epic_checks.sort(key=lambda x: (x.urgency.value, x.overall_completeness))
        
        report = "🎯 RELEASE NOTES COMPLIANCE REPORT\n"
        report += "=" * 50 + "\n\n"
        
        # Summary statistics
        total_epics = len(epic_checks)
        critical_issues = sum(1 for check in epic_checks if check.urgency == ReminderUrgency.CRITICAL)
        high_issues = sum(1 for check in epic_checks if check.urgency == ReminderUrgency.HIGH)
        avg_completeness = sum(check.overall_completeness for check in epic_checks) / total_epics if total_epics > 0 else 0
        
        report += f"📊 SUMMARY:\n"
        report += f"Total Epics: {total_epics}\n"
        report += f"Average Completeness: {avg_completeness:.1f}%\n"
        report += f"Critical Issues: {critical_issues}\n"
        report += f"High Priority Issues: {high_issues}\n\n"
        
        # Group by urgency
        urgent_epics = [check for check in epic_checks if check.urgency in [ReminderUrgency.CRITICAL, ReminderUrgency.HIGH]]
        
        if urgent_epics:
            report += "🚨 IMMEDIATE ACTION REQUIRED:\n\n"
            for check in urgent_epics:
                report += f"Epic: {check.epic_name} ({check.epic_id})\n"
                report += f"Completeness: {check.overall_completeness:.1f}%\n"
                report += f"Days to Release: {check.days_to_release}\n"
                report += f"Urgency: {check.urgency.value}\n\n"
                
                if check.reminder_actions:
                    report += "Required Actions:\n"
                    for action in check.reminder_actions:
                        report += f"  {action}\n"
                report += "\n" + "-" * 40 + "\n\n"
        
        # Standard priority items
        standard_epics = [check for check in epic_checks if check.urgency in [ReminderUrgency.MEDIUM, ReminderUrgency.LOW]]
        
        if standard_epics:
            report += "📋 STANDARD PRIORITY:\n\n"
            for check in standard_epics:
                if check.overall_completeness < 100:
                    report += f"Epic: {check.epic_name} ({check.overall_completeness:.1f}% complete)\n"
                    if check.missing_fields:
                        report += f"  Missing: {', '.join(check.missing_fields)}\n"
                    if check.incomplete_fields:
                        report += f"  Needs Work: {', '.join(check.incomplete_fields)}\n"
                    report += "\n"
        
        # Quick action suggestions
        report += "💡 QUICK WINS:\n"
        report += "• Use existing product documentation as source material\n"
        report += "• Copy content from previous release notes and update\n"
        report += "• Schedule 30-minute Epic review sessions with tech leads\n"
        report += "• Create templates for missing Epic types\n\n"
        
        return report

    def generate_automated_reminders(self, epic_checks: List[ComplianceCheck]) -> Dict[str, List[str]]:
        """Generate automated reminder emails/notifications"""
        reminders = {
            'pm_team': [],
            'qa_team': [],
            'tech_leads': [],
            'release_manager': []
        }
        
        for check in epic_checks:
            if check.urgency == ReminderUrgency.CRITICAL:
                reminders['release_manager'].append(
                    f"CRITICAL: {check.epic_name} ({check.overall_completeness:.1f}% complete) "
                    f"- Release in {check.days_to_release} days"
                )
            
            if check.urgency in [ReminderUrgency.CRITICAL, ReminderUrgency.HIGH]:
                reminders['pm_team'].append(
                    f"Epic {check.epic_id} needs immediate attention: {len(check.missing_fields)} missing fields"
                )
            
            if check.missing_fields or check.incomplete_fields:
                reminders['qa_team'].append(
                    f"Review Epic {check.epic_id} for release notes accuracy and completeness"
                )
                
                reminders['tech_leads'].append(
                    f"Technical review needed for Epic {check.epic_id}: {check.epic_name}"
                )
        
        return reminders

# Example usage
def monitor_release_readiness(epic_data_list: List[Dict], target_release_date: str) -> None:
    """Main monitoring function"""
    monitor = ReleaseNotesMonitor()
    
    epic_checks = []
    for epic_data in epic_data_list:
        check = monitor.check_epic_compliance(epic_data, target_release_date)
        epic_checks.append(check)
    
    # Generate reports
    pm_qa_report = monitor.generate_pm_qa_report(epic_checks)
    automated_reminders = monitor.generate_automated_reminders(epic_checks)
    
    print(pm_qa_report)
    
    # Example: Send automated notifications
    print("\n📧 AUTOMATED REMINDERS:")
    for team, reminders in automated_reminders.items():
        if reminders:
            print(f"\n{team.upper()}:")
            for reminder in reminders:
                print(f"  • {reminder}")

if __name__ == "__main__":
    # Example Epic data (based on your structure)
    sample_epics = [
        {
            'key': 'EPIC-001',
            'Epic Name': 'Introduction to Extreme Platform ONE',
            'Target Version': '25.3.0',
            'Description': 'Extreme Platform ONE is a unified touchpoint for Extreme Networks applications, simplifying the user experience and providing automation at scale. Key features include comprehensive UI, real-time notifications, contextual AI support, and single sign-on (SSO) capabilities.'
        },
        {
            'key': 'EPIC-002', 
            'Epic Name': 'Prerequisites',
            'Target Version': '25.3.0',
            'Description': 'Some basic info but missing device versions'  # Incomplete
        }
    ]
    
    monitor_release_readiness(sample_epics, '2025-07-15')
