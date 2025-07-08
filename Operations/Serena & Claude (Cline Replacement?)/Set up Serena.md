Always clone locally - not download zip (so I keep project history from GitHub)

**Install git**
brew install git

**Clone first**: `git clone https://github.com/oraios/serena`
cd serena (move to the directory)

**Install uv:**
curl -LsSf https://astral.sh/uv/install.sh | sh

**Install dependencies**
uv sync

# Per project - run indexing:

That command is for **indexing a project** with Serena, not for running the MCP server. Let me clarify:

## Two different operations:

### 1. **Indexing a project** (what that command does):

The error shows you're trying to run `index-project` from the **wrong directory**. You're running it from the **serena** directory but pointing it at a **book-library-mcp** directory.
### Run from your project directory

bash

```bash
cd "/Users/katiepotter/0Code/eMumbaApr23-May2/MCP-Claude-Tests-FuzzyBookAddedSince/book-library-mcp"
uv run --directory "/Users/katiepotter/0Code/serena" index-project
```

### Option 2: Run from serena directory

This **prepares/indexes** your codebase so Serena can work with it efficiently. You run this **once per project** you want Serena to understand.

### 2. **Running the MCP server** (for Claude Desktop):

Your JSON config is correct:

```json
"serena": {
  "command": "uv",
  "args": ["run", "python", "-m", "serena"],
  "cwd": "/Users/katiepotter/0Code/serena"
}
```

## Workflow:

1. **First**: Index your actual code project (like the web-controller repo):
    
    ```shell
    cd /path/to/your/web-controller-project
    uv run --directory /Users/katiepotter/0Code/serena index-project
    ```
    
2. **Then**: Your Claude Desktop config will start the Serena MCP server automatically
    
3. **Finally**: When you chat with Claude and mention working with code, Serena will use the indexed project data
    

So you need to run that `index-project` command **on each codebase** you want to work with (like the web-controller repo Murali was using), not on the Serena installation itself.

## Setup (one-time per repo):

**You'll need to index each repo separately**, but then you can switch between them seamlessly in Claude Desktop.
### Index each repository:

```bash
# Index web-controller
cd /path/to/web-controller
uv run --directory /path/to/serena index-project

# Index your docs repo  
cd /path/to/product-docs
uv run --directory /path/to/serena index-project

# Index translation UI repo
cd /path/to/translation-ui
uv run --directory /path/to/serena index-project
```

e.g. 
# cd , then:
uv run --directory /Users/katiepotter/0Code/serena index-project
## Daily workflow:

### **Option 1: Tell Claude which project** (easiest)

Just mention the project in your chat:

- "Let's work on the web-controller project..."
- "Switch to the product-docs repository..."
- "I need to check the translation-ui codebase..."

### **Option 2: Change directory in terminal**

```bash
cd /path/to/different-repo
# Then start your Claude Desktop session
```

### **Option 3: Use project-specific chats**

- Create separate Claude projects/chats for different repos
- Each chat "remembers" which codebase you're working on

## Serena is smart about context:

- It can work with **multiple indexed projects**
- It figures out which one you mean based on your conversation
- You can even compare code **across different repos** in the same chat

So index everything once, then just **tell Claude which project** you want to work on in each conversation!