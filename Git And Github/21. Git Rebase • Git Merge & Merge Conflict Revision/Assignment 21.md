# Assignment: Git Rebase, Git Merge & Merge Conflict

**Instructions:** Attempt all questions. Use proper Git commands and show the required commit history wherever asked.

---

## Q1. Rebase, Merge & Merge Conflict 

Answer the following:

1. Define **Git Merge**, **Merge Conflict**, and **Git Rebase**.
2. Explain **Merge vs Rebase** with a suitable diagram.
3. Write three advantages of Git Rebase.
4. Explain why Rebase is useful in real-life projects.
5. Explain the purpose of:

   * `git rebase --continue`
   * `git rebase --abort`
   * `git rebase --skip`
     
**Answers**

<img width="1024" height="1280" alt="WhatsApp Image 2026-09-16 at 5 17 16 PM" src="https://github.com/user-attachments/assets/ee88472f-e627-4578-a9a5-be3f9bb55b87" />
<img width="1600" height="1479" alt="WhatsApp Image 2026-09-16 at 5 17 37 PM" src="https://github.com/user-attachments/assets/d183cf8c-f762-4b99-a1b2-b84adc306951" />

### Tasks

1. Show the commit history using a diagram similar to:

```text
A---B---C---D  main
     \
      E---F    product-page
```

Use your **own meaningful commit messages** instead of `A, B, C...`.

2. Merge `product-page` into `main`.
3. Show the commit history after the merge (submit the screenshot).
4. Reset/recreate the scenario if required and perform a **rebase of `product-page` onto `main`**.
5. Show the commit history after the rebase(submit the screenshot).
6. Write **two differences** you observed between the merge and rebase results.

 
** Submission ** : GitHub Repo link + Screenshots + Photos of written answers

**Anwers**
https://github.com/maulik2609/rebase-assign.git
<img width="960" height="560" alt="Screenshot 2026-09-16 173624" src="https://github.com/user-attachments/assets/4209f98f-1657-41f6-8392-dda8fbdaf7b7" />
<img width="960" height="557" alt="Screenshot 2026-09-16 173859" src="https://github.com/user-attachments/assets/7d5559f4-467a-4f29-b7f9-625d4dde986e" />


# Q3. Rebase Conflict

### Scenario: Student Management System

You are developing a student management system.

Create your own Git scenario using:

* `main` branch
* `student-profile` branch

### Tasks

1. Create the `student-profile` branch from `main`.
2. On `student-profile`, make **two commits** related to the student profile.
3. Switch to `main` and make a change to the **same line of the same file**.
4. Switch back to `student-profile`.
5. Rebase `student-profile` onto `main`:

```bash
git rebase main
```

6. Resolve the rebase conflict.
7. Complete the rebase using:

```bash
git add .
git rebase --continue
```

8. Create another small rebase-conflict scenario and demonstrate:

```bash
git rebase --abort
```

Explain what happened to the branch after aborting.

9. Demonstrate:

```bash
git rebase --skip
```

Explain which commit was skipped.

10. Finally, display the commit history using following command and submit the screenshot:

```bash
git log --oneline --graph --all
```

** Submission ** : GitHub Repo link + Screenshots + Photos of written answers.

**Answers**

https://github.com/maulik2609/rebase-prac.git
<img width="953" height="542" alt="Screenshot 2026-09-16 175638" src="https://github.com/user-attachments/assets/f244be39-98ad-48a8-9f25-b7c669c57300" />
<img width="960" height="564" alt="Screenshot 2026-09-16 175940" src="https://github.com/user-attachments/assets/278674d0-1f12-4b9d-9801-dc9322701b9f" />
![Uploading Screenshot 2026-09-16 180009.png…]()








