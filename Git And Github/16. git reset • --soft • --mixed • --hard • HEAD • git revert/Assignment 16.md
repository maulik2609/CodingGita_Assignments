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


## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```

3. write the short answers in your own words in your notebook:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?

**Submit:**
- Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)
- Photos of written answers.
- Repository link

  **Answers**
  <img width="1570" height="1600" alt="WhatsApp Image 2026-09-06 at 5 15 41 PM" src="https://github.com/user-attachments/assets/da1d078a-366f-4fe5-a579-8ff3b5d34b7e" />
<img width="960" height="558" alt="Screenshot 2026-09-06 172155" src="https://github.com/user-attachments/assets/3f161bbb-faac-4e21-b8e4-6c950eee6d25" />
  <img width="960" height="538" alt="Screenshot 2026-09-06 172617" src="https://github.com/user-attachments/assets/ca132a0b-d65e-401f-ae0a-4e715a6fc6d4" />
  <img width="960" height="564" alt="Screenshot 2026-09-06 172832" src="https://github.com/user-attachments/assets/a13c65b9-d29f-4f75-814d-507867de9418" />

https://github.com/maulik2609/Reset-Assignment.git









