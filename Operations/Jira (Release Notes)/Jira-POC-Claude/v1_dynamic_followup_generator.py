#!/usr/bin/env python3
"""
Dynamic Follow-up Question Generator
Generates tailored questions based on what's missing from Epic documentation
"""

from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
from enum import Enum

class QuestionType(Enum):
    CRITICAL = "Critical"  # Blocks documentation
    IMPORTANT = "Important"  # Significantly improves documentation
    HELPFUL = "Helpful"  # Nice to have for complete documentation

class ActionComplexity(Enum):
    QUICK = "Quick (5-10 minutes)"
    MODERATE = "Moderate (30-60 minutes)" 
    INVOLVED = "Involved (2+ hours)"

@dataclass
class FollowUpQuestion:
    question: str
    rationale: str
    question_type: QuestionType
    complexity: ActionComplexity
    easy_alternatives: List[str]
    examples: List[str]

class EpicDocumentationAnalyzer:
    def __init__(self):
        # Define what makes epic documentation complete
        self.epic_requirements = {
            'user_story': {
                'patterns': [r'as a .* i want .* so that', r'given .* when .* then'],
                'field_sources': ['description', 'acceptance_criteria']
            },
            'business_value': {
                'patterns': [r'business|value|roi|cost|save|revenue|customer|impact'],
                'field_sources': ['description', 'business_context']
            },
            'user_workflows': {
                'patterns': [r'workflow|process|step|journey|use case'],
                'field_sources': ['description', 'acceptance_criteria']
            },
            'success_metrics': {
                'patterns': [r'metric|measure|kpi|target|goal|success'],
                'field_sources': ['description', 'definition_of_done']
            },
            'target_users': {
                'patterns': [r'user|admin|customer|operator|manager'],
                'field_sources': ['description', 'acceptance_criteria']
            },
            'technical_scope': {
                'patterns': [r'api|service|component|system|integration'],
                'field_sources': ['description', 'technical_details']
            }
        }

    def analyze_epic_gaps(self, epic_data: Dict) -> Dict[str, Any]:
        """Analyze what's missing from Epic documentation"""
        gaps = {
            'missing_elements': [],
            'weak_elements': [],
            'content_analysis': {}
        }
        
        # Extract text content from key fields
        description = epic_data.get('Description', '')
        acceptance_criteria = epic_data.get('Acceptance Criteria', '')
        epic_name = epic_data.get('Epic Name', '')
        
        combined_text = f"{epic_name} {description} {acceptance_criteria}".lower()
        
        # Check each requirement
        for requirement, config in self.epic_requirements.items():
            found_patterns = []
            for pattern in config['patterns']:
                if self._find_pattern(pattern, combined_text):
                    found_patterns.append(pattern)
            
            if not found_patterns:
                gaps['missing_elements'].append(requirement)
            elif len(found_patterns) < len(config['patterns']) / 2:
                gaps['weak_elements'].append(requirement)
            
            gaps['content_analysis'][requirement] = {
                'found_patterns': len(found_patterns),
                'total_patterns': len(config['patterns']),
                'strength': 'strong' if len(found_patterns) >= len(config['patterns']) / 2 else 'weak'
            }
        
        # Check for attachments/supporting materials
        attachments = epic_data.get('Attachment', [])
        gaps['has_attachments'] = len(attachments) > 0
        gaps['attachment_types'] = self._analyze_attachments(attachments)
        
        return gaps

    def _find_pattern(self, pattern: str, text: str) -> bool:
        """Check if pattern exists in text"""
        import re
        return bool(re.search(pattern, text, re.IGNORECASE))

    def _analyze_attachments(self, attachments: List) -> Dict[str, int]:
        """Analyze types of attachments present"""
        attachment_types = {
            'images': 0,
            'documents': 0,
            'videos': 0,
            'specs': 0
        }
        
        for attachment in attachments:
            filename = attachment.get('filename', '').lower()
            mime_type = attachment.get('mimeType', '').lower()
            
            if any(ext in filename for ext in ['.png', '.jpg', '.jpeg', '.gif']) or 'image' in mime_type:
                attachment_types['images'] += 1
            elif any(ext in filename for ext in ['.pdf', '.doc', '.docx']):
                attachment_types['documents'] += 1
            elif any(ext in filename for ext in ['.mp4', '.avi', '.mov']) or 'video' in mime_type:
                attachment_types['videos'] += 1
            elif any(ext in filename for ext in ['.yaml', '.json', '.spec']):
                attachment_types['specs'] += 1
        
        return attachment_types

    def generate_follow_up_questions(self, epic_data: Dict) -> List[FollowUpQuestion]:
        """Generate dynamic follow-up questions based on gaps"""
        gaps = self.analyze_epic_gaps(epic_data)
        questions = []
        
        epic_name = epic_data.get('Epic Name', 'this epic')
        
        # Generate questions for missing elements
        for missing_element in gaps['missing_elements']:
            question_config = self._get_question_config(missing_element, epic_name)
            if question_config:
                questions.append(question_config)
        
        # Generate questions for weak elements
        for weak_element in gaps['weak_elements']:
            question_config = self._get_improvement_question_config(weak_element, epic_name)
            if question_config:
                questions.append(question_config)
        
        # Add attachment-related questions
        if not gaps['has_attachments']:
            questions.append(self._get_attachment_question(epic_name))
        
        # Sort by priority (Critical first, then Important, then Helpful)
        questions.sort(key=lambda q: (q.question_type.value, q.complexity.value))
        
        return questions

    def _get_question_config(self, missing_element: str, epic_name: str) -> FollowUpQuestion:
        """Get question configuration for missing elements"""
        
        question_configs = {
            'user_story': FollowUpQuestion(
                question=f"Who are the primary users of {epic_name} and what specific value does it provide them?",
                rationale="User stories help documentation writers understand the audience and craft user-focused content. Without this, documentation becomes technical and hard to understand.",
                question_type=QuestionType.CRITICAL,
                complexity=ActionComplexity.MODERATE,
                easy_alternatives=[
                    "📝 Fill out this template: 'As a [user type] I want [capability] so that [benefit]'",
                    "🎥 Record a 3-minute video explaining who would use this feature and why",
                    "📋 Upload existing user research or requirements documents",
                    "💬 Schedule a 15-minute call with the product owner"
                ],
                examples=[
                    "'As a network administrator I want unified dashboard views so that I can monitor multiple tenants without switching interfaces'",
                    "'As a customer success manager I want automated reporting so that I can provide proactive service updates'"
                ]
            ),
            
            'business_value': FollowUpQuestion(
                question=f"What business problem does {epic_name} solve and what's the expected impact?",
                rationale="Business value helps justify the feature in documentation and helps users understand when/why to use it.",
                question_type=QuestionType.CRITICAL,
                complexity=ActionComplexity.QUICK,
                easy_alternatives=[
                    "💰 Specify cost savings, revenue impact, or efficiency gains",
                    "📊 Share any ROI calculations or business case documents",
                    "📈 Provide metrics like 'reduces time by X%' or 'increases capacity by Y'",
                    "🎯 Link to OKRs or business objectives this epic supports"
                ],
                examples=[
                    "'Reduces mean time to detection from 25 to 10 minutes (60% improvement)'",
                    "'Eliminates need for 50+ separate login sessions, saving 2 hours/day per admin'"
                ]
            ),
            
            'user_workflows': FollowUpQuestion(
                question=f"What are the key workflows or processes that users will follow with {epic_name}?",
                rationale="User workflows become the foundation for user guides, tutorials, and help documentation.",
                question_type=QuestionType.IMPORTANT,
                complexity=ActionComplexity.MODERATE,
                easy_alternatives=[
                    "🎬 Record a screen demo showing the main user journey (even if prototype)",
                    "📝 List the step-by-step process users will follow",
                    "🖼️ Upload screenshots or wireframes of key screens",
                    "📋 Attach existing process documentation or user flows"
                ],
                examples=[
                    "'Daily monitoring: Login → View dashboard → Check alerts → Drill down to issues'",
                    "'Setup: Configure tenants → Set thresholds → Customize layout → Save preferences'"
                ]
            ),
            
            'success_metrics': FollowUpQuestion(
                question=f"How will you measure if {epic_name} is successful? What metrics will you track?",
                rationale="Success metrics help create measurable outcomes in documentation and help users understand expected results.",
                question_type=QuestionType.IMPORTANT,
                complexity=ActionComplexity.QUICK,
                easy_alternatives=[
                    "📊 List 2-3 key metrics you'll track after release",
                    "🎯 Specify target improvements (e.g., '50% faster', '90% reduction')",
                    "📈 Share existing baseline metrics if available",
                    "💡 Describe what 'good adoption' looks like for users"
                ],
                examples=[
                    "'User adoption: 80% of admins using new dashboard within 30 days'",
                    "'Performance: Average response time < 3 seconds for dashboard loads'"
                ]
            ),
            
            'target_users': FollowUpQuestion(
                question=f"Who specifically will use {epic_name}? What are their roles and technical skill levels?",
                rationale="Understanding the audience helps writers choose appropriate language, depth, and format for documentation.",
                question_type=QuestionType.CRITICAL,
                complexity=ActionComplexity.QUICK,
                easy_alternatives=[
                    "👥 List primary and secondary user personas",
                    "🎯 Specify technical skill level (beginner/intermediate/advanced)",
                    "📋 Share existing persona documents or user research",
                    "💼 Describe typical job responsibilities of target users"
                ],
                examples=[
                    "'Primary: Network Operations Center (NOC) technicians - intermediate technical skills'",
                    "'Secondary: Service delivery managers - business focus, basic technical knowledge'"
                ]
            ),
            
            'technical_scope': FollowUpQuestion(
                question=f"What are the key technical components, APIs, or integrations involved in {epic_name}?",
                rationale="Technical scope helps create implementation guides, API documentation, and troubleshooting content.",
                question_type=QuestionType.HELPFUL,
                complexity=ActionComplexity.MODERATE,
                easy_alternatives=[
                    "🏗️ Upload architecture diagrams or technical specifications",
                    "📱 List main APIs, services, or components involved",
                    "🔗 Identify key integrations with existing systems",
                    "📋 Attach technical design documents if available"
                ],
                examples=[
                    "'REST APIs for data aggregation, WebSocket for real-time updates, SSO integration'",
                    "'New microservices: analytics-engine, dashboard-service, notification-gateway'"
                ]
            )
        }
        
        return question_configs.get(missing_element)

    def _get_improvement_question_config(self, weak_element: str, epic_name: str) -> FollowUpQuestion:
        """Get questions to improve weak elements"""
        
        improvement_configs = {
            'user_story': FollowUpQuestion(
                question=f"Can you provide more specific details about the user benefits of {epic_name}?",
                rationale="The current user story could be more detailed to help writers create compelling user-focused content.",
                question_type=QuestionType.IMPORTANT,
                complexity=ActionComplexity.QUICK,
                easy_alternatives=[
                    "✨ Add specific benefits: 'so that I can save 2 hours per day'",
                    "📝 Describe the pain point this solves",
                    "🎯 Quantify the improvement users will experience"
                ],
                examples=["Instead of 'better monitoring', say 'monitor 50+ tenants from one dashboard instead of logging into each separately'"]
            ),
            
            'business_value': FollowUpQuestion(
                question=f"Can you quantify the business impact of {epic_name} with specific numbers or percentages?",
                rationale="Adding specific metrics makes the business case more compelling in documentation.",
                question_type=QuestionType.IMPORTANT,
                complexity=ActionComplexity.QUICK,
                easy_alternatives=[
                    "📊 Add percentage improvements or time savings",
                    "💰 Include cost reduction or revenue impact numbers",
                    "📈 Specify user productivity gains"
                ],
                examples=["'Reduces manual effort by 40%', 'Improves response time from 30 to 5 minutes'"]
            )
        }
        
        return improvement_configs.get(weak_element)

    def _get_attachment_question(self, epic_name: str) -> FollowUpQuestion:
        """Generate question about missing attachments"""
        return FollowUpQuestion(
            question=f"Do you have any visual materials, specifications, or demos that would help explain {epic_name}?",
            rationale="Visual materials significantly improve documentation quality and user understanding.",
            question_type=QuestionType.HELPFUL,
            complexity=ActionComplexity.QUICK,
            easy_alternatives=[
                "📸 Upload screenshots of key screens or workflows",
                "🎥 Record a quick demo video (even from prototype/staging)",
                "📋 Attach technical specifications or requirements documents", 
                "🖼️ Include wireframes, mockups, or architecture diagrams",
                "📊 Share user research findings or competitive analysis"
            ],
            examples=[
                "Dashboard screenshots showing before/after views",
                "5-minute demo video of the main user workflow",
                "Technical architecture diagram showing component relationships"
            ]
        )

    def format_questions_for_user(self, questions: List[FollowUpQuestion], epic_id: str) -> str:
        """Format questions in a user-friendly way"""
        if not questions:
            return f"✅ Great! Epic {epic_id} has solid documentation for product docs creation."
        
        output = f"\n📝 **Epic {epic_id} - Documentation Improvement Suggestions**\n"
        output += "=" * 60 + "\n\n"
        
        # Group by priority
        critical_questions = [q for q in questions if q.question_type == QuestionType.CRITICAL]
        important_questions = [q for q in questions if q.question_type == QuestionType.IMPORTANT]
        helpful_questions = [q for q in questions if q.question_type == QuestionType.HELPFUL]
        
        if critical_questions:
            output += "🚨 **CRITICAL - Needed for basic documentation:**\n\n"
            for i, q in enumerate(critical_questions, 1):
                output += self._format_single_question(q, i)
        
        if important_questions:
            output += "\n⚠️ **IMPORTANT - Significantly improves documentation:**\n\n"
            for i, q in enumerate(important_questions, 1):
                output += self._format_single_question(q, i)
        
        if helpful_questions:
            output += "\n💡 **HELPFUL - Nice to have for complete documentation:**\n\n"
            for i, q in enumerate(helpful_questions, 1):
                output += self._format_single_question(q, i)
        
        output += "\n" + "=" * 60
        output += "\n💼 **Quick Win Suggestions:** Focus on the easy alternatives above - many can be completed in under 30 minutes!"
        
        return output

    def _format_single_question(self, question: FollowUpQuestion, number: int) -> str:
        """Format a single question with alternatives"""
        output = f"**{number}. {question.question}**\n"
        output += f"   *Why this helps:* {question.rationale}\n"
        output += f"   *Time needed:* {question.complexity.value}\n\n"
        
        output += "   **Easy alternatives:**\n"
        for alternative in question.easy_alternatives:
            output += f"   • {alternative}\n"
        
        if question.examples:
            output += f"\n   **Examples:**\n"
            for example in question.examples:
                output += f"   • {example}\n"
        
        output += "\n"
        return output

# Example usage
def analyze_epic_documentation(epic_data: Dict) -> str:
    """Main function to analyze epic and generate questions"""
    analyzer = EpicDocumentationAnalyzer()
    questions = analyzer.generate_follow_up_questions(epic_data)
    epic_id = epic_data.get('key', 'UNKNOWN')
    
    return analyzer.format_questions_for_user(questions, epic_id)

# Test with sample incomplete epic
if __name__ == "__main__":
    # Sample incomplete epic (like your XCO-11218 example)
    incomplete_epic = {
        'key': 'XCO-11218',
        'Epic Name': 'Tenant : VRF : Release Documentation',
        'Description': 'Tenant : VRF : Release Documentation',
        'Issue Type': {'name': 'Story'},
        'Acceptance Criteria': '',
        'Attachment': []
    }
    
    print(analyze_epic_documentation(incomplete_epic))
