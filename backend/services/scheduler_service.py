import uuid
import logging
from datetime import datetime, timezone
from models.task import Task

logger = logging.getLogger(__name__)

class SchedulerService:
    def __init__(self, perplexity_service, calendar_service):
        self.perplexity_service = perplexity_service
        self.calendar_service = calendar_service
        self.tasks_storage = {}

    def create_and_schedule_task(self, task):
        try:
            if not task.id:
                task.id = str(uuid.uuid4())

            # Use AI to schedule
            task_details = task.to_dict()
            schedule_suggestion = self.perplexity_service.generate_task_schedule(task_details)

            if schedule_suggestion and 'suggested_times' in schedule_suggestion:
                optimal_slot = schedule_suggestion['suggested_times'][0]
                task.scheduled_start = optimal_slot['start_time']
                task.scheduled_end = optimal_slot['end_time']
                task.status = 'scheduled'

                # Create calendar event
                if self.calendar_service.is_available():
                    event_data = {
                        'title': f"[AI Scheduled] {task.title}",
                        'description': task.description,
                        'start_time': task.scheduled_start,
                        'end_time': task.scheduled_end
                    }
                    created_event = self.calendar_service.create_event(event_data)
                    if created_event:
                        task.calendar_event_id = created_event['id']

            self.tasks_storage[task.id] = task
            return task
        except Exception as e:
            logger.error(f"Error scheduling task: {str(e)}")
            task.status = 'failed'
            return task

    def get_all_tasks(self):
        return list(self.tasks_storage.values())
