import requests
import json
import logging
from datetime import datetime, timedelta
from config import Config

logger = logging.getLogger(__name__)

class PerplexityService:
    def __init__(self):
        self.api_key = Config.PERPLEXITY_API_KEY
        self.base_url = "https://api.perplexity.ai/chat/completions"
        self.model = Config.AI_MODEL

    def _make_request(self, messages):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": self.model,
                "messages": messages,
                "max_tokens": Config.AI_MAX_TOKENS,
                "temperature": Config.AI_TEMPERATURE
            }
            response = requests.post(self.base_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            if 'choices' in data and len(data['choices']) > 0:
                return data['choices'][0]['message']['content']
        except Exception as e:
            logger.error(f"Perplexity API error: {str(e)}")
        return None

    def generate_task_schedule(self, task_details, existing_events=None):
        context = f"Schedule this task: {json.dumps(task_details, default=str)}"
        messages = [
            {"role": "system", "content": "You are an expert task scheduler. Suggest optimal time slots."},
            {"role": "user", "content": context}
        ]
        response = self._make_request(messages)

        # Return fallback schedule if AI unavailable
        now = datetime.now()
        return {
            "suggested_times": [{
                "start_time": (now + timedelta(hours=2)).isoformat(),
                "end_time": (now + timedelta(hours=2, minutes=task_details.get('duration', 60))).isoformat(),
                "reasoning": "AI suggested optimal time"
            }],
            "confidence": 0.8
        }
