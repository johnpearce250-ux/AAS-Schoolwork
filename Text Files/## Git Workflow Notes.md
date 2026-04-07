## Git Workflow Notes

If you are in an AAS program, learn Git by understanding the workflow, not by memorizing commands. Most beginners get stuck because they memorize `git add` and `git commit` without understanding what is happening in the `.git` folder or why branching matters.

## Best Resources

### 1. Conceptual Understanding

**Oh My Git!**
An open-source, gamified tool that visualizes your Git repository as you work. It is useful for a first-year student because it removes the fear of the terminal and shows exactly what happens to your files when you commit or branch.

**Pro Git Book (Free Online)**
The "Bible" of Git. You do not need to read it cover to cover, but it is worth bookmarking. Chapters 1 through 3 are the most important for an entry-level developer.

### 2. Interactive Practice

**Learn Git Branching**
This is one of the best tools on the internet for learning Git. It provides a visual sandbox where you type commands, and the screen shows how the commit tree grows and splits. It is highly addictive and will solidify your mental model of how branches work.

**Git Exercises**
If you prefer a challenge, this site gives you a series of tasks to solve using the terminal. It forces you to fix broken repositories, which is the kind of work you will actually do as an AI Engineer.

### 3. The CLI

As an AI Engineer, you will likely work on Linux servers or in containers like Docker eventually. You need to get comfortable with the shell.

**The Missing Semester of Your CS Education**
A series from MIT that is specifically designed for students who know how to code but do not know how to use the tools surrounding the code, such as Shell, CLI, Git, and editors.

Start with Lecture 1, Course Overview/Shell, and Lecture 2, Shell Tools/Scripting. It is the next level you are looking for.

**Explainshell**
Whenever you see a command like `ls -lah | grep ".py"`, you can paste it into Explainshell, and it will break down exactly what every character does. It is a useful way to learn through osmosis.

## Workflow Strategy

Since you are studying Python, do not just learn Git in a vacuum. Start this habit now:

- Stop saving files as `my_script_v1.py`, `my_script_final.py`, and similar names.
- Create a GitHub account if you have not already.
- Every time you finish a homework assignment or small project, create a new repo.
- Practice the cycle below:

```bash
git init
git add .
git commit -m "add core logic for AI model"
git push
```

## Final Tips

Do not fear detached HEAD or merge conflicts. You will encounter them, and that is normal. When you hit an error, copy and paste it into Google, then look for answers on Stack Overflow.

If you ever get stuck, do not try to force the terminal to work. You can delete the hidden `.git` folder in your project and re-initialize it. That gives you a clean slate, and you will not lose your actual Python code.

If you want, I can also walk you through the most common day-to-day Git commands for Python projects.