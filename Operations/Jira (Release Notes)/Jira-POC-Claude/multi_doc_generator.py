#!/usr/bin/env python3
"""
Multi-Document Generator from Release Notes Structure
Demonstrates how your Epic structure can generate various documentation types
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum

class DocumentType(Enum):
    RELEASE_NOTES = "Release Notes"
    GETTING_STARTED = "Getting Started Guide"
    SYSTEM_REQUIREMENTS = "System Requirements"
    FEATURE_OVERVIEW = "Feature Overview"
    KNOWN_ISSUES = "Known Issues & Troubleshooting"
    INSTALLATION_GUIDE = "Installation Guide"
    ADMIN_GUIDE = "Administrator Guide"
    API_DOCS = "API Documentation"

@dataclass
class DocumentTemplate:
    doc_type: DocumentType
    coverage_from_rn: int  # Percentage that can be auto-generated
    required_epics: List[str]
    missing_elements: List[str]
    template: str

class MultiDocumentGenerator:
    def __init__(self):
        self.document_templates = {
            DocumentType.RELEASE_NOTES: DocumentTemplate(
                doc_type=DocumentType.RELEASE_NOTES,
                coverage_from_rn=100,
                required_epics=[
                    "Introduction to Extreme Platform ONE",
                    "Supported Applications", 
                    "Prerequisites",
                    "Features Supported for this Release",
                    "Features not supported in this Release",
                    "Known Issues and Limitations"
                ],
                missing_elements=[],
                template="""
# Release Notes - Version {version}

## What's New
{introduction}

## Supported Applications  
{supported_applications}

## System Requirements
{prerequisites}

## New Features
{features_supported}

## Limitations
{features_not_supported}

## Known Issues
{known_issues}

## Bug Fixes
{defects_closed}
                """
            ),
            
            DocumentType.GETTING_STARTED: DocumentTemplate(
                doc_type=DocumentType.GETTING_STARTED,
                coverage_from_rn=80,
                required_epics=[
                    "Introduction to Extreme Platform ONE",
                    "Prerequisites", 
                    "Supported Applications"
                ],
                missing_elements=[
                    "Step-by-step setup procedures",
                    "First-time user workflows",
                    "Quick start examples"
                ],
                template="""
# Getting Started with Extreme Platform ONE

## Welcome
{introduction}

## Before You Begin
{prerequisites}

## What You Can Do
{supported_applications}

## Quick Start
⚠️ MISSING: Need to add Quick Start Epic with:
- Account setup steps
- First login procedure  
- Basic navigation walkthrough

## Next Steps
⚠️ MISSING: Need User Workflows Epic with:
- Common daily tasks
- Key workflows to try first
                """
            ),
            
            DocumentType.SYSTEM_REQUIREMENTS: DocumentTemplate(
                doc_type=DocumentType.SYSTEM_REQUIREMENTS,
                coverage_from_rn=95,
                required_epics=["Prerequisites"],
                missing_elements=["Network requirements", "Browser compatibility"],
                template="""
# System Requirements

## Supported Devices
{prerequisites}

## Additional Requirements
⚠️ MISSING: Need to add to Prerequisites Epic:
- Network connectivity requirements
- Browser compatibility matrix
- Minimum bandwidth specifications
                """
            ),
            
            DocumentType.FEATURE_OVERVIEW: DocumentTemplate(
                doc_type=DocumentType.FEATURE_OVERVIEW,
                coverage_from_rn=90,
                required_epics=[
                    "Features Supported for this Release",
                    "Supported Applications"
                ],
                missing_elements=["Use case examples", "Benefit statements"],
                template="""
# Feature Overview

## Platform Capabilities
{supported_applications}

## Available Features
{features_supported}

## Use Cases
⚠️ MISSING: Need Use Cases Epic with:
- Real-world scenarios
- Business benefits  
- ROI examples
                """
            ),
            
            DocumentType.INSTALLATION_GUIDE: DocumentTemplate(
                doc_type=DocumentType.INSTALLATION_GUIDE,
                coverage_from_rn=65,
                required_epics=["Prerequisites"],
                missing_elements=[
                    "Installation procedures",
                    "Configuration steps", 
                    "Post-installation verification"
                ],
                template="""
# Installation Guide

## Prerequisites
{prerequisites}

## Installation Steps
⚠️ MISSING: Need Installation Procedures Epic with:
- Download instructions
- Step-by-step installation
- Configuration examples
- Verification procedures

## Post-Installation
⚠️ MISSING: Need Post-Installation Epic with:
- Initial configuration
- User account setup
- Integration testing
                """
            ),
            
            DocumentType.API_DOCS: DocumentTemplate(
                doc_type=DocumentType.API_DOCS,
                coverage_from_rn=50,
                required_epics=["Supported Applications"],
                missing_elements=[
                    "API endpoints",
                    "Authentication methods",
                    "Request/response examples",
                    "Error codes"
                ],
                template="""
# API Documentation

## Overview
{supported_applications}

## Authentication
⚠️ MISSING: Need API Authentication Epic

## Endpoints
⚠️ MISSING: Need API Endpoints Epic with:
- Endpoint specifications
- Request/response schemas
- Code examples
- Rate limiting details

## Error Handling
⚠️ MISSING: Need API Error Handling Epic
                """
            )
        }

    def generate_document(self, doc_type: DocumentType, epic_data: Dict[str, Dict]) -> str:
        """Generate a specific document type from Epic data"""
        template_info = self.document_templates.get(doc_type)
        if not template_info:
            return f"Document type {doc_type.value} not supported"
        
        # Extract content from relevant Epics
        content_vars = {}
        
        for epic_name in template_info.required_epics:
            if epic_name in epic_data:
                epic = epic_data[epic_name]
                var_name = epic_name.lower().replace(' ', '_').replace('extreme_platform_one', 'introduction')
                content_vars[var_name] = epic.get('Description', 'Content not available')
        
        # Add version if available
        content_vars['version'] = epic_data.get('target_version', '25.3.0')
        
        # Handle defects for release notes
        if doc_type == DocumentType.RELEASE_NOTES:
            defects = self._format_defects(epic_data.get('defects', {}))
            content_vars['defects_closed'] = defects
        
        # Generate the document
        try:
            generated_doc = template_info.template.format(**content_vars)
            return generated_doc
        except KeyError as e:
            return f"Missing required content for {doc_type.value}: {e}"

    def _format_defects(self, defects_data: Dict) -> str:
        """Format defect information for release notes"""
        if not defects_data:
            return "No defects closed in this release."
        
        formatted = "## Defects Resolved\n\n"
        
        for defect_id, defect_info in defects_data.items():
            formatted += f"**{defect_id}:** {defect_info.get('symptom', 'Issue resolved')}\n"
            if defect_info.get('workaround'):
                formatted += f"*Previous Workaround:* {defect_info['workaround']}\n"
            formatted += "\n"
        
        return formatted

    def analyze_documentation_coverage(self, epic_data: Dict[str, Dict]) -> Dict[str, Any]:
        """Analyze what documentation can be generated and what's missing"""
        
        coverage_analysis = {
            'available_epics': list(epic_data.keys()),
            'document_readiness': {},
            'missing_epics_needed': [],
            'enhancement_suggestions': []
        }
        
        for doc_type, template_info in self.document_templates.items():
            available_epics = 0
            missing_epics = []
            
            for required_epic in template_info.required_epics:
                if required_epic in epic_data:
                    available_epics += 1
                else:
                    missing_epics.append(required_epic)
            
            epic_coverage = (available_epics / len(template_info.required_epics)) * 100 if template_info.required_epics else 100
            overall_readiness = (epic_coverage / 100) * (template_info.coverage_from_rn / 100) * 100
            
            coverage_analysis['document_readiness'][doc_type.value] = {
                'overall_readiness': round(overall_readiness, 1),
                'epic_coverage': round(epic_coverage, 1),
                'rn_coverage': template_info.coverage_from_rn,
                'missing_epics': missing_epics,
                'missing_elements': template_info.missing_elements,
                'can_generate': overall_readiness >= 70
            }
            
            # Collect missing epics
            for missing_epic in missing_epics:
                if missing_epic not in coverage_analysis['missing_epics_needed']:
                    coverage_analysis['missing_epics_needed'].append(missing_epic)
        
        # Generate enhancement suggestions
        coverage_analysis['enhancement_suggestions'] = self._generate_enhancement_suggestions(coverage_analysis)
        
        return coverage_analysis

    def _generate_enhancement_suggestions(self, coverage_analysis: Dict) -> List[str]:
        """Generate suggestions for improving documentation coverage"""
        suggestions = []
        
        # Analyze what's commonly missing
        all_missing_elements = []
        for doc_info in coverage_analysis['document_readiness'].values():
            all_missing_elements.extend(doc_info['missing_elements'])
        
        # Count frequency of missing elements
        from collections import Counter
        missing_frequency = Counter(all_missing_elements)
        
        # Generate suggestions based on frequency
        for element, count in missing_frequency.most_common(3):
            if count >= 2:
                suggestions.append(f"Consider adding Epic for '{element}' - needed for {count} document types")
        
        # Specific suggestions for high-value additions
        doc_readiness = coverage_analysis['document_readiness']
        
        if doc_readiness['Getting Started Guide']['overall_readiness'] < 80:
            suggestions.append("Add 'User Workflows' Epic to enable Getting Started Guide generation")
        
        if doc_readiness['Installation Guide']['overall_readiness'] < 70:
            suggestions.append("Add 'Installation Procedures' Epic to enable Installation Guide generation")
        
        if doc_readiness['API Documentation']['overall_readiness'] < 60:
            suggestions.append("Add 'API Specifications' Epic to enable API Documentation generation")
        
        return suggestions

    def generate_coverage_report(self, epic_data: Dict[str, Dict]) -> str:
        """Generate comprehensive coverage report"""
        analysis = self.analyze_documentation_coverage(epic_data)
        
        report = "📚 DOCUMENTATION GENERATION COVERAGE REPORT\n"
        report += "=" * 60 + "\n\n"
        
        # Summary
        ready_docs = sum(1 for doc_info in analysis['document_readiness'].values() if doc_info['can_generate'])
        total_docs = len(analysis['document_readiness'])
        
        report += f"📊 SUMMARY:\n"
        report += f"Available Epics: {len(analysis['available_epics'])}\n"
        report += f"Documents Ready to Generate: {ready_docs}/{total_docs}\n"
        report += f"Documentation Coverage: {round((ready_docs/total_docs)*100, 1)}%\n\n"
        
        # Document readiness breakdown
        report += "📋 DOCUMENT READINESS:\n\n"
        
        ready_docs_list = []
        needs_work_docs = []
        
        for doc_type, doc_info in analysis['document_readiness'].items():
            status_icon = "✅" if doc_info['can_generate'] else "⚠️" if doc_info['overall_readiness'] >= 50 else "❌"
            
            doc_line = f"{status_icon} {doc_type}: {doc_info['overall_readiness']}% ready"
            
            if doc_info['can_generate']:
                ready_docs_list.append(doc_line)
            else:
                needs_work_docs.append(doc_line)
                if doc_info['missing_epics']:
                    needs_work_docs.append(f"    Missing Epics: {', '.join(doc_info['missing_epics'])}")
                if doc_info['missing_elements']:
                    needs_work_docs.append(f"    Additional Needs: {', '.join(doc_info['missing_elements'][:2])}...")
        
        # Show ready documents first
        if ready_docs_list:
            report += "🎉 READY TO GENERATE:\n"
            for doc in ready_docs_list:
                report += f"  {doc}\n"
            report += "\n"
        
        # Show documents needing work
        if needs_work_docs:
            report += "🔧 NEEDS ENHANCEMENT:\n"
            for doc in needs_work_docs:
                report += f"  {doc}\n"
            report += "\n"
        
        # Enhancement suggestions
        if analysis['enhancement_suggestions']:
            report += "💡 ENHANCEMENT SUGGESTIONS:\n"
            for suggestion in analysis['enhancement_suggestions']:
                report += f"  • {suggestion}\n"
            report += "\n"
        
        # Missing Epics
        if analysis['missing_epics_needed']:
            report += "📝 MISSING EPICS TO CREATE:\n"
            for epic in analysis['missing_epics_needed']:
                report += f"  • {epic}\n"
        
        return report

# Example usage with your Epic structure
def demo_multi_document_generation():
    """Demonstrate multi-document generation capabilities"""
    
    # Sample Epic data based on your structure
    sample_epic_data = {
        "Introduction to Extreme Platform ONE": {
            "Description": "Extreme Platform ONE is a unified touchpoint for Extreme Networks applications, simplifying the user experience and providing automation at scale. Key features include comprehensive UI, real-time notifications, contextual AI support, and single sign-on (SSO) capabilities.",
            "Target Version": "25.3.0"
        },
        "Supported Applications": {
            "Description": "ExtremeCloud IQ: Centralized configuration and network monitoring. ExtremeCloud SD-WAN: Unified wired and wireless management. ExtremeCloud Universal ZTNA: Network, application, and device access security. ExtremeCloud Intuitive Insights: Cloud-based deployment and monitoring of Zebra hand-held devices.",
            "Target Version": "25.3.0"
        },
        "Prerequisites": {
            "Description": "Supported Device OS Version: VOSS or Fabric Engine devices must be 9.1.0.1 or later; EXOS or Switch Engine must be 33.2.1.12 or later. Supported Devices: Access Point, Switch Engine (various models), Fabric Engine (various models), Non-universal EXOS SKUs (various models), VOSS SKUs (various models).",
            "Target Version": "25.3.0"
        },
        "Features Supported for this Release": {
            "Description": "Feature: Backup & Restore | Description: Manual backup and restore for Virtual IQ. Feature: Subscriptions & Licensing | Description: View subscriptions and licenses for all cloud-based applications in one place.",
            "Target Version": "25.3.0"
        },
        "Known Issues and Limitations": {
            "Description": "Trial Subscriptions are only available for SD-WAN, ExtremeCloud IQ, and Extreme Intuitive Insights subscriptions. Intermittent issue - the topology gets distorted while changing any node position.",
            "Target Version": "25.3.0"
        }
    }
    
    generator = MultiDocumentGenerator()
    
    # Generate coverage report
    print(generator.generate_coverage_report(sample_epic_data))
    
    # Generate specific documents
    print("\n" + "="*60)
    print("SAMPLE GENERATED DOCUMENT:")
    print("="*60)
    
    getting_started = generator.generate_document(DocumentType.GETTING_STARTED, sample_epic_data)
    print(getting_started)

if __name__ == "__main__":
    demo_multi_document_generation()
