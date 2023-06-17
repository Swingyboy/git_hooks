# GIT HOOK FOR PRE-COMMIT

## Description
This is a simple pre-commit git hook written on Python3 that scans your staged files and checks if there any sensitive info presents. It uses **gitleaks** project (https://github.com/gitleaks/gitleaks-action) under the hood. If gitleaks wasn't installed this hook would install it ot HOME derectory in the *"gitleaks"* dir. 

## Requirements
 * Python v3.10 or higher

## Installation
 * **Linux/Mac OS:**
 Open terminal in the directory with git repo and execute ```curl https://raw.githubusercontent.com/Swingyboy/git_hooks/main/install.sh | sh```
 * **Windows:** Download *install.ps1* script to the directory with git repo and execute it.
 * **Manual:** Download git_hook.py and save it to *./.git/hook* with a new name *pre-commit*

 ## Usage
 To enable code scanning before commit it is necessary to add the *gitleaks* option to *hooks* section of git configs:
 ```git config hooks.gitleaks true```
 After that gitleaks would scan your staged files for any sensitive info. If sensitive info would be found the commit would be rejected. 