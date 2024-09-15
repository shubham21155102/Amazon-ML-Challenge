# Increase the buffer size for git
git config --global http.postBuffer 524288000 
git remote set-url origin git@github.com:shubham21155102/Amozon-ML.git
3. Check for Large Files

# If the repository contains large files that exceed GitHub’s file size limits, you may need to use Git Large File Storage (LFS). You can identify large files in your repository using:
git rev-list --objects --all | sort -k 2 > allfiles.txt

pip freeze > requirements.txt