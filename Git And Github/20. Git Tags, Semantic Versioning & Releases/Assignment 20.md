## Question 1:

Explain the following in your own words:

1. What is the difference between a **Branch** and a **Tag** in Git?
2. What is the difference between a **Lightweight Tag** and an **Annotated Tag**?
3. Why should we prefer Annotated tags in professional/collaborative projects?
4. What is Semantic Versioning? Explain with examples of `v1.0.0`, `v1.1.0`, and `v1.1.1`.

**Answers**
<img width="1600" height="1149" alt="WhatsApp Image 2026-09-14 at 2 17 51 PM" src="https://github.com/user-attachments/assets/4549c983-d2d8-45f4-a698-cede7e33ee17" />
<img width="1600" height="1230" alt="WhatsApp Image 2026-09-14 at 2 18 24 PM" src="https://github.com/user-attachments/assets/501a46ef-35d4-4d24-983b-750ed83d7a5a" />

## Question 2:

Perform the following tasks in your repository and submit screenshots:

1. Create at least 4 commits on the `main` branch.
2. Create two **Lightweight tags** on any two commits (as personal bookmarks).
3. Create three **Annotated tags** with proper Semantic Versioning:
   - `v1.0.0`
   - `v1.1.0`
   - `v1.1.1`
4. Push all annotated tags to GitHub.
5. Create **GitHub Releases** for `v1.0.0` and `v1.1.0`.

**Answers**

<img width="960" height="564" alt="Screenshot 2026-09-14 155559" src="https://github.com/user-attachments/assets/9ca8e39c-6593-4f34-8160-4f57d771ff0f" />
<img width="960" height="556" alt="Screenshot 2026-09-14 155629" src="https://github.com/user-attachments/assets/67b781ec-1180-499a-87ff-d4f545065a13" />
<img width="960" height="564" alt="Screenshot 2026-09-14 155706" src="https://github.com/user-attachments/assets/8c177ae4-246d-4c3a-b228-e3789c155a8e" />


### Part A: Lightweight Tags

1. Create a new repository.
2. Make at least **3 commits** on the `main` branch.
3. Create **Lightweight tags** on these commits as personal bookmarks.  
   Example names:
   - `v0.1.0-light`
   - `v0.1.1-bugFix`
   - `temp-trial`

4. Run the following command and take a screenshot:
   ```bash
   git tag
   ```
   **Answers**
   <img width="947" height="558" alt="Screenshot 2026-09-14 160941" src="https://github.com/user-attachments/assets/2f9e6b7c-fcf6-4524-8ca0-1964fc279b04" />
   ### Part B: Annotated Tags

Now imagine 2-3 developers have joined your project. From now on, use only **Annotated tags**.

### Steps:

1. Create three branches:
   ```bash
   git branch feature/major-update
   git branch feature/minor-update
   git branch bugfix/login-issue
   ```

2. **Major Update (v1.0.0)**
   - Switch to `feature/major-update`
   - Make **3 commits** (example: Authentication, Home Page, Payment Gateway)
   - Merge the branch into `main` using `pull request`
   - Create an **Annotated tag** on the merge commit:
     ```bash
     git tag -a v1.0.0 -m "First stable release - Auth, Home Page & Payment Gateway"
     ```

3. **Minor Update (v1.1.0)**
   - Switch to `feature/minor-update`
   - Make **2 commits** (example: Dark Mode feature)
   - Merge into `main` using `pull request`
   - Create Annotated tag:
     ```bash
     git tag -a v1.1.0 -m "Minor release - Added Dark Mode"
     ```

4. **Bug Fix (v1.1.1)**
   - Switch to `bugfix/login-issue`
   - Make **1 commit** (example: Fixed login redirect)
   - Merge into `main` using `pull request`
   - Create Annotated tag:
     ```bash
     git tag -a v1.1.1 -m "Patch release - Fixed login redirect issue"
     ```

---

### Part C: Push to GitHub

1. Push the `main` branch:
   ```bash
   git push origin main
   ```

2. Push all the annotated tags:
   ```bash
   git push origin v1.0.0
   git push origin v1.1.0
   git push origin v1.1.1
   ```

   **OR**

   ```bash
   git push origin --tags
   ```

---

### Part D: Create GitHub Releases

1. Go to your repository on GitHub.
2. Click on **Releases** → **Draft a new release**.
3. Create releases for the following tags:

   | Tag     | Release Title                        |
   |---------|--------------------------------------|
   | v1.0.0  | v1.0.0 – First Stable Release        |
   | v1.1.0  | v1.1.0 – Dark Mode Added             |
   | v1.1.1  | v1.1.1 – Login Bug Fix               |

4. Add a short description for each release.

---

## Submission Requirements

Submit the following:

1. Screenshot of `git tag` command (showing all tags)
2. Screenshot of `git show v1.0.0`
3. Screenshot of `git log --oneline --decorate --graph --all`
4. Link to your GitHub repository
5. Screenshots of the three GitHub Releases you created

 **Answers**

 <img width="948" height="560" alt="Screenshot 2026-09-14 162105" src="https://github.com/user-attachments/assets/1550485e-fd0b-4eab-a5be-bc5db822e8f5" />
 <img width="948" height="431" alt="Screenshot 2026-09-14 171028" src="https://github.com/user-attachments/assets/d1dee32f-89ad-4966-9dd6-4522653863f9" />
 <img width="948" height="499" alt="Screenshot 2026-09-14 171637" src="https://github.com/user-attachments/assets/7ba01389-abb4-4932-9daf-9f6178c05cb7" />
 <img width="343" height="411" alt="Screenshot 2026-09-14 172118" src="https://github.com/user-attachments/assets/0589b574-2072-42ea-8088-c1ea357c7cda" />
<img width="687" height="382" alt="Screenshot 2026-09-14 172706" src="https://github.com/user-attachments/assets/6734f259-036f-4119-bd67-9e8dde23b82b" />

 https://github.com/maulik2609/TAG-2.git
 













