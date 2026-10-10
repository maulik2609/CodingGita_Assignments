## Assignment 1 – Practice `git restore` and `git restore --staged`

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
```bash
git restore profile.txt
```
Observe that it does **not** work (because the file is untracked).
4. Stage the file:
```bash
git add profile.txt
```
5. Unstage it using:
```bash
git restore --staged profile.txt
```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
```bash
git add profile.txt
git commit -m "Add profile.txt"
```

**Submit:**
- Screenshot of `git status` when the file was untracked
- Screenshot after using `git restore --staged`
- Repository link

---
**Answers**
https://github.com/maulik2609/restore
<img width="954" height="508" alt="Screenshot 2026-09-03 170336" src="https://github.com/user-attachments/assets/479aabe4-4bbd-4338-9fb3-b8edef72b655" />
<img width="950" height="564" alt="Screenshot 2026-09-03 170453" src="https://github.com/user-attachments/assets/9934c209-aab5-402b-be88-4360eec87cb8" />


**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

  **Answers**
  https://github.com/maulik2609/rm-practice.git
  <img width="1280" height="823" alt="WhatsApp Image 2026-09-03 at 5 23 08 PM" src="https://github.com/user-attachments/assets/9c22f5d5-4cfa-4959-85f9-23a6afe7a76f" />
  <img width="960" height="566" alt="Screenshot 2026-09-03 171549" src="https://github.com/user-attachments/assets/d4c71dfb-db4f-41db-b461-9d1b7d0ee293" />
  <img width="914" height="554" alt="Screenshot 2026-09-03 171625" src="https://github.com/user-attachments/assets/84f0c2c2-ac24-4392-ac18-9b059397fde6" />
<img width="914" height="554" alt="Screenshot 2026-09-03 171625" src="https://github.com/user-attachments/assets/e912f756-ff14-47a7-a2cf-006be709af86" />


## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` after using `git rm --cached`
- Screenshot showing that `config.env` is ignored / removed from GitHub
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)

**Answers**

https://github.com/maulik2609/git-ignore

<img width="960" height="547" alt="Screenshot 2026-09-03 173635" src="https://github.com/user-attachments/assets/8622dfda-8ab2-49ac-9eba-af08bb2608ca" />

<img width="900" height="560" alt="Screenshot 2026-09-03 173724" src="https://github.com/user-attachments/assets/eb8aeb20-1b85-49e9-afae-fe69d9bf4110" />





  





