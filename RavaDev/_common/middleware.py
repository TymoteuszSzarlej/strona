# _common/middleware.py
import json
from django.utils import timezone
from django.db import models
from .utils import log
from .models import SystemLog

# _common/middleware.py
import time
from django.utils import timezone
from .utils import log

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Logowanie rozpoczęcia requestu
        start_time = time.time()
        
        # Przed przetworzeniem requestu
        try:
            log('INFO', f'Request started: {request.method} {request.path}', 
                source='middleware.request')
        except:
            pass  # Zabezpieczenie przed błędami w logowaniu
        
        response = self.get_response(request)
        
        # Po przetworzeniu requestu
        end_time = time.time()
        duration = end_time - start_time
        
        try:
            log('INFO', f'Request completed: {request.method} {request.path} '
                       f'Status: {response.status_code} Duration: {duration:.2f}s', 
                source='middleware.request')
        except:
            pass
        
        return response

    def process_exception(self, request, exception):
        # Logowanie wyjątków
        try:
            log('ERROR', f'Exception: {str(exception)}', 
                source='middleware.exception')
        except:
            pass
        return None

class LogModelSaveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Logowanie błędów
        try:
            log('ERROR', f'Exception: {str(exception)}', source='middleware.exception')
        except:
            pass  # Zapobiegaj nieskończonej pętli błędów

def log_model_save(sender, instance, created, **kwargs):
    """Signal handler for model saves with safe serialization"""
    try:
        action = 'created' if created else 'updated'
        
        # Bezpieczna serializacja metadanych
        metadata = {
            'model': sender.__name__,
            'action': action,
            'instance_id': getattr(instance, 'id', None),
            'timestamp': timezone.now().isoformat(),
        }
        
        # Dodaj tylko proste pola do metadanych
        simple_fields = {}
        for field in instance._meta.fields:
            if isinstance(field, (models.CharField, models.TextField, models.IntegerField, models.BooleanField)):
                field_value = getattr(instance, field.name, None)
                if field_value is not None and not isinstance(field_value, (models.Model, models.ModelState)):
                    simple_fields[field.name] = str(field_value)[:100]  # Ogranicz długość
        
        metadata['fields'] = simple_fields
        
        log('INFO', f'Model {sender.__name__} {action}', source='middleware.model_save', metadata=metadata)
        
    except Exception as e:
        # Bezpieczne logowanie błędów - unikaj rekurencji
        try:
            SystemLog.objects.create(
                level='ERROR',
                message=f'Error in log_model_save: {str(e)[:200]}',
                source='middleware.error',
                timestamp=timezone.now()
            )
        except:
            pass  # Ostateczne zabezpieczenie

# Alternatywnie - uproszczona wersja bez JSONField
def safe_log_model_save(sender, instance, created, **kwargs):
    """Simplified version without metadata"""
    try:
        action = 'created' if created else 'updated'
        message = f'{sender.__name__} {action} (id: {getattr(instance, "id", "new")})'
        
        SystemLog.objects.create(
            level='INFO',
            message=message,
            source='model_save',
            timestamp=timezone.now()
        )
    except Exception as e:
        # Minimalne logowanie błędu
        try:
            SystemLog.objects.create(
                level='ERROR',
                message=f'Log error: {str(e)[:100]}',
                source='log_error',
                timestamp=timezone.now()
            )
        except:
            pass