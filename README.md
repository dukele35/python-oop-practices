# python-oop-practices
this repo collects sub-repos featuring projects in python oop
# PRE-COMMIT HOOKS
## A. Introduction
Pre-commit hooks allow you to locally check and possibly reformat your code in terms of code styles, security issues, etc. before pushing your code onto Bitbucket. If any pre-commit hooks fail, you are not allowed to push your code. You could push your code onto Bitbucket if the failed hooks are chosen to be skipped.

The configuration file for pre-commit hooks is `.pre-commit-config.yaml`. There are four hooks as follows: 1. Default hooks from pre-commit include `trailing-whitespace`, `end-of-file-fixer` & `requirements-txt-fixer`. Those hooks are for checking(1) redundant white spaces (2) ensuring file is either empty, or ends with one newline (3) sorting entries in requirements.txt alphabetically. 2. black hook is for automatically reformatting & standardising python files. 3. flake8 hook is for checking styles of python code. 4. bandit hook is for checking security issue in python code.

## B. How to use
### B.1. First time use:
- First, install pre-commit package by running `pip install pre-commit`
- Second, run `pre-commit install` to set up the git hook scripts. After this, pre-commit will run automatically on git commit.

### B.2. Have a new change & about to commit your code:
- First, run `git add .` to add changes to the staging area of git. Then, run `pre-commit run - -all-files` for the first time use or pre-commit run to check if there is any issue regarding styling and securituy for your code. It also automatically reformats your code with the black hook.
- Second, run `git status` to see files being affected. Then, run `git add .` again to add new changes to the staging area of git. After that, run `pre-commit run` to see what's left for the code which could be not automatically reformatted by the black hook. After this step, you should manually modify your code.
- Finally, if all code is fixed, you now could run again `git add .`, `git commit - m < commit message >` & `git push`.
NB. You could not push your code if any hooks fail. You might need to use `SKIP=<hook-id> git commit - m <commit-message>` or `git commit - m <commit-message> --no-verify` to commit your chages with failed hook(s).
