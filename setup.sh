#!/bin/bash

echo "Setting up AI Scheduler Application..."

# Backend setup
echo "Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
echo "Backend dependencies installed!"

# Create .env file
cp .env.example .env
echo "Please edit .env file with your actual API keys!"

# Frontend setup  
echo "Setting up frontend..."
cd ../frontend
npm install
echo "Frontend dependencies installed!"

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit backend/.env file with your API keys"
echo "2. Add Google Calendar service account credentials as backend/credentials.json"
echo "3. Run backend: cd backend && python app.py"
echo "4. Run frontend: cd frontend && npm run dev"
