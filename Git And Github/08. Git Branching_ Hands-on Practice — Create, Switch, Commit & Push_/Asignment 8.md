**Objective:** Check basic understanding of branching.

**Tasks:**
1. What is a **branch** in Git? Explain in your own words.
2. Why should we **not** work directly on the `main` branch?
3. Explain the road analogy of branching (main road vs side road).
4. What is the difference between `git branch` and `git switch`?

**Submission:** Written answers in your notebook.
 **Answers**
<img width="1493" height="1600" alt="WhatsApp Image 2026-08-25 at 5 13 12 PM" src="https://github.com/user-attachments/assets/3c36d30b-185e-455d-b48c-21f9b2cc6442" />

**Objective:** Identify the correct commands.

**Tasks:**
1. Write the command for the following actions:

| Action                              | Command |
|-------------------------------------|---------|
| List all branches                   |         |
| Create a new branch named `feature-home` |    |
| Switch to `feature-home`            |         |
| Create + Switch in one command      |         |
| Merge `feature-home` into main      |         |
| Delete `feature-home` after merge   |         |

2. Write both the **modern** and **older** command for:
   - Switching to a branch
   - Creating + switching to a new branch

**Submission:** Filled table + answers
*Answers**
<img width="1600" height="1592" alt="WhatsApp Image 2026-08-25 at 5 21 40 PM" src="https://github.com/user-attachments/assets/c1450820-efcc-49bc-9f57-4aaa21621015" />

**Objective:** Perform the complete branching cycle.

**Tasks:**
1. Make sure you are on the `main` branch.
2. Create a new branch named `feature-contact`.
3. Create a file `contact.txt` and write your name + any message.
4. Stage and commit the file with a meaningful message.
5. Switch back to `main`.
6. Merge `feature-contact` into `main`.
7. Delete the `feature-contact` branch.
8. Verify using:
   - `git branch`
   - `git log --oneline`

**Submission:**  
- Screenshot of `git branch` (before and after)  
- Screenshot of `git log --oneline`  
- Screenshot showing `contact.txt` is present on `main`

**Answers**
<img width="1920" height="1196" alt="Screenshot 2026-08-15 101801" src="https://github.com/user-attachments/assets/aae94400-4050-4a91-8d07-456d97aa3d67" />



**Objective:** Understand rules and common mistakes.

**Tasks:**
1. What will happen if you try to delete a branch that is not yet merged?  
   Write the error and how to fix it.
2. Why should you always **commit** before switching branches?
3. Fill in the correct flow:

```
______ → Work → ______ → ______ → Switch to main → ______ → Delete branch
```

4. Explain the difference between:
   - `git branch -d branch-name`
   - `git branch -D branch-name`

**Submission:** Written answers

**Answers**

<img width="1600" height="600" alt="WhatsApp Image 2026-08-25 at 5 29 04 PM" src="https://github.com/user-attachments/assets/fc54e414-b1df-45dc-8748-452a597cbc5b" />
<img width="1600" height="795" alt="WhatsApp Image 2026-08-25 at 5 31 26 PM" src="https://github.com/user-attachments/assets/0df81c70-e337-440c-aa3c-0f57ad873d25" />

**Objective:** Apply branching in a realistic situation.

**Scenario:**  
You are working on a website project. Currently you are on the `main` branch. You need to add two new pages: **About** and **Services**.

**Tasks:**
1. Create a branch `feature-about`, add a file `about.txt`, commit it, merge it into `main`, and delete the branch.
2. Create another branch `feature-services`, add a file `services.txt`, commit it, merge it into `main`, and delete the branch.
3. After completing both, show:
   - Final list of branches (`git branch`)
   - Final commit history (`git log --oneline`)
4. Answer:
   - Why did we create two separate branches instead of doing both features on one branch?
   - What is the advantage of merging only after the feature is complete?

**Submission:**  
- Screenshots of both merges  
- Final `git branch` and `git log --oneline`  
- Written answers for the two questions

- **Answers**
<img width="1912" height="1194" alt="Assign 8" src="https://github.com/user-attachments/assets/aa6a4a5b-1be6-4b84-98c7-83b39f5cb515" />
<img width="1912" height="1195" alt="Assign 8 2" src="https://github.com/user-attachments/assets/c1773854-2bae-4a59-b179-dc0f56db7124" />
<img width="1599" height="1060" alt="WhatsApp Image 2026-08-25 at 5 34 43 PM" src="https://github.com/user-attachments/assets/c57ae53b-c495-438b-8fb0-47119ad7f838" />



  







 
