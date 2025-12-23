function TaskItem({ task, onComplete, onDelete, showCompleteButton = true }) {
  const formattedDate = new Date(task.created_at).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  });

  return (
    <div className={`task-item ${task.completed ? 'completed' : ''}`}>
      <div className="task-content">
        <h3>{task.task_name}</h3>
        <p>{task.description}</p>
        <span className="task-date">{formattedDate}</span>
      </div>
      
      <div className="task-actions">
        {showCompleteButton && !task.completed && (
          <button 
            className="btn-complete"
            onClick={() => onComplete(task.id)}
          >
            Complete
          </button>
        )}
        <button 
          className="btn-delete"
          onClick={() => onDelete(task.id)}
        >
          Delete
        </button>
      </div>
    </div>
  );
}

export default TaskItem;
