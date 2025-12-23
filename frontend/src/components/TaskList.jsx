import TaskItem from './TaskItem';

function TaskList({ title, tasks, onComplete, onDelete, showCompleteButton = true }) {
  if (tasks.length === 0) {
    return (
      <div className="task-list empty">
        <p className="empty-message">No tasks yet</p>
      </div>
    );
  }

  return (
    <div className="task-list">
      <h2>{title}</h2>
      <div className="tasks-container">
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            onComplete={onComplete}
            onDelete={onDelete}
            showCompleteButton={showCompleteButton}
          />
        ))}
      </div>
    </div>
  );
}

export default TaskList;
