import { useState, useEffect } from 'react';
import Header from './components/Header';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import { 
  getPendingTasks, 
  getCompletedTasks, 
  createTask, 
  completeTask, 
  deleteTask 
} from './api/tasks';
import './App.css';

function App() {
  const [pendingTasks, setPendingTasks] = useState([]);
  const [completedTasks, setCompletedTasks] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('pending');

  useEffect(() => {
    fetchAllTasks();
  }, []);

  const fetchAllTasks = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const [pending, completed] = await Promise.all([
        getPendingTasks(),
        getCompletedTasks(),
      ]);
      setPendingTasks(pending);
      setCompletedTasks(completed);
    } catch (err) {
      setError('Unable to connect to server');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreateTask = async (taskData) => {
    const newTask = await createTask(taskData);
    setPendingTasks([newTask, ...pendingTasks]);
  };

  const handleCompleteTask = async (taskId) => {
    const completedTask = await completeTask(taskId);
    setPendingTasks(pendingTasks.filter((t) => t.id !== taskId));
    setCompletedTasks([completedTask, ...completedTasks]);
  };

  const handleDeleteTask = async (taskId) => {
    await deleteTask(taskId);
    setPendingTasks(pendingTasks.filter((t) => t.id !== taskId));
    setCompletedTasks(completedTasks.filter((t) => t.id !== taskId));
  };

  return (
    <div className="app">
      <Header />
      
      <main className="main-content">
        <TaskForm onTaskCreated={handleCreateTask} />
        
        {error && <div className="error-banner">{error}</div>}
        
        {isLoading ? (
          <div className="loading">Loading...</div>
        ) : (
          <>
            <div className="tabs">
              <button
                className={`tab ${activeTab === 'pending' ? 'active' : ''}`}
                onClick={() => setActiveTab('pending')}
              >
                Pending ({pendingTasks.length})
              </button>
              <button
                className={`tab ${activeTab === 'completed' ? 'active' : ''}`}
                onClick={() => setActiveTab('completed')}
              >
                Completed ({completedTasks.length})
              </button>
            </div>

            {activeTab === 'pending' && (
              <TaskList
                title="Pending"
                tasks={pendingTasks}
                onComplete={handleCompleteTask}
                onDelete={handleDeleteTask}
              />
            )}
            
            {activeTab === 'completed' && (
              <TaskList
                title="Completed"
                tasks={completedTasks}
                onComplete={handleCompleteTask}
                onDelete={handleDeleteTask}
                showCompleteButton={false}
              />
            )}
          </>
        )}
      </main>
    </div>
  );
}

export default App;
