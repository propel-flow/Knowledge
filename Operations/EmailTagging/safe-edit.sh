#!/bin/bash
# safe-edit.sh - Run before making changes with Cline

echo "🔒 Creating safety checkpoint..."
git add .
git commit -m "Checkpoint: $(date +%Y-%m-%d_%H:%M:%S)" || echo "No changes to commit"
echo "✅ Checkpoint created! Safe to proceed with changes."
echo "💡 To undo all changes, run: git checkout ."
