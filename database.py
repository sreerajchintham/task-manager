import sqlite3

class Database():

    def __init__(self,database_name: str):

        self.conn = sqlite3.connect(database_name,check_same_thread=False)

        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    to_do_id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    task_description TEXT NOT NULL,
    task_completion_statu TEXT NOT NULL
)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS completed_tasks (
    to_do_id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    task_description TEXT NOT NULL,
    task_completion_statu TEXT NOT NULL
)""")

    
    def add_record(self,task_name:str,task_description:str,task_completion_status=False):

        self.cursor.execute("""INSERT INTO tasks (task_name,task_description,task_completion_status) VALUES (?,?,?)
        """, (task_name,task_description,task_completion_status))

        self.conn.commit()

        return 
    

    def get_table(self,table_name:str):

        self.cursor.execute(f"""SELECT * from {table_name}
        
        """)

        return self.cursor.fetchall()

    def modify_record(self,task_name:str):

        self.cursor.execute(f"""UPDATE tasks SET task_completion_status = ? WHERE task_name = ?""", ("True", task_name))
        self.conn.commit()



    def delete_record(self,task_name:str):

        self.cursor.execute("""DELETE FROM tasks WHERE task_name = ?""", (task_name,))
        self.conn.commit()

        return 
