#!/usr/bin/env python3
"""
HTML Email to Social Media Post Converter
Extracts content from HTML emails and formats for LinkedIn/Facebook posting
"""

import os
import re
import glob
from bs4 import BeautifulSoup
from pathlib import Path
import argparse

class EmailToSocialConverter:
    def __init__(self):
        # Emoji mappings for different pain points/benefits
        self.emoji_map = {
            'production': '🔥',
            'fire': '🔥',
            'bugs': '🐛',
            'balance': '⚖️',
            'feature': '⚖️',
            'documentation': '📝',
            'docs': '📝',
            'knowledge': '🧠',
            'blind': '🤔',
            'confused': '🤔',
            'monitoring': '📊',
            'test': '✅',
            'coverage': '✅',
            'confidence': '✅',
            'deploy': '🚀',
            'automation': '🤖',
            'ai': '🤖',
            'growth': '📈',
            'startup': '🚀',
            'scale': '📈'
        }
        
        # Unicode character mappings for formatting
        self.unicode_chars = {
            'bold': {
                'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵',
                'i': '𝗶', 'j': '𝗷', 'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽',
                'q': '𝗾', 'r': '𝗿', 's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅',
                'y': '𝘆', 'z': '𝘇', 'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙',
                'G': '𝗚', 'H': '𝗛', 'I': '𝗜', 'J': '𝗝', 'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡',
                'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩',
                'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭', '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯',
                '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'
            },
            'italic': {
                'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨', 'h': '𝘩',
                'i': '𝘪', 'j': '𝘫', 'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯', 'o': '𝘰', 'p': '𝘱',
                'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵', 'u': '𝘶', 'v': '𝘷', 'w': '𝘸', 'x': '𝘹',
                'y': '𝘺', 'z': '𝘻', 'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍',
                'G': '𝘎', 'H': '𝘏', 'I': '𝘐', 'J': '𝘑', 'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕',
                'O': '𝘖', 'P': '𝘗', 'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛', 'U': '𝘜', 'V': '𝘝',
                'W': '𝘞', 'X': '𝘟', 'Y': '𝘠', 'Z': '𝘡'
            }
        }
    
    def extract_content(self, html_file):
        """Extract key content sections from HTML email"""
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        content = {
            'subject': '',
            'hook': '',
            'stats': [],
            'pain_points': [],
            'features': [],
            'quote': '',
            'cta': '',
            'hashtags': []
        }
        
        # Extract subject/main headline
        hero_h1 = soup.find('h1')
        if hero_h1:
            content['subject'] = hero_h1.get_text().strip()
        
        # Extract hook (first paragraph after headline)
        hero_p = soup.find('div', class_='hero')
        if hero_p:
            p_tag = hero_p.find('p')
            if p_tag:
                content['hook'] = p_tag.get_text().strip()
        
        # Extract stats
        stats = soup.find_all('div', class_='stat-item')
        for stat in stats:
            number = stat.find('span', class_='stat-number')
            label = stat.find('div', class_='stat-label')
            if number and label:
                content['stats'].append({
                    'number': number.get_text().strip(),
                    'label': label.get_text().strip()
                })
        
        # Extract pain points
        pain_points = soup.find_all('div', class_='pain-point')
        for pain in pain_points:
            title = pain.find('div', class_='pain-title')
            desc = pain.find('div', class_='pain-desc')
            if title and desc:
                content['pain_points'].append({
                    'title': title.get_text().strip(),
                    'description': desc.get_text().strip()
                })
        
        # Extract features
        features = soup.find_all('div', class_='feature-item')
        for feature in features:
            title = feature.find('div', class_='feature-title')
            desc = feature.find('div', class_='feature-desc')
            if title and desc:
                content['features'].append({
                    'title': title.get_text().strip(),
                    'description': desc.get_text().strip()
                })
        
        # Extract quote
        quote_text = soup.find('div', class_='quote-text')
        quote_author = soup.find('div', class_='quote-author')
        if quote_text:
            content['quote'] = quote_text.get_text().strip()
            if quote_author:
                content['quote'] += f" - {quote_author.get_text().strip()}"
        
        # Extract CTA
        cta_button = soup.find('a', class_='cta-button')
        if cta_button:
            content['cta'] = cta_button.get_text().strip()
        
        return content
    
    def to_unicode_bold(self, text):
        """Convert text to Unicode bold characters"""
        result = ""
        for char in text:
            result += self.unicode_chars['bold'].get(char, char)
        return result
    
    def to_unicode_italic(self, text):
        """Convert text to Unicode italic characters"""
        result = ""
        for char in text:
            result += self.unicode_chars['italic'].get(char, char)
        return result
    
    def add_emoji(self, text):
        """Add relevant emoji based on text content"""
        text_lower = text.lower()
        for keyword, emoji in self.emoji_map.items():
            if keyword in text_lower:
                return f"{emoji} {text}"
        return f"• {text}"  # Default bullet if no emoji match
    
    def format_for_social(self, content):
        """Format extracted content for LinkedIn/Facebook posting (with Unicode formatting)"""
        
        # Start with hook
        post = f"{self.to_unicode_bold(self.add_emoji(content['subject']))}\n\n"
        
        if content['hook']:
            # Break hook into short lines for mobile readability
            hook_lines = content['hook'].split('. ')
            for line in hook_lines:
                if line.strip():
                    post += f"{line.strip()}{'.' if not line.endswith('.') else ''}\n\n"
        
        # Add stats if available
        if content['stats']:
            post += f"{self.to_unicode_bold('Here\\'s what\\'s possible:')}\n\n"
            for stat in content['stats']:
                post += f"✅ {self.to_unicode_bold(stat['number'] + ' ' + stat['label'].lower())}\n"
            post += "\n"
        
        # Add pain points
        if content['pain_points']:
            post += f"{self.to_unicode_bold('The challenge:')}\n\n"
            for i, pain in enumerate(content['pain_points'][:3]):  # Limit to 3 for readability
                emoji_title = self.add_emoji(pain['title'])
                post += f"{emoji_title} - {pain['description']}\n\n"
        
        # Add features/benefits
        if content['features']:
            post += f"{self.to_unicode_bold('The solution:')}\n\n"
            for feature in content['features'][:3]:  # Limit to 3
                emoji_title = self.add_emoji(feature['title'])
                post += f"✅ {self.to_unicode_bold(emoji_title)} - {feature['description']}\n\n"
        
        # Add quote if available
        if content['quote']:
            post += f"{self.to_unicode_bold('What others say:')}\n\n{self.to_unicode_italic('\"' + content['quote'] + '\"')}\n\n"
        
        # Add CTA
        if content['cta']:
            post += f"{self.to_unicode_bold(content['cta'])}\n\n"
            post += "Link in comments 👇\n\n"
        
        # Add engagement hook
        post += "What's your experience with this? Share below!\n\n"
        
        # Add hashtags
        hashtags = self.generate_hashtags(content)
        post += " ".join(hashtags)
        
        return post
    
    def generate_hashtags(self, content):
        """Generate relevant hashtags based on content"""
        base_hashtags = ["#StartupLife", "#TechLeadership", "#ProductDevelopment"]
        
        # Add context-specific hashtags
        text_content = f"{content['subject']} {content['hook']}".lower()
        
        if 'production' in text_content or 'fire' in text_content:
            base_hashtags.append("#ProductionIssues")
        if 'tech debt' in text_content or 'debt' in text_content:
            base_hashtags.append("#TechDebt")
        if 'cto' in text_content or 'engineering' in text_content:
            base_hashtags.append("#StartupCTO")
        if 'ai' in text_content or 'automation' in text_content:
            base_hashtags.append("#AITools")
        if 'test' in text_content or 'coverage' in text_content:
            base_hashtags.append("#SoftwareTesting")
        
        return base_hashtags[:8]  # LinkedIn recommends 3-5, but up to 8 is fine
    
    def process_folder(self, folder_path, output_folder=None):
        """Process all HTML files in a folder"""
        folder_path = Path(folder_path)
        if output_folder:
            output_folder = Path(output_folder)
            output_folder.mkdir(exist_ok=True)
        else:
            output_folder = folder_path / "social_posts"
            output_folder.mkdir(exist_ok=True)
        
        html_files = glob.glob(str(folder_path / "*.html"))
        
        for html_file in html_files:
            print(f"Processing: {html_file}")
            
            try:
                content = self.extract_content(html_file)
                social_post = self.format_for_social(content)
                
                # Save to output file
                output_file = output_folder / f"{Path(html_file).stem}_social_post.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(social_post)
                
                print(f"✅ Generated: {output_file}")
                
            except Exception as e:
                print(f"❌ Error processing {html_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert HTML emails to social media posts")
    parser.add_argument("input_folder", help="Folder containing HTML email files")
    parser.add_argument("-o", "--output", help="Output folder for social posts (default: input_folder/social_posts)")
    parser.add_argument("-f", "--file", help="Process single file instead of folder")
    
    args = parser.parse_args()
    
    converter = EmailToSocialConverter()
    
    if args.file:
        # Process single file
        content = converter.extract_content(args.file)
        social_post = converter.format_for_social(content)
        print(social_post)
    else:
        # Process folder
        converter.process_folder(args.input_folder, args.output)

if __name__ == "__main__":
    main()
