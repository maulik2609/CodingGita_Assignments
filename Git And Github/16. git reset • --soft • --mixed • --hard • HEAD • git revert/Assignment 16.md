## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Submit:**
- Screenshot of `git log --oneline` **before** reset
- Screenshot of `git log --oneline` and `git status` **after** reset
- Repository link

**Answers**
https://github.com/maulik2609/git-reset-revert-practice

<img width="960" height="564" alt="Screenshot 2026-09-05 095655" src="https://github.com/user-attachments/assets/627b5d11-3b83-4c4c-beb0-84f3d6c89d19" />
<img width="960" height="564" alt="Screenshot 2026-09-05 095754" src="https://github.com/user-attachments/assets/8beeebcf-2f93-473c-9923-a311ce684f64" />
<img width="960" height="559" alt="Screenshot 2026-09-05 095815" src="https://github.com/user-attachments/assets/feb84fe7-6d42-41db-bd61-a429fccdb40b" />






