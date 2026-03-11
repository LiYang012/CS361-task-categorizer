# CS361-task-categorizer

## Overview

The **Task Categorizer Microservice** analyzes a task and automatically assigns two labels:

1. **Task Category**

   * **Work** – tasks related to professional activities
   * **Personal** – tasks related to personal life

2. **Time Classification**

   * **Rigid** – tasks with a fixed start time and deadline
   * **Flexible** – tasks with only a deadline or no fixed start time

The service uses **keyword matching** and **task time fields** to determine the correct labels.

Example:

| Task                      | Result             |
| ------------------------- | ------------------ |
| "Client meeting tomorrow" | Work, Rigid        |
| "Buy groceries tonight"   | Personal, Flexible |

---

# How to Request Data from This Microservice

The microservice exposes a **GET HTTP API endpoint**.

### Endpoint

```
GET /categorize
```

### Query Parameters

| Parameter   | Required | Description            |
| ----------- | -------- | ---------------------- |
| title       | optional | Task title             |
| description | optional | Task description       |
| start_time  | optional | Start time of the task |
| deadline    | optional | Deadline of the task   |

### Example Request

```
http://localhost:8000/categorize?title=Client%20meeting&start_time=2026-04-10T09:00&deadline=2026-04-10T10:00
```

Another example:

```
http://localhost:8000/categorize?title=Buy%20groceries&deadline=2026-04-10
```

---

# How You Will Receive Data

The microservice returns a **JSON response** containing the classification results.

### Example Response

```json
{
  "task_type": "Work",
  "time_type": "Rigid"
}
```

### Response Fields

| Field     | Description                      |
| --------- | -------------------------------- |
| task_type | Either **Work** or **Personal**  |
| time_type | Either **Rigid** or **Flexible** |

Example response for a personal task:

```json
{
  "task_type": "Personal",
  "time_type": "Flexible"
}
```