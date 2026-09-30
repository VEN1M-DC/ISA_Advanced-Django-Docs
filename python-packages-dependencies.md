# Python Packages and Dependencies

Contributor: **ISA SAMIEZADE-YAZD**

AI-assisted review draft. Practice these commands and revise the explanations to reflect your understanding before submission.

## Packages dependencies and pip

An installable distribution provides reusable Python code. A dependency is software your project needs; dependencies can have dependencies of their own. `pip` installs and manages distributions. Installing Python supplies the interpreter; installing Django adds a framework to an interpreter's environment.

Activate your [virtual environment](python-virtual-environments.md) first. Using `python -m pip` selects pip for that interpreter.

```bash
python -m pip --version
python -m pip install Django
python -m pip show Django
python -m pip list
python -m pip check
```

`show` reports one distribution's metadata, `list` shows installed versions, and `check` detects missing or incompatible declared dependencies. A successful check does not prove application behavior is correct.

## Package versions

An unpinned installation selects a compatible available release according to pip's resolver. Compare your Python version with the intended Django release's official compatibility documentation before installing.

Requirement syntax examples, not installation recommendations:

| Expression | Meaning |
| --- | --- |
| `Django==5.2.1` | Exactly that version |
| `Django>=5.2,<5.3` | At least 5.2 and below 5.3 |

Exact pins make versions explicit; ranges permit changes. Test application behavior after dependency changes.

## Create requirements.txt

From a clean project environment, inspect the snapshot:

```bash
python -m pip freeze
```

Write UTF-8 consistently across Windows PowerShell and other shells:

```bash
python -c "import pathlib, subprocess, sys; pathlib.Path('requirements.txt').write_text(subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], text=True), encoding='utf-8')"
```

This overwrites `requirements.txt`; inspect an existing file before replacing it. The command avoids older Windows PowerShell redirection producing UTF-16 output.

`freeze` records installed distributions, including indirect dependencies, while omitting certain packaging tools by default. It snapshots the environment rather than determining which packages your application actually uses. It is not a full lockfile or a guarantee of identical behavior across operating systems and Python versions. Review entries for unrelated packages or machine-specific paths before committing.

## Recreate dependencies

A teammate creates and activates a fresh environment, then runs from the directory containing the file:

```bash
python -m pip install -r requirements.txt
python -m pip check
```

Share `requirements.txt` and source code through Git, rather than the machine-specific `djvenv` directory. Document the project's Python version separately. The requirements file belongs to the individual application repository; this shared repository contains instructions.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| `ModuleNotFoundError` | Confirm the executing interpreter and pip use the same environment. |
| No matching distribution | Check the package spelling, requested version, Python support, and platform support. |
| Requirements file not found | Check the current directory and file path. |
| Dependency conflict | Read the conflicting version constraints and choose compatible versions. |

## Practice and sources

Explain one installed package's role, then compare `pip list` with `requirements.txt`. Record actual observations rather than assuming the commands succeeded.

- [pip user guide](https://pip.pypa.io/en/stable/user_guide/)
- [pip freeze reference](https://pip.pypa.io/en/stable/cli/pip_freeze/)
- [Django Python compatibility](https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django)
- [Team documentation](README.md)

AI disclosure: AI assisted with this draft and examples. Add what you personally ran, verified, and learned.

## How requirements relate to compatibility

Checking compatibility comes first: choose a Django release that supports the project's Python version. After installing and checking the project dependencies, save their versions in `requirements.txt`. Another developer can use that file to install the recorded packages in a fresh environment.

The file does not install or select the Python interpreter. Record the Python version separately in the project's README, and check it before installing requirements:

```bash
python --version
python -m pip install -r requirements.txt
python -m pip check
```

For my setup, the activated environment screenshot showed Python 3.14.7. That screenshot alone does not confirm the installed Django version. To check Django in an activated environment, run:

```bash
python -m django --version
```

If Python reports that Django is missing, it is not available to that interpreter. Verify the selected environment before installing the chosen compatible release.

Sharing `requirements.txt` is more practical than sharing `djvenv`: the file is small and records dependencies, while the environment includes installed files and paths tied to a particular computer. Each teammate should create their own environment and install the requirements there.
