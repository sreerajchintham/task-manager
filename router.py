from fastapi import FastAPI
import uuid
from database import Database
app = FastAPI()

cursor = Database("tasks.db")

@app.get("/")
def health_check():
    return {"status" : "healthy"}


@ app.post("/create_task")
def create_task(task_name: str,task_description: str, task_completion_status=False):
    cursor.add_record(task_name=task_name,task_description=task_description,task_completion_status=task_completion_status)

    return

@app.get(f"/get_tasks")
def retrieve_tasks():
    print(cursor.get_table("tasks"))
    return cursor.get_table("tasks")

@app.get("/get_completed_tasks")
def retrieve_comlpleted_tasks():
    print(cursor.get_table("completed_tasks"))
    return cursor.get_table("completed_tasks")

@app.post("/modify_task")
def update_task(task_name:str):

    """
    Updates Tasks from Incomplete to Complete

    """
    record = cursor.modify_record(task_name=task_name)

    print(record)

    return record


@app.post("/delete_task")
def delete_task(task_name:str):

    """
    Delete Tasks from Table "tasks" when provided task name

    """
    deleted_task = cursor.delete_record(task_name=task_name)


    return cursor.get_table("tasks")




