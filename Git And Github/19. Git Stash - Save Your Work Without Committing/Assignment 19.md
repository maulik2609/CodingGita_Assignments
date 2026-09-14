### Task A1 — Basic Stash (10 mins)

1. On `main`:
   - Edit `README.md`.
   - Create `notes.txt` (don’t add it to Git).

2. Run:
   ```bash
   git stash
   git stash -u
   git stash list
   ```
   - Take 1 screenshot of `git stash list`.
  
     **Answers**

<img width="960" height="559" alt="Screenshot 2026-09-14 131027" src="https://github.com/user-attachments/assets/5b7fec92-5bff-4764-9d98-9f6a500740bc" />

4. Run:
   ```bash
   git stash pop
   git stash list
   ```
   - Take 1 screenshot.
<img width="960" height="558" alt="Screenshot 2026-09-14 131334" src="https://github.com/user-attachments/assets/b9899a0d-06e6-438a-9940-ee5b134dd826" />

### Task A2 — Switch Branch with Half-Done Work (10 mins)

1. Create branch:
   ```bash
   git switch -c feature/login
   ```
2. In this branch:
   - Create `login.html` → commit it.
   - Create `login.css` → stage it (`git add login.css`).
   - Create `login.js` → leave it untracked.

3. You must switch to `main` urgently.  
   Stash your work (include untracked files) with a message:
   ```bash
   git stash -u -m "WIP: login page"
   ```

4. Switch to `main`, make a small change, commit, push:
   ```bash
   git switch main
   # edit README.md
   git add README.md
   git commit -m "Small update"
   git push
   ```

5. Go back and restore your work:
   ```bash
   git switch feature/login
   git stash pop
   ```

**Answers**
<img width="952" height="564" alt="Screenshot 2026-09-14 132055" src="https://github.com/user-attachments/assets/9915a7dd-c798-47df-8496-7876eb110199" />


### Task A3 — Simple Hygiene (5 mins)

1. Make a small change in `README.md`.
2. Stash it with a clear message:
   ```bash
   git stash push -m "BUGFIX: README typo"
   git stash list
   ```
3. Take 1 screenshot.

**Answers**
<img width="960" height="558" alt="Screenshot 2026-09-14 132343" src="https://github.com/user-attachments/assets/c267ba9a-80c6-4216-933b-a5114358ff2d" />

## Assignment B —  Theoretical  
**Title:** “Stash Concepts”

**Submit:** Write short answers in your notebook.

Answer in 2–4 lines each.

1. What is `git stash` in simple words? When do we use it?  
2. You have:
   - `app.js` (tracked, modified)
   - `test.js` (untracked)
   - `.env` (ignored)

   Which files are stashed by:
   - `git stash`
   - `git stash -u`
   - `git stash -a`

3. Explain the difference between:
   - `git stash apply`
   - `git stash pop`

4. When would you prefer `apply` over `pop`? Give one small example.

5. What do these commands do?
   - `git stash drop`
   - `git stash clear`

6. You see this `git stash list`:
   ```text
   stash@{0}: WIP on feature/login: ...
   stash@{1}: WIP on main: ...
   ```
   - Which is the latest stash?
   - If you run `git stash pop`, which one is removed?

7. Why is it good to use messages like:
   ```bash
   git stash push -m "WIP: login form"
   ```
   instead of just `git stash`? (2–3 lines)

8. Scenario:
   - You are on `feature/checkout`.
   - `checkout.html` is committed.
   - `checkout.css` is staged.
   - `checkout.js` is untracked.

   You must switch to `main` urgently.  
   Write the exact command(s) you will use to stash your work safely (include untracked files and a message).

   
**Answers**
<img width="1600" height="1014" alt="WhatsApp Image 2026-09-14 at 1 01 07 PM" src="https://github.com/user-attachments/assets/91b76e79-6197-4b3d-9f05-204013b4ad6d" />
<img width="1395" height="1600" alt="WhatsApp Image 2026-09-14 at 1 02 18 PM" src="https://github.com/user-attachments/assets/3003c4d9-8ebc-4411-ad99-bcce5ac2f3a0" />
<img width="987" height="1280" alt="WhatsApp Image 2026-09-14 at 1 02 43 PM" src="https://github.com/user-attachments/assets/8c981de1-f221-471e-ab27-531350c2c22b" />


### Part C1 — Practical (10 mins)

1. On `main`:
   - Edit `README.md`.
   - Create `temp.txt` (untracked).

2. Run:
   ```bash
   git stash
   git stash -u
   git stash list
   ```
   - Take 1 screenshot.

3. Answer:
   - Q1: How many stashes? Which one is latest?
   - Q2: Which stash has `temp.txt`?

4. Run:
   ```bash
   git stash pop
   git stash list
   ```
   - Take 1 screenshot.

**Answers**
<img width="960" height="559" alt="Screenshot 2026-09-14 133719" src="https://github.com/user-attachments/assets/217dcae9-7cfc-4c48-9f1a-20e33d3e5c83" />

### Part C2 — Theory (10 mins)

Answer in 2–4 lines each in your notebook.

6. In your own words, what is `git stash` and why is it useful?  

7. Explain with a small example:
   - `git stash apply`
   - `git stash pop`

8. Why should we use `-u` when stashing new files?  

9. Why are meaningful stash messages (like `"WIP: login form"`) important in team projects?  

10. Imagine:
    - You stashed 3 times.
    - You run `git stash pop`.
    - Then you run `git stash drop`.

    How many stashes remain if you started with 3? Explain briefly.

    
**Answers**
<img width="987" height="1280" alt="WhatsApp Image 2026-09-14 at 1 02 43 PM" src="https://github.com/user-attachments/assets/ef8ed034-46f0-4b1f-90b5-81835f0e3fb0" />
<img width="1280" height="580" alt="WhatsApp Image 2026-09-14 at 1 03 07 PM" src="https://github.com/user-attachments/assets/9b2da801-ec36-4178-a6e7-5fd061c23f00" />





