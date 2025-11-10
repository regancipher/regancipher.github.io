# Local Testing Guide

## Quick Setup (One-time)

### If you have Ruby installed:
```bash
# Install Jekyll and Bundler
gem install bundler jekyll

# Navigate to your blog directory
cd /path/to/regancipher-blog

# Install dependencies
bundle install

# Start the local server
bundle exec jekyll serve

# Open in browser: http://localhost:4000
```

### If you DON'T have Ruby:
**Windows:** Download RubyInstaller from https://rubyinstaller.org/
**Mac:** Ruby is pre-installed, just run the commands above
**Linux:** `sudo apt-get install ruby-full` (Ubuntu/Debian)

## Live Reloading

Once running, Jekyll watches for changes:
- Edit a file → Save → Auto-refreshes in browser
- Perfect for iterating on design/content

## Testing Workflow

```bash
# Terminal 1: Keep Jekyll running
bundle exec jekyll serve

# Terminal 2: Edit files
vim _posts/2025-10-31-new-review.md
# Save file → Check browser → Repeat
```

## Troubleshooting

**Port already in use?**
```bash
bundle exec jekyll serve --port 4001
```

**Changes not showing?**
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache

**Build errors?**
Check the terminal output for YAML syntax errors or missing files.
