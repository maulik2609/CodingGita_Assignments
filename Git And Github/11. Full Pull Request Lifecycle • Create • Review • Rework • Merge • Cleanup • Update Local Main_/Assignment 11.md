**Goal:** Practice the full cycle: branch → file → commit → push → PR → merge → cleanup.

1. Update main:  
   `git checkout main && git pull origin main`
2. Create branch:  
   `git checkout -b feature/contact-form`
3. Create file `contact.html` with a simple heading and a short paragraph about a contact form.
4. Stage, commit and push:  
   ```bash
   git add contact.html
   git commit -m "Add contact form page"
   git push -u origin feature/contact-form
   ```
5. On GitHub: Open a Pull Request (base = `main`, compare = `feature/contact-form`). Write a clear title and description.
6. Merge the Pull Request using **“Create a merge commit”**.
7. Delete the remote branch (GitHub “Delete branch” button or `git push origin --delete feature/contact-form`).
8. Update local main using the two-command method:  
   ```bash
   git checkout main
   git fetch origin main
   git merge origin/main
   ```
9. Delete local branch:  
   `git branch -d feature/contact-form`
10. Take screenshots of:  
    (a) the merged PR  
    (b) terminal after fetch + merge  
    (c) `git branch` showing the branch is gone

**Submit:** Merged PR link + the 3 screenshots listed above.

**Answers**

https://github.com/maulik2609/Assignment-Part/pull/1

<img width="935" height="558" alt="Screenshot 2026-08-27 165813" src="https://github.com/user-attachments/assets/82dd8ac9-a86b-44db-9458-8409309255d1" />

<img width="815" height="491" alt="Screenshot 2026-08-27 165904" src="https://github.com/user-attachments/assets/ae2a9a49-2f17-48c0-a138-5c731067da0f" />



**Goal:** Practice receiving a review comment, reworking the **same** branch, and updating the PR.

1. Create branch:  
   `git checkout -b feature/about-page`
2. Create `about.html` with only a basic heading (intentionally incomplete).
3. Commit and push:  
   ```bash
   git add .
   git commit -m "Add about page skeleton"
   git push -u origin feature/about-page
   ```
4. Open a Pull Request on GitHub.
5. **Simulate review:** Add a comment on the PR yourself (or ask a classmate/mentor) requesting:  
   *“Please add a short paragraph about the purpose of the about page and a simple team section placeholder.”*
6. Rework on the **same branch**:  
   ```bash
   git checkout feature/about-page
   # edit about.html as requested
   git add .
   git commit -m "Address review: add description and team section"
   git push origin feature/about-page
   ```
7. Confirm the PR on GitHub now shows the new commit.
8. Merge the PR, delete remote branch, update local main (`git fetch` + `git merge` or `git pull`), delete local branch.
9. Screenshot:  
   (a) PR conversation showing the review comment + your new commit  
   (b) merged PR

**Submit:** PR link showing review comment + rework commit, plus merged PR screenshot.

**Answers**


https://github.com/maulik2609/Assignment-Part/pull/2

**Goal:** Independently complete one more full PR lifecycle.

1. Create `feature/navbar` branch from updated main.
2. Create `navbar.html` with a heading and 3–4 lines describing what a navigation bar contains (Home, About, Contact, etc.).
3. Commit, push, open PR with a clear title and description.
4. Merge the PR on GitHub.
5. Delete remote branch.
6. Update local main using:  
   ```bash
   git fetch origin main
   git merge origin/main
   ```
7. Delete local branch with `git branch -d feature/navbar`.
8. Run `git log --oneline -10` and take a screenshot showing the merge commits from the features you completed.

**Submit:** Merged PR link + screenshot of `git log --oneline`.

**Answers**

https://github.com/maulik2609/PR-/pull/1

<img width="953" height="500" alt="Screenshot 2026-08-27 172552" src="https://github.com/user-attachments/assets/aeafa64b-6568-43a8-969b-3b3288e4a2ee" />

rite answer **in your own words** in your notebook:

- Why do we push new commits to the **same** feature branch after a review instead of creating a new PR?
- What is the difference between deleting a remote branch and deleting a local branch?
- Why must we run `git fetch` + `git merge` (or `git pull`) after merging a PR on GitHub?
- Write the full sequence of commands you used to update local main and delete the local feature branch.

**Submit:** Photos of the hand written answers of the above questions.


**Answers**

<img width="1599" height="592" alt="WhatsApp Image 2026-08-26 at 5 28 15 PM" src="https://github.com/user-attachments/assets/08b267bc-2b66-4721-9abc-adc6e928e458" />
<img width="1600" height="925" alt="WhatsApp Image 2026-08-26 at 5 28 26 PM" src="https://github.com/user-attachments/assets/5714a81a-b3f7-4ff6-83b9-1b194c75f92d" />



