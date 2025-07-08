#!/usr/bin/env python3
"""
Immediate Testing Script for Your JIRA Exports
Test the documentation analysis against your existing markdown files and folder structure
"""

import os
import re
import json
from typing import Dict, List, Any
from dataclasses import dataclass
from pathlib import Path

@dataclass
class AttachmentAnalysis:
    filename: str
    file_type: str
    documentation_value: str
    size_kb: int
    suggestions: List[str]

class JiraExportAnalyzer:
    """
    Analyze your existing JIRA export files (.md) and attachment folders
    This works with the structure you showed: specific_issues/NVO-3613/files...
    """
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        
    def analyze_exported_epic(self, md_file_path: str) -> Dict[str, Any]:
        """
        Analyze a single Epic from your markdown exports
        Works with files like XCO-10595.md, XCO-11218.md, XIQ-5896.md
        """
        md_path = Path(md_file_path)
        
        if not md_path.exists():
            return {"error": f"File not found: {md_file_path}"}
        
        # Parse the markdown content
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract Epic data using your existing structure
        epic_data = self._parse_markdown_epic(content, md_path.stem)
        
        # Look for associated attachment folder
        attachment_folder = self._find_attachment_folder(md_path.stem)
        
        # Analyze attachments if folder exists
        attachment_analysis = []
        if attachment_folder:
            attachment_analysis = self._analyze_attachment_folder(attachment_folder)
        
        # Apply documentation quality analysis
        doc_analysis = self._analyze_documentation_quality(epic_data, attachment_analysis)
        
        return {
            'epic_key': md_path.stem,
            'epic_data': epic_data,
            'attachment_analysis': attachment_analysis,
            'documentation_analysis': doc_analysis,
            'attachment_folder': str(attachment_folder) if attachment_folder else None
        }
    
    def _parse_markdown_epic(self, content: str, epic_key: str) -> Dict[str, Any]:
        """Parse Epic data from your markdown format"""
        epic_data = {'key': epic_key}
        
        # Extract title/summary
        title_match = re.search(r'^# (.+)', content, re.MULTILINE)
        if title_match:
            epic_data['Summary'] = title_match.group(1).replace(f"{epic_key} - ", "")
        
        # Extract description (usually the first major section)
        desc_match = re.search(r'### Description.*?\n(.*?)\n### ', content, re.DOTALL)
        if desc_match:
            epic_data['Description'] = desc_match.group(1).strip()
        else:
            # Fallback: look for description in field list
            desc_match = re.search(r'Description.*?\n(.*?)(?=\n###|\n\n|\Z)', content, re.DOTALL)
            if desc_match:
                epic_data['Description'] = desc_match.group(1).strip()
        
        # Extract Epic Name (custom field)
        epic_name_match = re.search(r'Epic Name.*?`([^`]+)`', content)
        if epic_name_match:
            epic_data['Epic Name'] = epic_name_match.group(1)
        
        # Extract target version
        version_match = re.search(r'Target Version.*?`([^`]+)`', content)
        if not version_match:
            version_match = re.search(r'Fix Version.*?`([^`]+)`', content)
        if version_match:
            epic_data['Target Version'] = version_match.group(1)
        
        # Extract components
        component_match = re.search(r'Component.*?\n.*?name.*?([^,\n]+)', content)
        if component_match:
            epic_data['Component'] = component_match.group(1).strip()
        
        # Extract issue type
        type_match = re.search(r'Issue Type.*?name.*?([^,\n]+)', content)
        if type_match:
            epic_data['Issue Type'] = type_match.group(1).strip()
        
        # Extract acceptance criteria if present
        ac_match = re.search(r'Acceptance Criteria.*?\n(.*?)(?=\n###|\n\n|\Z)', content, re.DOTALL)
        if ac_match:
            epic_data['Acceptance Criteria'] = ac_match.group(1).strip()
        
        # Look for attachments section
        attachments = []
        if "## Attachments" in content:
            attachment_section = content.split("## Attachments")[1]
            attachment_lines = re.findall(r'- \[([^\]]+)\]', attachment_section)
            attachments = [{'filename': name} for name in attachment_lines]
        
        epic_data['Attachments'] = attachments
        
        return epic_data
    
    def _find_attachment_folder(self, epic_key: str) -> Path:
        """
        Find attachment folder for Epic
        Looks for patterns like: specific_issues/NVO-3613/, specific_issues/XIQ-31955/
        """
        
        # Check if there's a specific_issues folder
        specific_issues_path = self.base_path / "specific_issues"
        if specific_issues_path.exists():
            # Look for folder matching the Epic key
            for folder in specific_issues_path.iterdir():
                if folder.is_dir() and epic_key in folder.name:
                    return folder
        
        # Check for folder with same name as Epic in base path
        epic_folder = self.base_path / epic_key
        if epic_folder.exists():
            return epic_folder
        
        return None
    
    def _analyze_attachment_folder(self, folder_path: Path) -> List[AttachmentAnalysis]:
        """
        Analyze attachment folder like your NVO-3613 example:
        - Images (PNG files)
        - Logs (.txt, .har files)  
        - Documents (.md files)
        """
        
        attachments = []
        
        for file_path in folder_path.rglob("*"):
            if file_path.is_file():
                file_analysis = self._analyze_single_attachment(file_path)
                attachments.append(file_analysis)
        
        return attachments
    
    def _analyze_single_attachment(self, file_path: Path) -> AttachmentAnalysis:
        """Analyze a single attachment file"""
        filename = file_path.name.lower()
        file_size = file_path.stat().st_size / 1024  # Size in KB
        
        # Determine file type and documentation value
        if any(ext in filename for ext in ['.png', '.jpg', '.jpeg', '.gif']):
            if 'image-' in filename and any(time in filename for time in ['2024', '2025']):
                file_type = "screenshot"
                doc_value = "high"
                suggestions = ["Screenshots are excellent for user guides and troubleshooting docs"]
            else:
                file_type = "image"
                doc_value = "medium"
                suggestions = ["Consider adding captions or context for this image"]
                
        elif filename.endswith('.txt') or filename.endswith('.log'):
            if 'log' in filename or 'crash' in filename:
                file_type = "troubleshooting_log"
                doc_value = "medium"
                suggestions = ["Log files can be used to create troubleshooting guides"]
            else:
                file_type = "text_document"
                doc_value = "medium"
                suggestions = ["Text files may contain useful procedural information"]
                
        elif filename.endswith('.har'):
            file_type = "network_trace"
            doc_value = "low"
            suggestions = ["HAR files are mainly for debugging - consider extracting key insights"]
            
        elif filename.endswith('.md'):
            file_type = "documentation"
            doc_value = "very_high" 
            suggestions = ["Markdown files are perfect for documentation generation"]
            
        elif any(ext in filename for ext in ['.pdf', '.doc', '.docx']):
            file_type = "document"
            doc_value = "high"
            suggestions = ["Documents likely contain valuable specification or procedure information"]
            
        elif any(ext in filename for ext in ['.mp4', '.avi', '.mov']):
            file_type = "video"
            doc_value = "very_high"
            suggestions = ["Videos are excellent for training materials and user guides"]
            
        else:
            file_type = "unknown"
            doc_value = "unknown"
            suggestions = ["Unknown file type - review for potential documentation value"]
        
        return AttachmentAnalysis(
            filename=file_path.name,
            file_type=file_type,
            documentation_value=doc_value,
            size_kb=round(file_size, 1),
            suggestions=suggestions
        )
    
    def _analyze_documentation_quality(self, epic_data: Dict[str, Any], 
                                     attachments: List[AttachmentAnalysis]) -> Dict[str, Any]:
        """Apply your documentation quality framework to the Epic"""
        
        analysis = {
            'completeness_score': 0,
            'documentation_readiness': 'poor',
            'missing_elements': [],
            'strengths': [],
            'improvement_suggestions': []
        }
        
        # Analyze Epic description quality
        description = epic_data.get('Description', '')
        if description:
            if len(description) > 200:
                analysis['completeness_score'] += 30
                analysis['strengths'].append("Substantial description provided")
            elif len(description) > 50:
                analysis['completeness_score'] += 15
                analysis['improvement_suggestions'].append("Expand description with more detail")
            else:
                analysis['missing_elements'].append("Description too brief")
        else:
            analysis['missing_elements'].append("No description provided")
        
        # Check for user story format
        if 'as a' in description.lower() or 'user' in description.lower():
            analysis['completeness_score'] += 15
            analysis['strengths'].append("Contains user perspective")
        else:
            analysis['improvement_suggestions'].append("Add user story or user perspective")
        
        # Check for Epic Name
        if epic_data.get('Epic Name'):
            analysis['completeness_score'] += 10
        else:
            analysis['missing_elements'].append("Epic Name not specified")
        
        # Check for target version
        if epic_data.get('Target Version'):
            analysis['completeness_score'] += 10
        else:
            analysis['missing_elements'].append("Target Version not specified")
        
        # Check for components
        if epic_data.get('Component'):
            analysis['completeness_score'] += 5
        else:
            analysis['missing_elements'].append("Component not specified")
        
        # Analyze attachments
        if attachments:
            analysis['completeness_score'] += 15
            
            high_value_attachments = [a for a in attachments if a.documentation_value in ['high', 'very_high']]
            if high_value_attachments:
                analysis['completeness_score'] += 15
                analysis['strengths'].append(f"Contains {len(high_value_attachments)} high-value attachments")
            
            # Check for specific attachment types
            has_images = any(a.file_type in ['screenshot', 'image'] for a in attachments)
            has_docs = any(a.file_type in ['documentation', 'document'] for a in attachments)
            has_videos = any(a.file_type == 'video' for a in attachments)
            
            if has_images:
                analysis['strengths'].append("Contains visual materials (screenshots/images)")
            if has_docs:
                analysis['strengths'].append("Contains document attachments")
            if has_videos:
                analysis['strengths'].append("Contains video demonstrations")
                
        else:
            analysis['improvement_suggestions'].append("Add attachments (screenshots, docs, videos)")
        
        # Determine overall readiness
        score = analysis['completeness_score']
        if score >= 80:
            analysis['documentation_readiness'] = 'excellent'
        elif score >= 60:
            analysis['documentation_readiness'] = 'good'
        elif score >= 40:
            analysis['documentation_readiness'] = 'fair'
        else:
            analysis['documentation_readiness'] = 'poor'
        
        return analysis
    
    def batch_analyze_exports(self, export_folder: str) -> Dict[str, Any]:
        """
        Analyze all Epic markdown files in a folder
        Perfect for testing with your current JIRA exports
        """
        export_path = Path(export_folder)
        results = {
            'total_epics': 0,
            'epics_analyzed': [],
            'summary_stats': {
                'excellent': 0,
                'good': 0, 
                'fair': 0,
                'poor': 0,
                'with_attachments': 0,
                'high_value_attachments': 0
            }
        }
        
        # Find all markdown files that look like Epic exports
        epic_files = []
        for file_path in export_path.rglob("*.md"):
            # Look for files with Epic-like names (PROJECT-NUMBER format)
            if re.match(r'^[A-Z]+-\d+\.md$', file_path.name):
                epic_files.append(file_path)
        
        results['total_epics'] = len(epic_files)
        
        # Analyze each Epic
        for epic_file in epic_files:
            epic_analysis = self.analyze_exported_epic(str(epic_file))
            results['epics_analyzed'].append(epic_analysis)
            
            # Update summary stats
            doc_readiness = epic_analysis['documentation_analysis']['documentation_readiness']
            results['summary_stats'][doc_readiness] += 1
            
            if epic_analysis['attachment_analysis']:
                results['summary_stats']['with_attachments'] += 1
                
                high_value = [a for a in epic_analysis['attachment_analysis'] 
                            if a.documentation_value in ['high', 'very_high']]
                if high_value:
                    results['summary_stats']['high_value_attachments'] += 1
        
        return results

# Quick test function for your current data
def test_your_current_exports():
    """
    Test this immediately with your current JIRA export files
    """
    
    # Adjust this path to where your JIRA exports are located
    analyzer = JiraExportAnalyzer("/path/to/your/jira/exports")
    
    # Test individual Epics (adjust paths to your actual files)
    test_epics = [
        "XCO-10595.md",
        "XCO-11218.md", 
        "XIQ-5896.md"
    ]
    
    print("🧪 TESTING YOUR CURRENT JIRA EXPORTS")
    print("=" * 50)
    
    for epic_file in test_epics:
        print(f"\n--- Analyzing {epic_file} ---")
        
        try:
            analysis = analyzer.analyze_exported_epic(epic_file)
            
            if 'error' not in analysis:
                epic_data = analysis['epic_data']
                doc_analysis = analysis['documentation_analysis']
                attachments = analysis['attachment_analysis']
                
                print(f"Epic: {epic_data.get('Epic Name', 'No Name')}")
                print(f"Description Length: {len(epic_data.get('Description', ''))}")
                print(f"Documentation Readiness: {doc_analysis['documentation_readiness']}")
                print(f"Completeness Score: {doc_analysis['completeness_score']}%")
                print(f"Attachments: {len(attachments)}")
                
                if doc_analysis['strengths']:
                    print("Strengths:")
                    for strength in doc_analysis['strengths']:
                        print(f"  ✅ {strength}")
                
                if doc_analysis['improvement_suggestions']:
                    print("Suggestions:")
                    for suggestion in doc_analysis['improvement_suggestions'][:2]:
                        print(f"  💡 {suggestion}")
                        
            else:
                print(f"❌ {analysis['error']}")
                
        except Exception as e:
            print(f"❌ Error analyzing {epic_file}: {e}")
    
    # Test batch analysis
    print(f"\n🎯 BATCH ANALYSIS")
    try:
        batch_results = analyzer.batch_analyze_exports(".")
        
        print(f"Total Epics Found: {batch_results['total_epics']}")
        stats = batch_results['summary_stats']
        print(f"Documentation Quality Distribution:")
        print(f"  Excellent: {stats['excellent']}")
        print(f"  Good: {stats['good']}")
        print(f"  Fair: {stats['fair']}")
        print(f"  Poor: {stats['poor']}")
        print(f"With Attachments: {stats['with_attachments']}")
        print(f"High-Value Attachments: {stats['high_value_attachments']}")
        
    except Exception as e:
        print(f"❌ Batch analysis error: {e}")

if __name__ == "__main__":
    test_your_current_exports()
