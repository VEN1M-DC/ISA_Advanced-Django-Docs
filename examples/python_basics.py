"""Run the examples accompanying the team's Python learning draft."""


def result_label(score):
    if score >= 70:
        return "pass"
    return "review"


class Student:
    def __init__(self, name):
        self.name = name

    def introduction(self):
        return f"Hello, I am {self.name}."


if __name__ == "__main__":
    topic = "Python"
    scores = [80, 90, 100]
    location = (2, 3)
    student = {"name": "Ada", "active": True}
    topics = {"Python", "HTML", "Python"}
    print(scores[0])
    print(student["name"])
    print(len(topics))

    for score in [80, 60]:
        print(f"{score}: {result_label(score)}")

    learner = Student("Ada")
    print(learner.introduction())
