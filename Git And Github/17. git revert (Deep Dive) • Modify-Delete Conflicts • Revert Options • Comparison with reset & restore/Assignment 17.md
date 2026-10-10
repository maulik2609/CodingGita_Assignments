# Assignment - git revert • Modify/Delete Conflict • Revert Options • Comparison with reset & restore

---

## Instructions

- Use your **CodingGita_Assignment** repository for all practical work and submission.
- Complete the assignments in order.
- For theoretical questions → write a short and correct answer in your notebook.
- Take clear photos of the written answers.
- Take screenshots of terminal / GitHub where asked.
- Push your practical work to the repository and submit the repository link along with the required photos and screenshots.

**Before you start:** Make sure your working directory is clean (`git status`).

---

## Assignment 1 – Basic Revert Practice

**Goal:** Perform a simple revert and observe the new commit.

1. Create 2–3 commits on any file (for example `index.html` or `notes.txt`).
2. Using `git log --oneline`, note the commit hash of the latest commit.
3. Revert the latest commit:
   ```bash
   git revert HEAD
   ```
   (or use the commit hash)
4. Run `git log --oneline` and observe the new revert commit.

**Submit:**
- Screenshot of `git log --oneline` before revert
- Screenshot of `git log --oneline` after revert
- Repository link

**Answer**

<img width="960" height="548" alt="Screenshot 2026-09-14 102422" src="https://github.com/user-attachments/assets/b77da9df-af82-4f6f-9c18-c0b8467b481a" />
<img width="960" height="554" alt="Screenshot 2026-09-14 102510" src="https://github.com/user-attachments/assets/c0e30683-d4d7-4eda-a07d-3ab0ce9861c1" />
https://github.com/maulik2609/Assignment-17-.git


## Assignment 2 – Modify/Delete Conflict during Revert

**Goal:** Face and resolve a Modify/Delete conflict while reverting.

1. Create a commit that **adds a new file**.
2. Make one more commit after that.
3. Try to revert the commit that added the file.
4. A Modify/Delete conflict should appear.
5. Resolve it (either delete the file or keep it with required content).
6. Use:
   ```bash
   git add .
   git revert --continue
   ```

**Submit:**
- Screenshot of the conflict (VS Code or terminal)
- Screenshot after successful `git revert --continue`
- Repository link

**Answer**
<img width="960" height="558" alt="Screenshot 2026-09-14 103638" src="https://github.com/user-attachments/assets/f4c56c80-3f61-4500-ac08-692431db4d57" />

https://github.com/maulik2609/Assig.17-2.git

## Assignment 3 – Revert Options + Conceptual Questions

**Goal:** Practice important flags and understand the concepts.

### Practical Part
1. Demonstrate any two of the following commands with a real commit:
   - `git revert --no-edit <commit_id>`
   - `git revert --no-commit <commit_id>`
   - `git revert --abort`
2. Take screenshots of the commands and their results.

### Theoretical Part (Write in Notebook)
Write short and correct answers for the following:

1. What does `git revert` do?
2. Why is `git revert` safer than `git reset` on a shared branch?
3. What is a Modify/Delete conflict? When can it occur during revert?
4. What is the difference between `git revert --abort` and `git revert --quit`?
5. Write one major difference each between:
   - `git restore`
   - `git reset`
   - `git revert`

**Submit:**
- Screenshots of the two practical commands you tried
- Clear photos of the written answers from your notebook
- Repository link

  **Answers**
  <img width="947" height="551" alt="Screenshot 2026-09-14 105143" src="https://github.com/user-attachments/assets/31b21fd6-ca89-4a4f-b07e-b3a8bd550de6" />
  <img width="960" height="536" alt="Screenshot 2026-09-14 105251" src="https://github.com/user-attachments/assets/07b2e0f7-b0cb-451d-95f0-3cb5b14ab0a7" />
<img width="1013" height="1280" alt="WhatsApp Image 2026-09-14 at 11 19 06 AM" src="https://github.com/user-attachments/assets/bc95cdd4-6df2-48b8-9117-e0f725d9e835" />
<img width="1600" height="1169" alt="WhatsApp Image 2026-09-14 at 11 19 37 AM" src="https://github.com/user-attachments/assets/5b11ad50-cdd8-40ff-98e2-8bdf1bfcd3dd" />
https://github.com/maulik2609/PRACTICAL.git





  





