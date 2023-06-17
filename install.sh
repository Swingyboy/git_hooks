curl -o ./.git/hooks/pre-commit https://raw.githubusercontent.com/Swingyboy/git_hooks/main/git_hook.py
cd ./.git/hooks/
chmod +x pre-commit
git config hooks.gitleaks true