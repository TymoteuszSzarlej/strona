# _common/models.py
from django.db import models
from django.utils import timezone

class SystemLog(models.Model):
    LEVEL_CHOICES = [
        ('DEBUG', 'Debug'),
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
        ('CRITICAL', 'Critical'),
    ]
    
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    message = models.TextField()
    source = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    # Usuń lub zmień metadata field na TextField
    metadata_text = models.TextField(blank=True, null=True)
    
    def set_metadata(self, data):
        """Safe metadata serialization"""
        try:
            import json
            self.metadata_text = json.dumps(data, default=str)
        except:
            self.metadata_text = str(data)
    
    def get_metadata(self):
        """Safe metadata deserialization"""
        try:
            import json
            return json.loads(self.metadata_text) if self.metadata_text else {}
        except:
            return {'raw': self.metadata_text}
    
    def __str__(self):
        return f"{self.timestamp} [{self.level}] {self.source}: {self.message[:50]}"

class EmailQueue(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Oczekuje'),
        ('SENT', 'Wysłano'),
        ('FAILED', 'Błąd'),
    ]

    to = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    error_message = models.TextField(blank=True, null=True)
    retries = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.subject} → {self.to} ({self.status})"

class EmailTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject_template = models.TextField()
    body_template = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
