**Conflict during `git pull`**

**Goal:** Face and resolve a conflict that appears when you run `git pull origin main`.

1. On GitHub (remote `main`), create a file `welcome.txt` with the content:  
   `Welcome to Git class`
2. Commit it directly on GitHub.
3. On your **local main**, create the same file `welcome.txt` with different content:  
   `Welcome to Day 13`
4. Run:
   ```bash
   git add welcome.txt
   git commit -m "Add welcome.txt locally"
   git pull origin main
   ```
5. A conflict will appear. Resolve it by keeping **both** lines (or any final version you prefer).
6. Remove all conflict markers, then:
   ```bash
   git add welcome.txt
   git commit -m "Resolve pull conflict in welcome.txt"
   git push origin main
   ```

**Submit:**
- Screenshot of the conflict markers
- Screenshot of the final resolved file on GitHub
- Repository link

- **Answers**
https://github.com/maulik2609/Assi-13-.git

<img width="954" height="564" alt="Screenshot 2026-08-29 170244" src="https://github.com/user-attachments/assets/4ee382d7-5ff9-43e9-bdd8-682127cd77a1" />
<img width="938" height="554" alt="Screenshot 2026-08-29 170449" src="https://github.com/user-attachments/assets/e6863e72-7249-47e2-abeb-fe36d42a6a12" />




  
