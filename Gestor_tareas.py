import sqlite3

class TaskManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            description TEXT
        )
        ''')
        self.conn.commit()

    def add_task(self, description):
        self.c.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
        self.conn.commit()

    def view_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        tasks = self.c.fetchall()
        for task in tasks:
            print(f'Task ID: {task[0]}, Description: {task[1]}')

    def delete_task(self, task_id):
        self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db_name = "tasks.db"
    task_manager = TaskManager(db_name)

    while True:
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Delete Task')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            description = input('Enter task description: ')
            task_manager.add_task(description)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_id = input('Enter task ID to delete: ')
            task_manager.delete_task(task_id)
        elif choice == '4':
            task_manager.close()
            break
        else:
            print('Invalid choice')
