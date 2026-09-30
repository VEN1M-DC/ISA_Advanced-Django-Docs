# Git and GitHub Development Environment

Contributor: **ISA SAMIEZADE-YAZD**

Git records changes locally. GitHub hosts repositories online and provides collaboration tools. A repository contains project files and version history. Saving a file in an editor, committing it with Git, and pushing it to GitHub are separate steps.

## Work with this repository

Clone only when you need a new local copy:

```bash
git clone https://github.com/VEN1M-DC/ISA_Advanced-Django-Docs.git
cd ISA_Advanced-Django-Docs
git status
```

If you already have a checkout, open that folder instead. `origin` is the usual name for its remote. `git remote -v` shows the configured URLs.

## Branch edit review and publish

Start with a clean working tree. Pull incoming work before making a branch:

```bash
git switch main
git pull --ff-only
git switch -c docs/improve-navigation
```

Edit and save the intended file. Then inspect the changes before committing:

```bash
git diff
git add README.md
git diff --cached
git commit -m "Clarify documentation navigation"
git push -u origin docs/improve-navigation
```

Staging selects content for the next commit. A branch keeps a line of development separate until merged. Open a pull request on GitHub to review the branch and merge it into `main`. Pushing a branch alone does not merge it.

Version control provides a history of decisions, a way to compare or restore earlier work, and a shared process for reviewing contributions. A push copies committed history; it does not back up ignored or uncommitted files.

## GitHub Desktop

Use **File > Clone repository** to clone the repository URL into a local folder. Select the correct repository and branch. Fetch and pull incoming changes before editing. In Changes, inspect the diff, select the files to include, enter a clear summary, and commit. Push or publish the branch, then open a pull request if appropriate.

Use History to inspect saved commits. Verify the expected files and branch on GitHub after pushing. Capture your own Changes or History screenshots when the assignment requires them.

## Files to track and ignore

Track source files, templates, static assets, documentation, `requirements.txt`, `.gitignore`, and Django migration files. In an application repository, a starting `.gitignore` can contain:

```gitignore
djvenv/
.venv/
__pycache__/
*.py[cod]
.env
.env.*
!.env.example
db.sqlite3
.DS_Store
```

An example environment file should contain placeholders only. The SQLite rule is for a disposable local development database, not migration source files. Each developer recreates the environment from requirements rather than downloading someone else's installed environment.

Ignore patterns affect untracked files. If an unwanted file is already tracked, `git rm --cached path/to/file` removes that specific path from the index while keeping the local copy. Review the result and commit. Removing a secret from the current version does not erase history; revoke or rotate exposed credentials.

## Troubleshooting

| Symptom | What to do |
| --- | --- |
| Changes missing online | Check whether they were saved, committed, pushed, and viewed on the correct branch |
| Push rejected | Fetch and inspect incoming changes; do not force-push over shared work |
| Merge conflict | Read both versions, resolve the conflicting content, remove conflict markers, check the result, and commit |
| Unexpected staged files | Use `git restore --staged path/to/file` to unstage without deleting the working copy |
| Authentication failure | Check account access and the configured remote; never put credentials into documentation |

If a merge becomes confusing, `git merge --abort` cancels an in-progress merge. Commit or otherwise preserve unrelated work before beginning merges.

## Repository and website links

A repository link shows files and history. GitHub Pages publishes static content as a website. Configure its publishing source under the repository's Pages settings, then verify deployment and navigation. The repository being public does not by itself prove Pages is configured. Django needs separate hosting that executes Python.

Sources: [Git tutorial](https://git-scm.com/docs/gittutorial), [Git ignore rules](https://git-scm.com/docs/gitignore), [GitHub Desktop](https://docs.github.com/en/desktop), [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

[Back to documentation](README.md)
