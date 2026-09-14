# 📝 Assignment: Git Reflog & Recovery

## 🎯 Objective
Practice recovering lost commits and reworking old commits using `git reflog`, detached HEAD, and branching strategies.

***

## 📋 Part 1: Recovery After `git reset --hard` (5 Points)

### Task
1. Create a new repository called `reflog-practice-part1`
2. Create 3 commits:
   - **C0:** `README.md` with project title
   - **C1:** `index.html` with `<h1>Welcome</h1>`
   - **C2:** `style.css` with basic styling
3. Accidentally delete C1 and C2 using `git reset --hard <C0-commit-hash>`
4. Use `git reflog` to find the lost C2 commit
5. Recover C2 (and C1) using detached HEAD + branch + merge
6. Verify all commits are restored

**Answers**

<img width="960" height="559" alt="Screenshot 2026-09-14 113000" src="https://github.com/user-attachments/assets/75d83cdc-4d3a-4fc6-83dc-714070df2c76" />
<img width="960" height="564" alt="Screenshot 2026-09-14 113045" src="https://github.com/user-attachments/assets/eef95d4b-03ab-4031-af49-7e95bd20dfd0" />
<img width="960" height="549" alt="Screenshot 2026-09-14 115949" src="https://github.com/user-attachments/assets/0cc0fd35-542f-401b-aaf6-43fcd1c68c7f" />
<img width="960" height="553" alt="Screenshot 2026-09-14 115720" src="https://github.com/user-attachments/assets/058b6425-a209-4922-b6c1-18f3b718ecf1" />
https://github.com/maulik2609/Assignment-18.git


## 📋 Part 2: Reworking Old Commit (5 Points)

### Task
1. Create a new repository called `reflog-practice-part2`
2. Create 3 commits:
   - **C0:** `README.md` with just title
   - **C1:** `app.js` with basic function
   - **C2:** `utils.js` with helper functions
3. Realize you need to add description to README (C0) without losing C1 and C2
4. Create a branch at C0: `git switch -c rework/readme-update <C0-hash>`
5. Update README.md with description, commit
6. Merge the branch back to main
7. Verify C0, C1, and C2 are all preserved

**Answers**
<img width="960" height="564" alt="Screenshot 2026-09-14 120958" src="https://github.com/user-attachments/assets/8fe02f65-99bf-4583-bb5e-218f91630f3b" />
<img width="947" height="559" alt="Screenshot 2026-09-14 121022" src="https://github.com/user-attachments/assets/0b6b71a0-5e65-4163-8423-d7f932f4c0e7" />
<img width="960" height="558" alt="Screenshot 2026-09-14 121219" src="https://github.com/user-attachments/assets/b3ea2cf2-2e63-4da4-8464-bb8f98de702b" />
https://github.com/maulik2609/reflog-practice-part2.git









