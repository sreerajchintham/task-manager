import { useState } from 'react';

function TaskForm({ onTaskCreated }) {
  const [taskName, setTaskName] = useState('');
  const [description, setDescription] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!taskName.trim() || !description.trim()) {
      setError('Please fill in all fields');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      await onTaskCreated({ 
        task_name: taskName, 
        description: description 
      });
      
      setTaskName('');
      setDescription('');
    } catch (err) {
      setError('Failed to create task');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <h2>New Task</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      <div className="form-group">
        <label htmlFor="taskName">Title</label>
        <input
          type="text"
          id="taskName"
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
          placeholder="Enter task title"
          disabled={isLoading}
        />
      </div>
      
      <div className="form-group">
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Enter task description"
          rows={3}
          disabled={isLoading}
        />
      </div>
      
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Adding...' : 'Add Task'}
      </button>
    </form>
  );
}

export default TaskForm;
