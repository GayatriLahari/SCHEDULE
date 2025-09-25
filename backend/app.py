#!/usr/bin/env python3
"""AI Scheduler App - Backend API"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging
from datetime import datetime, timezone
import json
from services.perplexity_service import PerplexityService
from services.calendar_service import GoogleCalendarService
from services.scheduler_service import SchedulerService
from models.task import Task

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize services
perplexity_service = PerplexityService()
calendar_service = GoogleCalendarService()
scheduler_service = SchedulerService(perplexity_service, calendar_service)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()})

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = scheduler_service.get_all_tasks()
        return jsonify({"tasks": [task.to_dict() for task in tasks]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            due_date=data.get('due_date'),
            duration=data.get('duration', 60),
            task_type=data.get('task_type', 'general')
        )
        scheduled_task = scheduler_service.create_and_schedule_task(task)
        return jsonify({"message": "Task created successfully", "task": scheduled_task.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
