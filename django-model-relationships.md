---
title: Django Model Relationships and Branch Workflow
---

# Django Model Relationships and Branch Workflow

Contributor: **ISA SAMIEZADE-YAZD**. Updated October 7, 2026. Study guide based on the linked relationship slides with AI assistance. Portfolio and Project code below is a proposed exercise, not a statement that those models have been added to the application.

## Choose relationships from requirements

| Requirement | Relationship | Django field |
| --- | --- | --- |
| A Student can have one Portfolio; each Portfolio has one Student | One-to-one | OneToOneField |
| A Portfolio can have multiple Projects; each Project belongs to one Portfolio | One-to-many | ForeignKey on Project |
| Projects can use multiple Skills and Skills can appear on multiple Projects | Many-to-many | ManyToManyField; identify only at this stage |

A required OneToOneField means every saved Portfolio references a Student. It does not force every Student to already have a Portfolio. Decide optionality and deletion behavior explicitly.

## Branch workflow

Start with a clean, working main and commit existing work first. The lecture names the development branch model_setup; these are commands to run for that exercise:

```powershell
git status
git switch main
git pull --ff-only
git switch -c model_setup
# Implement a small model change, migrate, and verify it.
git diff
git add portfolio_app/models.py portfolio_app/admin.py portfolio_app/migrations/
git commit -m "Add portfolio relationship"
git push -u origin model_setup
```

Use git branch and git log to inspect progress. Commit after meaningful tested increments. Integrate the completed sprint into main after review and relationship checks. The local database is ignored and not switched with the branch; applying schema changes affects that same local file. No application branch was created by publishing this study guide.

## Keys and the Portfolio model

A primary key identifies its own row. A foreign key identifies a related row in another table. Portfolio.id identifies the Portfolio; Portfolio.student_id references Student.id. The two keys can coincidentally have the same numeric value without meaning the same thing.

The lecture provides these Portfolio fields:

```python
class Portfolio(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title
```

Expected table: portfolio_app_portfolio. Expected columns: id, student_id, title, contact_email, is_active, about. Python exposes student as an object relationship; SQLite stores the related key as student_id. The one-to-one field has uniqueness enforcement on that reference.

For the one-to-many requirement, this is an illustrative extension. The Project field details should be checked against the assignment's full UML design:

```python
class Project(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
```

Expected relation: Project.portfolio_id references Portfolio.id. Several Project rows can use the same portfolio_id. This proposed related_name makes portfolio.projects available for reverse queries; it is a design choice added in the example, not a field specified by the slides.

## Migration and admin inspection

After editing models, run check, makemigrations portfolio_app, and migrate. Inspect the generated migration and tables. Register new models without registering Student twice:

```python
from django.contrib import admin
from .models import Student, Portfolio, Project
admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)
```

Prediction questions: Which table and columns should appear? Which key identifies the row? Which column connects it to its owner? Compare predictions with the migration and SQLite table. Keep the database and admin password out of Git.

## Test cardinality and deletion

Use disposable fictional examples in a test database. Create a Student and its Portfolio. Attempting a second Portfolio for that Student should fail validation or the database uniqueness constraint. Create two Projects attached to one Portfolio and confirm both are retrieved. Capture actual outcomes rather than treating predicted results as observed facts.

CASCADE means deleting the referenced Student causes Django to delete its related Portfolio. With the illustrative Project cascade, Django also deletes that Portfolio's Projects. Deleting a Portfolio does not delete the Student it referenced. Deleting a Project does not delete its Portfolio. Test deletion using temporary fixtures so the two existing Student examples remain intact.

Remove bad example records through admin or the ORM rather than deleting schema tables. flush clears data, including the superuser, and deserves a deliberate decision. Diagnose schema problems before deleting databases or migrations.

## Navigate and query relationships

These shell exercises require Portfolio to exist and contain data:

```python
from portfolio_app.models import Student, Portfolio
Student.objects.all()
Portfolio.objects.all()
portfolio = Portfolio.objects.first()
if portfolio is not None:
    print(portfolio.title)
    print(portfolio.student)
    print(portfolio.student.name)
    print(portfolio.student.major)

student = Student.objects.first()
if student is not None:
    try:
        print(student.portfolio.title)
    except Portfolio.DoesNotExist:
        print("This Student does not have a Portfolio yet.")

portfolios = Portfolio.objects.filter(student__major="CSCI-BS")
print(portfolios.query)
list(portfolios)
```

The default reverse one-to-one accessor is student.portfolio. A missing related object raises a related-object exception. Double underscores traverse relationships in filter conditions. SQLite receives SQL, often involving joins, while the programmer writes Python queries. Printing query shows its representation; list evaluates it.

With the illustrative Project model, portfolio.projects.all() returns its children. select_related("student") can fetch a Portfolio and its Student together; prefetch_related("projects") can fetch collections efficiently. Measure query behavior before optimizing.

## Completion evidence

Record the model code, generated migration, applied status, table columns, related rows, duplicate-one-to-one outcome, deletion outcome in a test database, and relationship query results. Explain what you wrote versus what Django generated. The next sprint can then add views and templates to display the stored portfolio.

## Sources

- [Course slides on models and database relationships](https://drive.google.com/file/d/1-z7prhD6YUYHVfgSpXmmRQPbL1erRifo/view)
- [Django relationship fields](https://docs.djangoproject.com/en/6.1/topics/db/models/#relationships)
- [Django one-to-one examples](https://docs.djangoproject.com/en/6.1/topics/db/examples/one_to_one/)
- [Django many-to-one examples](https://docs.djangoproject.com/en/6.1/topics/db/examples/many_to_one/)
- [Django queries](https://docs.djangoproject.com/en/6.1/topics/db/queries/)

[Return to documentation home](index.md) · [Review models and databases](django-models-databases.md)
