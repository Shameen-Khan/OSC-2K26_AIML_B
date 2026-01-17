# Getting Started with Git and GitHub

A beginner-friendly guide for PyExpo 2026 - Open Source Connect

## 📖 What is Git?

Git is a version control system that helps you track changes in your code. Think of it as a "time machine" for your projects – you can see what changed, when it changed, and who changed it.

## 📖 What is GitHub?

GitHub is a website where you can store your Git repositories online. It's like Google Drive, but specifically designed for code. It also makes it easy to collaborate with others.

## 🛠️ Installation

### Windows
1. Download Git from [git-scm.com](https://git-scm.com/)
2. Run the installer
3. Use default settings (just keep clicking "Next")

### macOS
```bash
# Using Homebrew
brew install git

# Or download from git-scm.com
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git
```

## ⚙️ Initial Setup

After installing Git, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 🚀 Basic Git Workflow

### 1. Clone a Repository
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### 2. Create a Branch
```bash
git checkout -b fix/problem-name
```

### 3. Make Changes
Edit files using your favorite text editor.

### 4. Check Status
```bash
git status
```
This shows which files you've changed.

### 5. Stage Changes
```bash
# Stage a specific file
git add filename.py

# Stage all changes
git add .
```

### 6. Commit Changes
```bash
git commit -m "Fix: Brief description of what you fixed"
```

### 7. Push Changes
```bash
git push origin branch-name
```

## 🔄 Contributing to This Project

### Complete Workflow Example:

```bash
# 1. Fork the repo on GitHub (click Fork button)

# 2. Clone YOUR fork
git clone https://github.com/YOUR_USERNAME/OSC-2K26.git
cd OSC-2K26

# 3. Create a new branch
git checkout -b fix/problem-001

# 4. Fix the problem in problems/medium/problem_001.py

# 5. Test your fix
python3 problems/medium/problem_001.py

# 6. Stage and commit
git add problems/medium/problem_001.py
git commit -m "Fix: Resolved syntax error in problem_001"

# 7. Push to your fork
git push origin fix/problem-001

# 8. Go to GitHub and create a Pull Request
```

## 📝 Commit Message Guidelines

Good commit messages help others understand what you did:

### Format:
```
Type: Brief description

Optional longer description if needed
```

### Types:
- `Fix:` - Fixed a bug or error
- `Add:` - Added new functionality
- `Update:` - Updated existing code
- `Docs:` - Documentation changes

### Examples:
- ✅ `Fix: Resolved missing colon in problem_001.py`
- ✅ `Fix: Corrected off-by-one error in loop`
- ❌ `fixed stuff`
- ❌ `updated file`

## 🌿 Branching Best Practices

### Branch Naming:
```
fix/problem-001
fix/syntax-error-problem-005
update/readme-typo
```

### Rules:
- One branch per problem/fix
- Use descriptive names
- Use lowercase and hyphens

## 🆘 Common Issues and Solutions

### Problem: "Permission denied (publickey)"
**Solution**: Set up SSH keys or use HTTPS instead
```bash
git remote set-url origin https://github.com/username/repo.git
```

### Problem: "Merge conflict"
**Solution**: This happens when two people edit the same line
```bash
# Pull latest changes
git pull origin main

# Resolve conflicts in your editor
# Look for <<<<<<< and >>>>>>>

# After fixing
git add .
git commit -m "Resolved merge conflict"
```

### Problem: "Your branch is behind"
**Solution**: Update your branch
```bash
git pull origin main
```

### Problem: Made a mistake in commit message
**Solution**: Fix the last commit message
```bash
git commit --amend -m "New message"
```

## 📚 Useful Git Commands

```bash
# See commit history
git log

# See changes you made
git diff

# Undo changes (before staging)
git checkout -- filename.py

# Unstage a file
git reset filename.py

# Switch to another branch
git checkout branch-name

# See all branches
git branch -a

# Delete a branch (after merging)
git branch -d branch-name
```

## 🎓 Learning Resources

### Official Resources:
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

### Interactive Tutorials:
- [Learn Git Branching](https://learngitbranching.js.org/)
- [GitHub Skills](https://skills.github.com/)

### Video Tutorials:
- Search "Git and GitHub for Beginners" on YouTube
- freeCodeCamp has excellent Git tutorials

## 💡 Pro Tips

1. **Commit Often**: Make small, frequent commits rather than one huge commit
2. **Write Clear Messages**: Your future self will thank you
3. **Pull Before Push**: Always pull latest changes before pushing
4. **One Feature Per Branch**: Keep changes focused and organized
5. **Test Before Commit**: Make sure your code works!

## ❓ Getting Help

- **Git Help**: `git help <command>` (e.g., `git help commit`)
- **This Project**: Open an issue on GitHub
- **General Git**: StackOverflow, Git documentation

---

**Remember**: Everyone makes mistakes with Git at first. It's part of learning!

Don't be afraid to experiment – that's how you learn best! 🚀
