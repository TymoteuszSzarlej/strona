import logging
import sys
from datetime import datetime
from django.conf import settings

# Konfiguracja loggera
logger = logging.getLogger('django')

class AppLogger:
    """
    Klasa do obsługi logowania zdarzeń w aplikacji Django
    """
    
    @staticmethod
    def _get_log_prefix(level):
        """Tworzy prefix dla logów z timestampem i poziomem"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{level.upper()}]"
    
    @staticmethod
    def info(message, module_name=""):
        """Loguje informacyjną wiadomość"""
        prefix = AppLogger._get_log_prefix('INFO')
        if module_name:
            message = f"{module_name}: {message}"
        
        logger.info(message)
        print(f"{prefix} {message}", file=sys.stdout)
    
    @staticmethod
    def warning(message, module_name=""):
        """Loguje ostrzeżenie"""
        prefix = AppLogger._get_log_prefix('WARNING')
        if module_name:
            message = f"{module_name}: {message}"
        
        logger.warning(message)
        print(f"{prefix} ⚠️  {message}", file=sys.stdout)
    
    @staticmethod
    def error(message, module_name="", exc_info=None):
        """Loguje błąd"""
        prefix = AppLogger._get_log_prefix('ERROR')
        if module_name:
            message = f"{module_name}: {message}"
        
        logger.error(message, exc_info=exc_info)
        print(f"{prefix} ❌ {message}", file=sys.stderr)
        
        if exc_info and settings.DEBUG:
            import traceback
            traceback.print_exc()
    
    @staticmethod
    def debug(message, module_name=""):
        """Loguje wiadomość debug (tylko gdy DEBUG=True)"""
        if not settings.DEBUG:
            return
            
        prefix = AppLogger._get_log_prefix('DEBUG')
        if module_name:
            message = f"{module_name}: {message}"
        
        logger.debug(message)
        print(f"{prefix} 🔍 {message}", file=sys.stdout)
    
    @staticmethod
    def critical(message, module_name="", exc_info=None):
        """Loguje krytyczny błąd"""
        prefix = AppLogger._get_log_prefix('CRITICAL')
        if module_name:
            message = f"{module_name}: {message}"
        
        logger.critical(message, exc_info=exc_info)
        print(f"{prefix} 💥 {message}", file=sys.stderr)
    
    @staticmethod
    def request_info(request, message=""):
        """Loguje informacje o requeście HTTP"""
        user_info = f"Użytkownik: {request.user}" if hasattr(request, 'user') else "Użytkownik: Anonimowy"
        path_info = f"Ścieżka: {request.path}"
        method_info = f"Metoda: {request.method}"
        
        full_message = f"{message} | {user_info} | {path_info} | {method_info}"
        AppLogger.info(full_message, "HTTP Request")
    
    @staticmethod
    def database_operation(model_name, operation, details=""):
        """Loguje operację na bazie danych"""
        message = f"Model: {model_name} | Operacja: {operation}"
        if details:
            message += f" | Szczegóły: {details}"
        AppLogger.info(message, "Database")
    
    @staticmethod
    def user_action(user, action, details=""):
        """Loguje akcję użytkownika"""
        user_ident = user.username if hasattr(user, 'username') else str(user)
        message = f"Użytkownik: {user_ident} | Akcja: {action}"
        if details:
            message += f" | Szczegóły: {details}"
        AppLogger.info(message, "User Action")

# Skrócone aliasy dla łatwiejszego użycia
def log_info(message, module_name=""):
    AppLogger.info(message, module_name)

def log_warning(message, module_name=""):
    AppLogger.warning(message, module_name)

def log_error(message, module_name="", exc_info=None):
    AppLogger.error(message, module_name, exc_info)

def log_debug(message, module_name=""):
    AppLogger.debug(message, module_name)

def log_critical(message, module_name="", exc_info=None):
    AppLogger.critical(message, module_name, exc_info)