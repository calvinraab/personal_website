# How to Update the Site

1. **Log into PythonAnywhere**:

   - Navigate to the PythonAnywhere console and open the console for the correct virtual environment:  
     **`personal_website_vert_env`**.

2. **Ensure You’re in the Right Directory**:

   - Check that you’re in the correct directory for your `personal_website` project:
     ```bash
     pwd
     ```
   - If not, navigate to the correct folder:
     ```bash
     cd /path/to/personal_website
     ```

3. **Switch to the `main` Branch**:

   - Ensure you are on the `main` branch:
     ```bash
     git checkout main
     ```

4. **Fetch and Reset to the Latest Remote Version**:

   - Fetch the latest changes from the remote repository:
     ```bash
     git fetch origin
     ```
   - Reset your local branch to match the remote:
     ```bash
     git reset --hard origin/main
     ```

5. **Confirm the Update**:

   - Verify that the site files are updated by listing the contents of the directory:
     ```bash
     ls -l
     ```

6. **Restart the Web Application (if necessary)**:
   - If your app requires a restart after updates, restart it from the PythonAnywhere dashboard or by running:
     ```bash
     touch /path/to/your_wsgi_file.py
     ```

---
