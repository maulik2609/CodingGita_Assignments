# Q1. Theory — Understanding Cherry-Pick

Answer the following questions:

1. What is `git cherry-pick`?
2. What is the difference between **cherry-pick** and **merge**?
3. Does cherry-pick move the original commit? Explain.
4. Why does cherry-pick create a new commit?
5. What is the purpose of the following commands?

   * `git cherry-pick --continue`
   * `git cherry-pick --abort`
   * `git cherry-pick --skip`
6. What is the difference between:

   ```bash
   git cherry-pick <start_commit>..<end_commit>
   ```

   and

   ```bash
   git cherry-pick <start_commit>^..<end_commit>
   ```

   **Answers**
   <img width="966" height="1280" alt="WhatsApp Image 2026-09-19 at 2 54 52 PM" src="https://github.com/user-attachments/assets/4d00ea1f-1960-49e2-b5ae-e9ab5ea082bb" />
   <img width="1381" height="1080" alt="WhatsApp Image 2026-09-19 at 2 55 05 PM" src="https://github.com/user-attachments/assets/a5d28086-ba5f-4142-be96-74a5c0d46ee7" />

   # Q2. Practical — Cherry-Pick a Specific Commit

## Scenario

You are developing a **Student Management System**.

Create a new Git repository and create a file:

```text
Student.txt
```

Add:

```text
Student Management System
```

Commit it with a meaningful commit message.

### Tasks

1. Initialize the Git repository.
2. Create and commit `Student.txt`.
3. Create a new branch for student information.
4. Add information about **Rahul** and commit it.
5. Add information about **Amit** and commit it.
6. Switch back to `main`.
7. Find the commit ID of the **Amit** commit.
8. Cherry-pick only the **Amit** commit into `main`.
9. Display the commit history using:

```bash
git log --oneline --graph --all
```
**Answers**
https://github.com/maulik2609/cherry-pick.git
<img width="960" height="562" alt="Screenshot 2026-09-20 112338" src="https://github.com/user-attachments/assets/ca99956c-55dd-476e-b2e4-6c4b6330d168" />


   

