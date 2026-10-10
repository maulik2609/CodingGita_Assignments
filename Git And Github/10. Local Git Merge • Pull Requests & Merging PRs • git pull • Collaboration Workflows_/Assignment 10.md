1. Create a new branch:  
   `git checkout -b feature-local-merge`
2. Create a file named `local-merge.txt` and write 3–4 lines about what you learned today about local merge.
3. Stage and commit:  
   `git add .`  
   `git commit -m "Add local-merge notes"`
4. Switch back to main:  
   `git checkout main`
5. Merge the feature branch:  
   `git merge feature-local-merge`
6. Push main:  
   `git push origin main`
7. Run `git log --oneline -5` and take a screenshot of the history.

**Submit:** Screenshot of `git log --oneline` after the merge + confirmation that the file is on GitHub `main`.

<img width="944" height="478" alt="Screenshot 2026-08-26 165706" src="https://github.com/user-attachments/assets/7931bb1f-d16a-4c69-9af9-b359e4311306" />
<img width="948" height="564" alt="Screenshot 2026-08-26 165731" src="https://github.com/user-attachments/assets/d64303bc-56a1-4757-b498-bb81598fe9f0" />

1. Create a new branch:  
   `git checkout -b feature-pr-practice`
2. Create a file named `pr-practice.txt`. Write what a Pull Request is and why teams use it (4–5 lines).
3. Commit:  
   `git add .`  
   `git commit -m "Add PR practice notes"`
4. Push the branch:  
   `git push -u origin feature-pr-practice`
5. On GitHub: Open a Pull Request from `feature-pr-practice` into `main`. Write a clear PR title and description.
6. Merge the Pull Request on GitHub (use **“Create a merge commit”** option).
7. Delete the feature branch on GitHub (optional but recommended).
8. Locally:  
   `git checkout main`  
   `git pull origin main`
9. Confirm `pr-practice.txt` is now present on local main. Take a screenshot of the terminal after pull and of the merged PR on GitHub.

**Submit:** Link to the merged PR + screenshot of successful `git pull` + screenshot of GitHub PR (merged state).

<img width="927" height="537" alt="Screenshot 2026-08-26 170620" src="https://github.com/user-attachments/assets/8e92122d-bcd8-4f59-93fb-bd10ba39f863" />
https://github.com/maulik2609/Pull-Practice/pull/1

1. You already did one local merge (Assignment 1) and one PR merge (Assignment 2).
2. Create a short file named `comparison.txt` (on a new branch or directly on main).
3. In that file answer these questions **in your own words**:
   - What is the main difference between local merge and PR merge?
   - When would you prefer a local merge?
   - When is a Pull Request better?
   - After merging a PR on GitHub, which command brings the changes to your computer?
   - What does `git pull` actually do (two steps)?
4. Commit and push `comparison.txt` (either via local merge or via a new PR).

**Submit:** Content of `comparison.txt` (or screenshot) + link to the commit/PR.

<img width="1446" height="1600" alt="WhatsApp Image 2026-08-26 at 4 58 27 PM" src="https://github.com/user-attachments/assets/ce9bb3a7-0dd7-48d7-97dc-abc399884081" />

1. Make sure you are on `main`:  
   `git checkout main`
2. Run `git pull origin main` and observe the output.
3. Create a small change on GitHub itself (edit any file using the GitHub web editor on `main` and commit).
4. Back in your terminal, run `git pull origin main` again.
5. Confirm the web change is now in your local files.
6. Take a screenshot of the terminal showing the pull that brought the web change.

**Submit:** Screenshot of the successful `git pull` that received the GitHub web edit.

<img width="927" height="537" alt="Screenshot 2026-08-26 170620" src="https://github.com/user-attachments/assets/01933543-1dc0-4654-b256-37a30b494039" />








