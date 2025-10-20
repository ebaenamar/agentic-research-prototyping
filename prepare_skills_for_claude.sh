#!/bin/bash

# Script to prepare skills for Claude Desktop/Code
# This creates properly structured ZIP files for each skill

echo "================================================"
echo "Preparing Skills for Claude Desktop/Code"
echo "================================================"

# Create output directory
mkdir -p claude-skills-zips
cd skills

# List of skills to package
SKILLS=(
    "literature-review-skill"
    "research-methodology-validator"
    "validation-without-humans-skill"
    "experiment-design-skill"
    "results-analysis-skill"
    "research-review-skill"
)

echo ""
echo "Processing ${#SKILLS[@]} skills..."
echo ""

# Process each skill
for skill in "${SKILLS[@]}"; do
    echo "Processing: $skill"
    
    if [ ! -d "$skill" ]; then
        echo "  ⚠️  Directory not found: $skill"
        continue
    fi
    
    cd "$skill"
    
    # Rename SKILL.md to Skill.md if needed
    if [ -f "SKILL.md" ]; then
        echo "  → Renaming SKILL.md to Skill.md"
        mv SKILL.md Skill.md
    fi
    
    # Check if Skill.md exists
    if [ ! -f "Skill.md" ]; then
        echo "  ❌ Skill.md not found in $skill"
        cd ..
        continue
    fi
    
    # Create ZIP
    echo "  → Creating ZIP file"
    zip -r "../../claude-skills-zips/${skill}.zip" . -x "*.DS_Store" -x "__pycache__/*" -x "*.pyc" > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo "  ✅ Created: ${skill}.zip"
    else
        echo "  ❌ Failed to create ZIP for $skill"
    fi
    
    cd ..
    echo ""
done

cd ..

echo "================================================"
echo "Summary"
echo "================================================"
echo ""
echo "ZIP files created in: claude-skills-zips/"
echo ""
ls -lh claude-skills-zips/*.zip 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
echo ""
echo "================================================"
echo "Next Steps:"
echo "================================================"
echo ""
echo "1. Open Claude Desktop or Claude Code"
echo "2. Go to Settings > Capabilities"
echo "3. Enable 'Code execution and file creation'"
echo "4. Scroll to Skills section"
echo "5. Click 'Upload skill' for each ZIP file"
echo "6. Toggle each skill ON"
echo ""
echo "See CLAUDE_SKILLS_SETUP.md for detailed instructions"
echo ""
echo "Done! 🚀"
