# 🚀 Quick Start Guide

Get started with Open Source Connect in 5 minutes!

## ⚡ Fast Track (For Experienced Users)

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/OSC-2K26.git
cd OSC-2K26
git checkout -b fix/problem-001
# Edit problems/medium/problem_001.py
python3 problems/medium/problem_001.py
git add problems/medium/problem_001.py
git commit -m "Fix: Resolved syntax error in problem_001"
git push origin fix/problem-001
# Create PR on GitHub
```

## 📚 Detailed Steps (For Beginners)

### 1️⃣ Setup (One Time Only)

#### Create GitHub Account
1. Go to [github.com](https://github.com)
2. Sign up for free
3. Verify your email

#### Install Git
- **Windows**: Download from [git-scm.com](https://git-scm.com/)
- **Mac**: `brew install git` or download from git-scm.com
- **Linux**: `sudo apt-get install git` (Ubuntu/Debian)

#### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

#### Install Python
- Download from [python.org](https://www.python.org/) (version 3.7+)
- Check installation: `python3 --version`

### 2️⃣ Fork the Repository

1. Go to the main repository on GitHub
2. Click the **"Fork"** button (top right)
3. This creates your own copy

### 3️⃣ Clone Your Fork

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/OSC-2K26.git
cd OSC-2K26
```

### 4️⃣ Choose a Problem

```bash
# Look at available problems
ls problems/medium/
ls problems/advanced/

# View a problem
cat problems/medium/problem_001.py
```

### 5️⃣ Create a Branch

```bash
# Always work on a new branch!
git checkout -b fix/problem-001
```

Branch naming convention: `fix/problem-XXX` where XXX is the problem number

### 6️⃣ Fix the Problem

1. Open the problem file in your editor
2. Read the comments to understand what it should do
3. Find and fix the error(s)
4. Save the file

### 7️⃣ Test Your Solution

```bash
# Run the file
python3 problems/medium/problem_001.py

# Make sure the output matches the expected output!
```

### 8️⃣ Commit Your Changes

```bash
# Stage your changes
git add problems/medium/problem_001.py

# Commit with a clear message
git commit -m "Fix: Resolved missing colon in problem_001"
```

### 9️⃣ Push to GitHub

```bash
# Push your branch
git push origin fix/problem-001
```

If this is your first push, Git might ask you to set up authentication.

### 🔟 Create Pull Request

1. Go to your fork on GitHub
2. You'll see a banner: **"Compare & pull request"** - click it
3. Write a description of what you fixed
4. Click **"Create pull request"**
5. Wait for review! 🎉

## 🎯 Your First Problem

We recommend starting with **Easy** problems for first-time contributors:

### Easy Problems (Start Here!) 🟢
- **problems/easy/problem_001.py** - Missing colon (syntax error)
- **problems/easy/problem_002.py** - Missing print parentheses
- **problems/easy/problem_005.py** - Variable typo

### Medium Problems (After Easy) 🟡
- **problems/medium/problem_051.py** - List comprehension issue
- **problems/medium/problem_052.py** - String immutability

### Advanced Problems (For Experts) 🔴
- **problems/advanced/problem_201.py** - Metaclass challenge
- Only attempt these after mastering easy and medium!

## 💡 Tips for Success

### ✅ DO:
- Read the problem description carefully
- Test your solution before committing
- Use clear commit messages
- Fix one problem per PR
- Ask for help if stuck

### ❌ DON'T:
- Skip testing your solution
- Fix multiple problems in one PR
- Modify other people's fixes
- Remove the problem description comments

## 🆘 Troubleshooting

### "Permission denied" when pushing
- Make sure you cloned YOUR fork, not the main repository
- Check: `git remote -v` should show YOUR_USERNAME

### "Merge conflict"
```bash
# Update your branch
git pull origin main
# Fix conflicts in your editor
git add .
git commit -m "Resolved merge conflict"
```

### Code still has errors after fixing
- Double-check the expected output in comments
- Make sure you saved the file
- Try running: `python3 -m py_compile filename.py` to check syntax

### Can't find what's wrong
- Check the README/DEBUGGING_GUIDE.md
- Look at the error message carefully
- Ask in the discussions section

## 📖 More Resources

- [Full Git Guide](README/GIT_GUIDE.md) - Complete Git tutorial
- [Debugging Guide](README/DEBUGGING_GUIDE.md) - How to find and fix errors
- [Problems README](problems/README.md) - Detailed problem-solving guide

## 🎉 After Your First PR

1. Pat yourself on the back! 🎊
2. Add your name to CONTRIBUTORS.md
3. Try a harder problem
4. Help other students in discussions

## ❓ Questions?

- **Git questions**: See [README/GIT_GUIDE.md](README/GIT_GUIDE.md)
- **Python questions**: See [README/DEBUGGING_GUIDE.md](README/DEBUGGING_GUIDE.md)
- **Other questions**: Open an issue on GitHub

---

**Ready? Let's code! 🚀**

Time to make your first contribution to open source!
