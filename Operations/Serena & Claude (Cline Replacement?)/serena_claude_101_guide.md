# Serena with Claude 101: Complete First-Time User Guide

## Table of Contents
1. [What is Serena?](#what-is-serena)
2. [Initial Setup](#initial-setup)
3. [Basic Workflow](#basic-workflow)
4. [Advanced Strategies](#advanced-strategies)
5. [Team Collaboration](#team-collaboration)
6. [Common Use Cases](#common-use-cases)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

## What is Serena?

Serena is an MCP (Model Context Protocol) server that acts as a bridge between Claude and your local code repositories. It provides:

- **Language Server Protocol (LSP) integration** - Enables precise, targeted code edits instead of regex replacements
- **Abstract Syntax Tree (AST) analysis** - Understands code structure for accurate line-by-line modifications
- **Memory management** - Maintains project context and progress across chat sessions
- **Repository indexing** - Builds comprehensive understanding of your codebase structure

### Why Serena Over Plain Claude?

**Without Serena:** Claude does simple regex replacements and needs extensive context for each edit
**With Serena:** Claude can make surgical edits like "on line #13, update this specific line to that line"

## Initial Setup

### 1. Installation
```bash
# Clone Serena MCP server locally (recommended for enterprise security)
git clone [serena-mcp-server-repo]
cd serena-mcp-server

# Add to your MCP config
# Point to local server, not remote hosted instance
```

### 2. Repository Preparation
**CRITICAL:** Always work with clean repositories

```bash
# Create a clean branch before starting
git checkout -b feature/your-task-name
git status  # Ensure no untracked files

# Clone locally (never download ZIP)
# This maintains version history and enables proper collaboration
```

### 3. First Connection
In Claude, simply say:
```
"Look at this folder and be ready for my instructions"
```
Serena will:
- Index your repository
- Analyze the tech stack
- Create a `.serena` folder with project metadata
- Build understanding of file structure and dependencies

## Basic Workflow

### Step 1: Planning Phase
**Never jump straight to implementation**

```
"This codebase is not [feature] compatible. Think hard about a comprehensive plan for how to convert this. Give me 3-5 strategies that are relevant."
```

**Example for i18n:**
```
"The codebase is not i18n compatible at all. Check out a plan for how to make it internationalization-ready. Think hard and give me multiple strategies."
```

### Step 2: Strategy Validation
```
"This is how I'm thinking I want to implement [feature]. Please validate this strategy and challenge me if you think something seems wrong."
```

### Step 3: Implementation Planning
Once you approve the strategy:
```
"I'm fine with this approach. Create a progress document in memory and break this down into specific tasks by phase. Show me which files and folders will be affected in each phase."
```

### Step 4: Controlled Execution
```
"Start with Phase 1 and always keep updating the memory file when you're done with any action. Do not progress to the next task until you get my confirmation to continue."
```

## Advanced Strategies

### Memory Management
Serena creates progress files in `.serena/` folder that allow you to:
- **Resume work** across different chat sessions
- **Track progress** through complex multi-file changes
- **Collaborate** with team members on the same codebase

### Starting New Chat Sessions
When you hit context limits:
1. Start a new Claude chat
2. Say: "Look at this folder and be ready"
3. Serena will automatically detect existing progress and say: "I see you have an ongoing project at 30% completion. Let me continue from where we left off."

### Batching Strategy
For large codebases:
```
"I see you've identified 50 files to update. Batch this into groups of 3-5 files at a time and wait for my review after each batch before continuing."
```

## Team Collaboration

### Multi-Developer Workflow

#### Scenario 1: Sequential Work
1. **Developer A** completes Phase 1, commits to branch
2. **Developer B** clones that branch (includes `.serena` folder)
3. **Developer B** tells Claude: "There are multiple team members working on this. Create a new progress file for only the [specific folder] I'm working on. Don't update the main progress file."

#### Scenario 2: Parallel Work
Different developers can work on different folders simultaneously:
```
"I'm only responsible for the /components folder. Create a separate progress file for this folder only and keep your scope limited to these files."
```

### Project Setup for Teams
If more than one person is working on the same task:
- Set up a formal project structure
- Use specific branch naming conventions
- Maintain separate progress files per developer/folder

## Common Use Cases

### 1. Internationalization (i18n)
**Phase 1:** Making app i18n-compatible
- Install i18n library (React i18next)
- Add wrapper to root component
- Set up translation infrastructure

**Phase 2:** Component conversion
- Identify hardcoded strings across components
- Replace with translation functions
- Create translation files

**Example prompts:**
```
"Check the files to see where there are hardcoded strings that need i18n conversion"
"The app is now i18n-ready but components are not compatible. I'm working on the /pages folder only."
```

### 2. Language Migration
Converting between programming languages (e.g., Go to Python):
```
"I need to convert this Go ETL pipeline to Python while maintaining the same functionality. Analyze the Go code structure and create a conversion plan that preserves all business logic."
```

### 3. Code Refactoring
Large-scale refactoring across multiple files:
```
"Refactor this codebase to use the new [framework/pattern]. Identify all files that need changes and create a migration strategy."
```

### 4. API Updates
Updating deprecated API calls across the codebase:
```
"Find all instances of the old API pattern and create a plan to update them to the new API structure."
```

## Best Practices

### 1. Be Surgical, Not General
❌ **Wrong:** "Make this codebase better"
✅ **Right:** "Update all hardcoded strings in the /components/auth folder to use i18n translation functions"

### 2. Think Like Managing a Junior Developer
- Give specific, contained tasks
- Review work after each batch
- Don't overwhelm with entire codebase at once
- Provide clear, actionable instructions

### 3. Always Plan First
Never ask Claude to start coding immediately:
1. **Understand** the current state
2. **Plan** the approach
3. **Validate** the strategy
4. **Execute** in controlled batches
5. **Review** after each phase

### 4. Use Memory Effectively
```
"Add this to memory: [specific decision or context]"
"Update the progress file with the current status"
"Create a task file for this implementation plan"
```

### 5. Model Selection
- **Use Sonnet 4** for most tasks (200K context limit)
- **Switch to Opus 4** only for very complex tasks where Sonnet struggles
- Opus 4 is more powerful but use sparingly

### 6. Maintain Context Control
```
"Wait for my confirmation before proceeding to the next step"
"Show me what you plan to change before making any modifications"
"Update the memory file and pause for my review"
```

## Troubleshooting

### Common Issues

#### 1. Context Window Exhaustion
**Solution:** Start a new chat session - Serena will automatically resume from progress files

#### 2. Hallucinations
**Solution:** Keep tasks smaller and more specific. Review changes frequently.

#### 3. Uncontrolled Execution
**Solution:** Always include "wait for confirmation" instructions

#### 4. Team Conflicts
**Solution:** Use separate progress files per developer and clearly define folder ownership

### Quality Control Checklist
- [ ] Started with clean repository branch
- [ ] Created specific, surgical prompts
- [ ] Validated strategy before implementation
- [ ] Set up proper batching for large tasks
- [ ] Configured memory management
- [ ] Defined clear stopping points
- [ ] Established review process

### File Structure After Setup
```
your-repo/
├── .serena/
│   ├── memories/
│   ├── progress/
│   └── project-analysis/
├── your-code-files...
└── .git/
```

**Note:** Consider committing `.serena/` folder once your team adopts this workflow - it serves as excellent project documentation.

## Security Considerations

- **Always use local Serena server** (not remote hosted)
- **Never commit sensitive data** in progress files
- **Review all changes** before pushing to remote repositories
- **Use enterprise-approved branches** for sensitive codebases

## Next Steps

1. **Install and configure** Serena locally
2. **Practice with a small project** first
3. **Establish team conventions** for progress file management
4. **Create templates** for common use cases in your organization
5. **Train team members** on the surgical prompting approach

Remember: Serena + Claude is most effective when you treat it as a highly capable junior developer who needs clear, specific instructions and regular oversight.