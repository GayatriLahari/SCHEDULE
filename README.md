# AI Scheduler App

A full-stack AI-powered task scheduler with Google Calendar integration.

## Features

- ✅ AI-powered task scheduling using Perplexity API
- ✅ Google Calendar integration (service account - no OAuth required)
- ✅ React + TypeScript frontend
- ✅ Python Flask backend
- ✅ Task management with priorities and due dates
- ✅ Schedule optimization
- ✅ Dark theme UI

## Setup Instructions

### 1. Clone and Setup

```bash
# Extract the ZIP file and navigate to the project
cd ai-scheduler-app
chmod +x setup.sh
./setup.sh
```

### 2. Configure API Keys

Edit `backend/.env` file:

```env
PERPLEXITY_API_KEY=pplx-your-actual-api-key-here
GOOGLE_CREDENTIALS_FILE=credentials.json
SECRET_KEY=your-secret-key-here
```

### 3. Google Calendar Setup (Optional)

For Google Calendar integration:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Calendar API
4. Create a Service Account
5. Download JSON credentials as `backend/credentials.json`
6. Share your calendar with the service account email

### 4. Run the Application

**Backend:**
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python app.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```

The app will be available at http://localhost:3000

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

## Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- The `.gitignore` file protects secrets
- Service account credentials are not exposed to frontend

## Demo Application

A fully functional demo is available that shows the complete UI and functionality without requiring backend setup.
