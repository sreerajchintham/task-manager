# Task Manager

A full-stack task management application with a FastAPI backend and React frontend.

## 🚀 Live Demo

- **Frontend:** [Coming soon - Vercel]
- **Backend API:** [Your Render URL]/docs

## ✨ Features

- Create, read, update, and delete tasks
- Mark tasks as complete
- View pending and completed tasks separately
- Clean, modern React UI

## 🛠️ Tech Stack

### Backend
- **Framework:** FastAPI
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **ORM:** SQLAlchemy 2.0
- **Validation:** Pydantic 2.0
- **Language:** Python 3.12

### Frontend
- **Framework:** React 18
- **Build Tool:** Vite
- **HTTP Client:** Axios
- **Styling:** CSS

## 📁 Project Structure

```
task-manager/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Application entry point
│   │   ├── config.py       # Settings management
│   │   ├── database.py     # Database connection
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── routers/        # API routes
│   ├── requirements.txt
│   ├── Procfile            # Render deployment
│   └── runtime.txt
│
├── frontend/               # React frontend
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── ...
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

## 🏃 Getting Started

### Prerequisites

- Python 3.12+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env  # Edit with your settings

# Run the server
uvicorn app.main:app --reload
```

Backend runs at http://localhost:8000

API docs at http://localhost:8000/docs

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend runs at http://localhost:5173

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks` | Get pending tasks |
| `GET` | `/tasks/completed` | Get completed tasks |
| `GET` | `/tasks/{id}` | Get a specific task |
| `PUT` | `/tasks/{id}` | Update a task |
| `PATCH` | `/tasks/{id}/complete` | Mark task complete |
| `DELETE` | `/tasks/{id}` | Delete a task |

## 🚀 Deployment

### Backend (Render)

1. Connect your GitHub repo to Render
2. Set root directory to `backend`
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (DATABASE_URL, etc.)

### Frontend (Vercel)

1. Connect your GitHub repo to Vercel
2. Set root directory to `frontend`
3. Vite is auto-detected
4. Add environment variable: `VITE_API_URL=your-render-url`

## 📝 License

MIT

## 👤 Author

Sreeraj Chintham
