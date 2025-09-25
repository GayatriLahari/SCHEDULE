import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any

@dataclass
class Task:
    title: str
    description: str = ""
    priority: str = "medium"
    task_type: str = "general"
    duration: int = 60
    due_date: Optional[str] = None
    scheduled_start: Optional[str] = None
    scheduled_end: Optional[str] = None
    id: Optional[str] = None
    status: str = "pending"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    calendar_event_id: Optional[str] = None
    tags: list = None
    location: str = ""
    attendees: list = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc).isoformat()
        if self.updated_at is None:
            self.updated_at = self.created_at
        if self.tags is None:
            self.tags = []
        if self.attendees is None:
            self.attendees = []

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
