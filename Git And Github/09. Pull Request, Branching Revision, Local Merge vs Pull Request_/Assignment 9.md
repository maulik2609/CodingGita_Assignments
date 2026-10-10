
**Objective:** Revise branching commands and naming conventions.

**Tasks:**
1. Write the modern and older command for the following:

| Action                         | Modern Command | Older Command |
|--------------------------------|----------------|---------------|
| Switch to a branch             |                |               |
| Create + Switch to new branch  |                |               |
| Merge a feature branch         |                |               |
| Delete a merged branch         |                |               |

2. Write 4 **good** branch names and 4 **bad** branch names.
3. What is the recommended naming convention for feature branches?

**Submission:** Written answers
**Answers**
<img width="1600" height="1399" alt="WhatsApp Image 2026-08-25 at 5 45 43 PM" src="https://github.com/user-attachments/assets/344499f1-856e-45b1-a036-2e83d72a91be" />


**Objective:** Understand the difference between the two methods.

**Tasks:**
1. Create a comparison table between **Local Merge** and **GitHub Pull Request** (at least 5 points).
2. When should you use Local Merge?
3. When should you use a Pull Request?
4. Why is Pull Request preferred in team/professional projects?

**Submission:** Written answers
**Answers**

<img width="1600" height="1350" alt="WhatsApp Image 2026-08-25 at 5 46 26 PM" src="https://github.com/user-attachments/assets/a0afa4b5-7fbb-4bde-98d7-c50da7cf0e93" />

**Objective:** Practice the complete local merge workflow.

**Tasks:**
1. Make sure you are on `main`.
2. Create a branch named `feature/about-page`.
3. Create a file `about.txt` and add some content.
4. Stage and commit with a meaningful message.
5. Switch to `main` and merge the branch.
6. Delete the feature branch.
7. Verify with `git branch` and `git log --oneline`.

**Submission:**  
- Screenshot of `git branch` (final)  
- Screenshot of `git log --oneline`  
- Screenshot showing `about.txt` is present on main

  <img width="954" height="537" alt="Screenshot 2026-08-25 180906" src="https://github.com/user-attachments/assets/d7683038-3bbb-4b82-96df-08e7aa5c765d" />

  **Objective:** Perform the professional Pull Request workflow.

**Tasks:**
1. Create a new branch `feature/services-page`.
2. Add a file `services.txt` with any content.
3. Commit the changes.
4. Push the branch using:
   ```bash
   git push -u origin feature/services-page
   ```
5. Go to GitHub and create a Pull Request.
6. Merge the Pull Request.
7. Delete the branch on GitHub.
8. Update your local main:
   ```bash
   git switch main
   git pull origin main
   git branch -d feature/services-page
   ```

**Submission:**  
- Screenshot of the created Pull Request  
- Screenshot after merging the PR  
- Screenshot of final `git log --oneline` on main


**Answers**
<img width="1920" height="1190" alt="Screenshot 2026-08-19 201238" src="https://github.com/user-attachments/assets/6bc10e21-0917-4701-99a9-b5f8fa347ba7" />
<img width="1874" height="1070" alt="Screenshot 2026-08-19 201336" src="https://github.com/user-attachments/assets/020b6372-7c03-427a-8711-febd6eeff403" />


**Objective:** Test deep understanding of Day 9 concepts.

**Tasks:**
1. Write the complete **Local Merge** workflow (step-by-step commands).
2. Write the complete **Pull Request** workflow (step-by-step).
3. Answer the following:
   - Why should we always run `git pull` on main before creating a new feature branch?
   - What happens if you merge a PR on GitHub but forget to run `git pull` locally?
   - Why should feature branches be deleted after merging?
4. Write 4 key takeaways from Day 9.

**Submission:** Written answers
<img width="1600" height="1388" alt="WhatsApp Image 2026-08-25 at 5 52 41 PM" src="https://github.com/user-attachments/assets/e1af5358-ac04-4555-96b1-a6c08e0165d4" />








