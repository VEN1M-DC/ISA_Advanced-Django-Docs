---
layout: default
---

# Command Line

Contributor: **ISA SAMIEZADE-YAZD**

The command line lets you give a computer instructions by typing. A terminal displays the session, while a shell such as PowerShell or Bash interprets the commands. Developers use it to navigate folders, run Python, start a server, and work with Git.

## Know your location

Commands usually act on the current folder. Check it before creating files or running project commands. An absolute path identifies a full location; a relative path starts from where you are now. `.` means the current directory and `..` means its parent.

| Task | Windows PowerShell | Bash on Linux macOS or Git Bash |
| --- | --- | --- |
| Show current folder | `Get-Location` | `pwd` |
| List files | `Get-ChildItem` | `ls` |
| Include hidden files | `Get-ChildItem -Force` | `ls -a` |
| Enter a folder | `Set-Location practice` | `cd practice` |
| Move up one folder | `Set-Location ..` | `cd ..` |
| Create a folder | `New-Item practice -ItemType Directory` | `mkdir practice` |
| Create an empty file | `New-Item notes.txt -ItemType File` | `touch notes.txt` |
| Read a file | `Get-Content notes.txt` | `cat notes.txt` |
| Copy a file | `Copy-Item notes.txt backup.txt` | `cp notes.txt backup.txt` |
| Rename a file | `Move-Item backup.txt saved.txt` | `mv backup.txt saved.txt` |

These examples assume the destination names are unused. `touch` changes timestamps when the file already exists. Quote paths containing spaces. Git Bash commonly represents the Windows C drive as `/c/`.

## Practice in a separate folder

Run these once in a directory where you want a new practice folder:

```powershell
Get-Location
New-Item terminal-practice -ItemType Directory
Set-Location terminal-practice
New-Item notes.txt -ItemType File
Set-Content notes.txt 'Check the current directory before running setup.'
Get-Content notes.txt
Get-ChildItem
```

The expected result is a `notes.txt` file containing the sentence. `Set-Content` replaces existing content, so check the target first. Edit the file in VS Code, save it, and run `Get-Content` again to see the change.

If the VS Code command is installed, `code .` opens the current folder. `Ctrl+C` usually stops a running foreground command, such as Django's development server.

## Common mistakes

- **Wrong directory:** a command may work but create files in the wrong location. Check your path first; do not create project environments in `C:\Windows\system32`.
- **Command not found:** check the shell, spelling, installation, and PATH. PowerShell aliases do not make every Bash command available.
- **Path not found:** list the directory and check the folder name. Enter the real path rather than a tutorial placeholder.
- **Unexpected continuation prompt:** an unclosed quote or bracket can make the shell wait for more input. Press `Ctrl+C`, then re-enter a complete command.

Do not paste prompt characters such as `PS>` or `>>>` as part of commands. Use [virtual environments](python-virtual-environments.md) for the next setup step.

Sources: [PowerShell current location](https://learn.microsoft.com/en-us/powershell/scripting/samples/managing-current-location), [Bash manual](https://www.gnu.org/software/bash/manual/).

[Back to documentation](index.md)
