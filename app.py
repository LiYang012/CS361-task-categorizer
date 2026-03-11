from fastapi import FastAPI

app = FastAPI()

work_keywords = ["meeting", "report", "client", "sprint"]
personal_keywords = ["gym", "grocery", "family", "doctor"]

def classify_task(title, description):
    text = f"{title} {description}".lower()

    for word in work_keywords:
        if word in text:
            return "Work"

    for word in personal_keywords:
        if word in text:
            return "Personal"

    return "Personal"

def classify_time(start_time, deadline):
    if start_time and deadline:
        return "Rigid"
    elif deadline:
        return "Flexible"
    return "Flexible"


@app.get("/categorize")
def categorize(title: str = "", description: str = "",
               start_time: str = None, deadline: str = None):

    task_type = classify_task(title, description)
    time_type = classify_time(start_time, deadline)

    return {
        "task_type": task_type,
        "time_type": time_type
    }
