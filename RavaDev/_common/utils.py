from .models import SystemLog
from django.utils.timezone import now

def log(level: str, message: str, source: str = None, metadata: dict = None):
    """
    Dodaje wpis do logów systemowych.

    :param level: INFO, WARNING, ERROR, DEBUG
    :param message: Treść komunikatu
    :param source: Opcjonalnie: nazwa modułu/funkcji
    :param metadata: Opcjonalnie: dodatkowe dane (np. user_id, traceback)
    """
    level = level.upper()
    if level not in ['INFO', 'WARNING', 'ERROR', 'DEBUG']:
        level = 'INFO'

    SystemLog.objects.create(
        timestamp=now(),
        level=level,
        source=source or 'unknown',
        message=message,
        metadata=metadata or {}
    )
