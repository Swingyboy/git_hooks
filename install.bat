Invoke-WebRequest https://raw.githubusercontent.com/Swingyboy/git_hooks/main/git_hook.py -OutFile ./.git/hooks/pre-commit
cd ./.git/hooks/
git config hooks.gitleaks true