# AI Scheduler App

A full-stack AI-powered task scheduler with Google Calendar integration.

## Features

- AI-powered task scheduling using Perplexity API
-  Google Calendar integration (service account - no OAuth required)
-  React + TypeScript frontend
-  Python Flask backend
-  Task management with priorities and due dates
-  Schedule optimization
-  Dark theme UI

## Setup Instructions

### 1. Configure API Keys

Edit `backend/.env` file:

```env
PERPLEXITY_API_KEY=pplx-actual-api-key-here
GOOGLE_CREDENTIALS_FILE=credentials.json
SECRET_KEY=your-secret-key-here
```

### 3. Running the Application

**Backend:**
```bash
cd backend
source venv/bin/activate 
python app.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```
## API Endpoints

- `GET /api/health` - Health check
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
- `POST /api/schedule/optimize` - Optimize schedule

## Technology Stack

**Backend:**
- Python 3.8+
- Flask
- Google Calendar API
- Perplexity AI API

**Frontend:**
- React 18
- TypeScript
- Vite
- Axios

