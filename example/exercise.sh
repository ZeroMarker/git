--- push existing repo to github
git init
git add -A
git commit -m 'Added my project'
git remote add origin git@github.com:sammy/my-new-project.git
git push -u -f origin main

Show difference between local and remote branches
git fetch origin
git diff --name-only main origin/main
