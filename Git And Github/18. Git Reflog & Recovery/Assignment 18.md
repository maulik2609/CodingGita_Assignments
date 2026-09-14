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




