1. Create/clone a repository and on `main` create `tasks.txt`:

```text
My Tasks
1. Study Git
2. Complete assignment
3. Review notes
```

2. Commit and push to `main`.
3. Create branch `feature/tasks-A` → change line 3 to `Practice merge conflicts` → commit → push → open PR (do **not** merge yet).
4. Switch back to `main`, create branch `feature/tasks-B` → change line 3 to `Watch Git tutorial` → commit → push → open second PR.
5. Merge the first PR successfully.
6. Merge the second PR → conflict appears.
7. Resolve the conflict on GitHub:
   - Understand Current vs Incoming
   - Decide final text (keep one, both, or write your own)
   - Remove all conflict markers
   - Mark as resolved → Commit merge → Merge the PR
8. Delete both remote feature branches.
9. Update local main and delete local branches:
   ```bash
   git checkout main
   git pull origin main
   git branch -D feature/tasks-A
   git branch -D feature/tasks-B
   ```

**Submit:**
- Repository link
- Screenshot of the conflict editor (showing markers)
- Screenshot of the successfully merged second PR
- Screenshot of `git log --oneline` after pull

**Answers**
https://github.com/maulik2609/Conflict.git
<img width="938" height="539" alt="Assign 12 2" src="https://github.com/user-attachments/assets/be985831-68d4-4358-8a60-ed91f8a9e184" />
<img width="832" height="559" alt="Assign 12" src="https://github.com/user-attachments/assets/1b643c63-1339-4ed3-8a7e-bb1dc01f98f2" /
<img width="930" height="499" alt="Assign 12 3" src="https://github.com/user-attachments/assets/c2e242ac-f63f-4676-83a6-21eb26b16da0" />


1. In your notebook, write in your own words:
   - What a merge conflict is
   - What each of these markers means:
     - `<<<<<<<`
     - `=======`
     - `>>>>>>>`
   - What “Current changes” means
   - What “Incoming changes” means
   - Three possible ways to resolve a conflict (accept current / accept incoming / write manually)
   - Why we must delete the conflict markers before finishing
3. Add one small example of how a conflicted file looks (you can copy the style from the shopping-list example taught in class).


**Submit:**
- Photos of the answers of the above questions.

**Answers**

<img width="994" height="1280" alt="WhatsApp Image 2026-08-28 at 7 00 20 PM" src="https://github.com/user-attachments/assets/94cf8775-7af6-479c-99d9-26093a69b8e6" />
<img width="1600" height="1151" alt="WhatsApp Image 2026-08-28 at 7 01 08 PM" src="https://github.com/user-attachments/assets/c0cefadc-ba2c-4e64-8fca-ea412b6fb0e4" />

write answer in your own words in your notebook:

1. What causes a merge conflict?
2. After resolving a conflict on GitHub, why do we still need to run `git pull` on local `main`?
3. What is the difference between `git branch -d` and `git branch -D`?
4. Write the cleanup commands you used after merging the conflicted PR (delete remote + delete local + pull).

Commit and push the file to `main`.

**Submit:** - Photos of the answers of the above questions

**Answers**

<img width="1600" height="889" alt="WhatsApp Image 2026-08-28 at 7 01 32 PM" src="https://github.com/user-attachments/assets/a934327b-adf1-4411-939b-377ecc6e216c" />
<img width="1600" height="1006" alt="WhatsApp Image 2026-08-28 at 7 01 58 PM" src="https://github.com/user-attachments/assets/980b8b2a-8a04-4426-ba67-1121981ad14c" />







