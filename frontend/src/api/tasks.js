// src/api/tasks.js

// API base URL - uses proxy in dev, env variable in prod
const API_URL = import.meta.env.VITE_API_URL || '/api';

// Get all pending tasks
export async function getPendingTasks() {
  const response = await fetch(`${API_URL}/tasks`);
  if (!response.ok) throw new Error('Failed to fetch tasks');
  return response.json();
}

// Get all completed tasks
export async function getCompletedTasks() {
  const response = await fetch(`${API_URL}/tasks/completed`);
  if (!response.ok) throw new Error('Failed to fetch completed tasks');
  return response.json();
}

// Create a new task
export async function createTask(taskData) {
  const response = await fetch(`${API_URL}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(taskData),
  });
  if (!response.ok) throw new Error('Failed to create task');
  return response.json();
}

// Mark task as complete
export async function completeTask(taskId) {
  const response = await fetch(`${API_URL}/tasks/${taskId}/complete`, {
    method: 'PATCH',
  });
  if (!response.ok) throw new Error('Failed to complete task');
  return response.json();
}

// Delete a task
export async function deleteTask(taskId) {
  const response = await fetch(`${API_URL}/tasks/${taskId}`, {
    method: 'DELETE',
  });
  if (!response.ok) throw new Error('Failed to delete task');
  return true;
}

// Update a task
export async function updateTask(taskId, taskData) {
  const response = await fetch(`${API_URL}/tasks/${taskId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(taskData),
  });
  if (!response.ok) throw new Error('Failed to update task');
  return response.json();
}