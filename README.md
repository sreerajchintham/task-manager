# Task Manager API

A RESTful API for managing tasks, built with FastAPI and SQLite.

## Features

- Create, read, update, and delete tasks
- Mark tasks as complete
- Filter tasks by completion status

## Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite
- **Language:** Python 3.12

## Installation

1. Clone the repository
git clone https://github.com/sreerajchintham/task-manager.git
cd task-manager
2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.tx
4. Run the server
uvicorn app.main:app --reload## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks | Create a task |
| GET | /tasks | Get pending tasks |
| GET | /tasks/completed | Get completed tasks |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |
| PATCH | /tasks/{id}/complete | Mark as complete |

## License

MIT