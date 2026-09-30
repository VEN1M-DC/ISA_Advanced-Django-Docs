# Django Framework and Setup

Contributor: **ISA SAMIEZADE-YAZD**

Django is a Python web framework. It supplies common web application tools and a project structure so developers can focus on features instead of writing every supporting part themselves. This is abstraction: using a tool through its commands and interfaces without rebuilding all its internal behavior.

## Check versions first

Installing Python provides the interpreter; installing Django adds a framework to a Python environment. In the activated project environment, run:

```bash
python --version
python -m django --version
```

The setup screenshot recorded Python 3.14.7. Check Django separately; an activated environment does not prove Django is installed. Match the chosen release to the [official compatibility table](https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django). Use documentation for that release.

## Set up an individual project

Keep the application separate from this documentation repository. On Windows, use a new folder or an existing empty project folder:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\django-portfolio"
Set-Location "$env:USERPROFILE\django-portfolio"
py -m venv djvenv
.\djvenv\Scripts\Activate.ps1
```

Skip environment creation if it already exists. On macOS/Linux, navigate to your project folder, then use `python3 -m venv djvenv` and `source djvenv/bin/activate`.

Install the stable compatible release you selected. Replace `X.Y.Z` below with its actual version before running:

```bash
python -m pip install "Django==X.Y.Z"
python -m django --version
```

The version placeholder is intentionally not an installation command as written.

## Generate and inspect the project

Run once, from the project folder, before a `manage.py` file exists:

```bash
python -m django startproject django_project .
```

The final period uses the current directory rather than creating another outer folder.

| File | What it provides |
| --- | --- |
| `manage.py` | Commands for this project |
| `django_project/settings.py` | Application and database configuration |
| `django_project/urls.py` | URL routing |
| `django_project/__init__.py` | Python package marker |
| `django_project/asgi.py` and `wsgi.py` | Entry points for compatible servers |

A project combines settings and apps. An app provides a feature, such as a blog; a project may contain multiple apps.

## Run and verify

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

`check` inspects configuration. `migrate` applies database migrations. Open `http://127.0.0.1:8000/` while the development server is running. A newly generated project should display Django's installation success page. Record your actual terminal and browser results.

The browser is the client and Django's development process is the server. The browser requests a URL and receives a response. `localhost` refers to your computer; `127.0.0.1` is an IPv4 loopback address. This development server is not intended for production hosting.

## Stop restart and troubleshoot

Press `Ctrl+C` to stop the server and run `deactivate` when finished. Next time, return to the folder containing `manage.py`, activate the environment, and run the server again.

| Problem | Check or action |
| --- | --- |
| No module named django | Verify `python` points into `djvenv`, then install the chosen dependency there |
| Cannot open manage.py | Check the working directory |
| Port already in use | Stop the earlier server or use `python manage.py runserver 8001` and open port 8001 |
| Activation script blocked | Invoke `.\djvenv\Scripts\python.exe` directly instead of changing machine-wide policy |
| Unexpected import errors | Avoid filenames such as `django.py` that shadow packages |

Save dependencies using the [requirements instructions](python-packages-dependencies.md). Track project code and migration files with Git; ignore the environment, caches, secrets, and disposable local databases. GitHub Pages can publish static documentation but cannot execute the Django server.

Sources: [Django tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial01/), [Django commands](https://docs.djangoproject.com/en/6.0/ref/django-admin/), [Python environments](https://docs.python.org/3/library/venv.html).

[Back to documentation](README.md)
