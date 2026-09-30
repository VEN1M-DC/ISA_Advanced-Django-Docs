# Python fundamentals

Contributor: **ISA SAMIEZADE-YAZD**

Review status: AI-assisted learning draft. Run the examples, revise the explanations to reflect your understanding, and record actual team feedback before submitting.

Python is the programming language used to write Django applications. This page introduces enough Python syntax to begin reading project code, with comparisons for someone familiar with Java or C#.

## Verify Python and run a file

In Windows PowerShell:

```powershell
py --version
py examples/python_basics.py
```

On macOS or Linux:

```bash
python3 --version
python3 examples/python_basics.py
```

Run the file command from the repository directory. If you have activated a project virtual environment, use `python` to select that environment's interpreter. Python 3.14.6 was detected on the computer used to check this draft; verify your own installation instead of assuming the same version.

## Comparison cheat sheet

Python supports object-oriented programming as well as standalone functions. The comparison below uses familiar Java and C# conventions; those languages also have features beyond these introductory examples.

| Concept | Common Java or C# form | Python form |
| --- | --- | --- |
| Code block | Braces `{ ... }` | Colon followed by indented statements |
| Variable | Declared type or inferred local type | `name = "Ada"` |
| Boolean | `true`, `false` | `True`, `False` |
| Missing value | `null` | `None` |
| Logical operators | `&&`, `\|\|`, `!` | `and`, `or`, `not` |
| Comment | `// note` | `# note` |
| Function | Method declaration | `def greet(name):` |
| Instance reference | `this` | Explicit first parameter, conventionally `self` |
| New object | `new Student("Ada")` | `Student("Ada")` |
| Instance initialization | Constructor | `__init__` initializes an instance |
| Inheritance | `extends` or `:` | `class Graduate(Student):` |

Use four spaces per indentation level. Python names refer to objects; objects have types. You do not declare a fixed type for a variable name. Optional type hints document expectations but do not, by themselves, enforce types at runtime.

## Values and collections

Common types include `int` for whole numbers, `float` for floating-point numbers, `str` for text, and `bool` for truth values. A list is an ordered, mutable collection; a tuple is immutable; a dictionary maps keys to values; a set holds unique elements.

```python
topic = "Python"
scores = [80, 90, 100]
location = (2, 3)
student = {"name": "Ada", "active": True}
topics = {"Python", "HTML", "Python"}

print(scores[0])           # 80: indexing begins at zero
print(student["name"])    # Ada
print(len(topics))         # 2: duplicate elements are removed
```

## Decisions functions and loops

```python
def result_label(score):
    if score >= 70:
        return "pass"
    return "review"

for score in [80, 60]:
    print(f"{score}: {result_label(score)}")
```

Expected output:

```text
80: pass
60: review
```

`def` introduces a reusable function, `return` provides its result, and the `for` loop visits each list element. An f-string inserts expressions inside braces into text. Use `==` to compare values and `=` to assign a value.

## Classes and objects

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduction(self):
        return f"Hello, I am {self.name}."

learner = Student("Ada")
print(learner.introduction())
```

Output: `Hello, I am Ada.`

The class describes student objects. Each instance can hold its own `name`. When an instance method is called, Python supplies the instance as its first argument. Django uses Python classes in features such as models, so recognizing methods, attributes, and inheritance will help when reading framework code.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Python command is not found | Verify Python is installed and try the command for your operating system. Reopen the terminal after installation. |
| `IndentationError` | Check alignment and avoid mixing tabs with spaces. |
| `NameError` | Check spelling, capitalization, and whether the name was assigned before use. |
| `TypeError` when combining text and numbers | Use an f-string or explicitly convert the number with `str()`. |
| File cannot be opened | Confirm the terminal is in the repository directory and the filename is correct. |

Read the last line of a traceback for the exception, then inspect the referenced line in your own file. These are practice troubleshooting suggestions, not a record of problems experienced by a team member.

## Practice before submitting

1. Change the student name and explain why the output changes.
2. Add a score of 70 and predict which label the function returns.
3. Create a second student and explain how its attributes differ from the first student's.
4. Rewrite one explanation using your own words and add two improvements based on actual team feedback.

## Official resources

- [Python tutorial introduction](https://docs.python.org/3/tutorial/introduction.html) — numbers, strings, lists, and comments.
- [Python classes tutorial](https://docs.python.org/3/tutorial/classes.html) — instances, methods, and inheritance.

## AI use disclosure to personalize

AI helped draft explanations, comparisons, and practice examples. The example script was executed during preparation. Add what you personally checked, changed, and learned; do not claim a review or learning experience you have not completed.
