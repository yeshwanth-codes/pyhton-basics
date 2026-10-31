import csv

multi_task = [
    {"task": "prepare slides", "user": "ultron", "deadline": "monday"},
    {"task": "presentation", "user": "dum-e", "deadline": None},
    {"task": "debugg", "user": "", "deadline": None},
    {"task": None, "user": " ", "deadline": "weekend"},
]

def checks_task(t):
    errors = []

    if not t["task"] or not t["task"].strip():
        errors.append("needs a task")
    if not t["user"] or not t["user"].strip():
        errors.append("needs a user")
    if not t["deadline"] or not str(t["deadline"]).strip():
        errors.append("needs a deadline")

    return errors


complete = []
incomplete = []

for t in multi_task:
    errors = checks_task(t)
    if errors:
        incomplete.append({"task": t, "errors": errors})
    else:
        complete.append(t)



print("Saved", len(complete), "task(s) to tasks.csv")
print("INCOMPLETE:", incomplete)