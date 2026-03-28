#!/usr/bin/env python3
"""
GitHub Setup Helper for LAN File Share
This script helps you push your project to GitHub and set up automatic APK builds.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"\n{'=' * 60}")
    print(f"▶ {description}")
    print(f"{'=' * 60}")
    print(f"Command: {cmd}\n")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Success: {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description}")
        print(f"Error code: {e.returncode}")
        return False

def get_user_input(prompt, default=""):
    """Get user input with optional default."""
    if default:
        display = f"{prompt} [{default}]: "
    else:
        display = f"{prompt}: "
    
    user_input = input(display).strip()
    if not user_input and default:
        return default
    return user_input

def main():
    print("\n" + "=" * 60)
    print("🚀 LAN File Share - GitHub Setup Helper")
    print("=" * 60)
    
    # Check if git is initialized
    if not os.path.exists(".git"):
        print("\n❌ Git repository not found!")
        print("Run 'git init' first or check your working directory.")
        sys.exit(1)
    
    # Get GitHub credentials
    print("\n" + "=" * 60)
    print("Step 1: GitHub Account Information")
    print("=" * 60)
    
    username = get_user_input("Enter your GitHub username")
    if not username:
        print("❌ Username is required!")
        sys.exit(1)
    
    repo_name = get_user_input("Enter repository name (default: lan-file-share)", "lan-file-share")
    
    print("\n⚠️  Important: Make sure you've created the repository on GitHub first!")
    print(f"   Go to: https://github.com/new")
    print(f"   Repository name: {repo_name}")
    print(f"   Do NOT initialize with README, .gitignore, or license")
    
    confirm = get_user_input("\nHave you created the repository? (yes/no)", "no")
    if confirm.lower() not in ['yes', 'y']:
        print("\n❌ Please create the repository first, then run this script again.")
        sys.exit(1)
    
    # Configure git
    print("\n" + "=" * 60)
    print("Step 2: Configuring Git")
    print("=" * 60)
    
    email = get_user_input("Enter your Git email")
    if email:
        run_command(f'git config user.email "{email}"', "Setting git email")
    
    # Add README if not already committed
    print("\n" + "=" * 60)
    print("Step 3: Updating Repository")
    print("=" * 60)
    
    run_command("git add README.md .gitignore", "Adding README and .gitignore")
    run_command('git commit -m "docs: Update README and add .gitignore" --allow-empty', "Committing updates")
    
    # Add remote and push
    print("\n" + "=" * 60)
    print("Step 4: Pushing to GitHub")
    print("=" * 60)
    
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    print(f"\nRemote URL: {remote_url}")
    
    run_command(f'git remote add origin "{remote_url}"', "Adding remote")
    run_command("git branch -m master main", "Renaming branch to main")
    run_command("git push -u origin main", "Pushing to GitHub")
    
    # Final instructions
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    
    print(f"""
Your project is now on GitHub!

📍 Repository: https://github.com/{username}/{repo_name}

Next steps:

1. **Enable GitHub Actions**:
   - Go to your repository
   - Click "Actions" tab
   - Click "Enable Actions"

2. **Wait for First Build**:
   - The workflow will start automatically
   - Check the "Actions" tab for progress
   - Wait 10-20 minutes for the build to complete

3. **Download APK**:
   - Go to Actions → Latest workflow run
   - Download "apk-debug" artifact
   - Extract the .apk file
   - Transfer to Android device and install

4. **Automatic Builds**:
   - Every time you push code, APK rebuilds automatically
   - APK available in Actions artifacts

For more info, see README.md in your repository.

Happy sharing! 🎉
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
