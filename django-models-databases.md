---
title: Django Models Databases and ORM
---

# Django Models Databases and ORM

Contributor: **ISA SAMIEZADE-YAZD**. Updated October 7, 2026. Study notes synthesized from the linked lecture with AI assistance.

## Build in useful iterations

Agile development uses small working increments, evidence, feedback, and reflection. A user story describes a user's need and purpose; acceptance criteria define observable success. Requirements describe what the system must do, while design describes how components will do it.

For the portfolio owner's identity story, acceptance criteria include a Student class with name, email, and major; a migration; a Student table; an automatic identifier; and records that can be saved and queried. Predict the outcome, implement one change, inspect it, and explain the evidence. Commit working increments instead of waiting for the whole application.

## Classes objects and UML

A class defines attributes and behavior. An instance is one particular object. Student is one class even when the database has two rows. UML class diagrams show class names, fields, methods, and relationships. Identify nouns as candidate classes and verbs as responsibilities, then refine the design with requirements. Single Responsibility encourages focused classes; DRY avoids repeating the same logic.

Student stores owner identity, Portfolio stores portfolio content, and Project represents a piece of work. The [relationship guide](django-model-relationships.md) explains their connections.

## From a Python class to a stored row

The model layer connects Python code with database information. Here is a reduced example; the application's complete Student model also defines the course major choices:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField("MSU Email")
    major = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
```

| Python concept | Database concept |
| --- | --- |
| Student model | portfolio_app_student table |
| name email major fields | Columns |
| Saved Student instance | Row |
| Automatically added id | Primary key |

`__str__` provides a readable object label. An email field validates email syntax through forms; it does not create an email account or password. Choices store codes such as CSCI-BS while forms display labels. Direct save operations do not automatically run all model validation; use forms or explicit validation when appropriate.

The database engine and file are configured in settings.py. This project's local SQLite database is db.sqlite3. Other backends may generate different SQL while using the same model API.

## Migrations schema and records

```powershell
python manage.py check
python manage.py makemigrations portfolio_app
python manage.py migrate
python manage.py showmigrations
python manage.py sqlmigrate portfolio_app 0001
```

`check` examines configuration. `makemigrations` writes schema-change instructions as Python migrations. `migrate` applies them and records their application. `showmigrations` reports their status, and `sqlmigrate` shows backend-specific SQL. A schema describes table structure; a row stores data. Adding a record in admin does not require a new migration.

Track model code and migration files in Git. Exclude the virtual environment, database, caches, and credentials. Each developer restores dependencies and migrates their own database; switching a Git branch does not restore a different db.sqlite3 automatically.

## Admin and identity

After migrating, create a local administrator with `python manage.py createsuperuser`. It inserts a user record and hashes the password; it does not generate a Python file. Register the model:

```python
from django.contrib import admin
from .models import Student
admin.site.register(Student)
```

Visit http://127.0.0.1:8000/admin/ on the server's computer. Saving an admin form creates or updates a row. Use fictional example data during practice. Inspect portfolio_app_student using VS Code's qwtel.sqlite-viewer extension. Confirm field values and identifiers without publishing credentials.

Django's automatic id illustrates the Identity Field pattern: a stable unique key distinguishes records even if names repeat. Model methods such as save and delete illustrate Active Record concepts by combining a row representation with persistence behavior.

## Managers QuerySets and SQL

Start `python manage.py shell` in the project folder:

```python
from portfolio_app.models import Student
Student.objects.all()
Student.objects.count()
Student.objects.filter(major="CSCI-BS")
Student.objects.first()
students = Student.objects.filter(major="CSCI-BS")
print(students.query)
list(students)
```

The default manager is objects. all and filter build QuerySets; count returns a number; first returns an instance or None. Assignment generally does not execute the query. Iteration, list conversion, and other evaluation operations retrieve data. QuerySet repr may also execute a limited query for display.

`print(students.query)` shows a SQL representation, not results or a safely executable SQL string. Values are parameterized during actual database execution. In development with DEBUG enabled, django.db.connection.queries can show recorded query details; it is not a production monitoring strategy.

| ORM operation | SQL idea | Recorded example result from October 5 |
| --- | --- | --- |
| all() | SELECT rows | Jordan Rivera and Taylor Morgan |
| count() | COUNT rows | 2 |
| filter(major="CSCI-BS") | WHERE condition | Jordan Rivera |
| first() | Ordered selection with limit | Jordan Rivera |
| list(students) | Evaluate filtered selection | One matching instance |

Those are historical local examples, not a guarantee of the current database contents. SQL reaches SQLite; Django converts returned rows into Python instances. Unlike an older screenshot in the lecture, the initial Student schema does not contain portfolio_id: the planned relationship puts student_id on Portfolio.

## Recovery and evidence

For unwanted example data, delete only the intended records through admin or the ORM. `python manage.py flush` removes application data, including local users, while keeping migrated tables. It is destructive and is not a routine setup step. Rebuilding db.sqlite3 requires preserving needed data and understanding migration history first. Save the actual error before choosing a recovery action; do not delete tables or migration files merely because a query is empty.

Evidence should connect class, migration, table, and record. A screenshot of a success page alone does not establish database persistence. Check the schema, save a row, inspect its values, query it, and record what happened. The slides' lab sequence covers app creation, registration, migration, administrator setup, two records, ORM queries, commits, and a separate written summary.

## Sources

- [Course slides on models and databases](https://docs.google.com/presentation/d/1TSNIUaCGMYIwGwP8LFVcAhUlt_TCLy5wG5hoOADOLVQ/edit)
- [Django models](https://docs.djangoproject.com/en/6.1/topics/db/models/)
- [Django migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/)
- [Django queries](https://docs.djangoproject.com/en/6.1/topics/db/queries/)
- [Django admin](https://docs.djangoproject.com/en/6.1/ref/contrib/admin/)

[Return to documentation home](index.md) · [Continue to model relationships](django-model-relationships.md)
