from django.contrib import messages

class FlashMessage:
    """
    Klasa do obsługi wiadomości flash w Django
    """
    
    @staticmethod
    def success(request, message):
        """Dodaje wiadomość sukcesu"""
        messages.success(request, message)
    
    @staticmethod
    def error(request, message):
        """Dodaje wiadomość błędu"""
        messages.error(request, message)
    
    @staticmethod
    def warning(request, message):
        """Dodaje wiadomość ostrzeżenia"""
        messages.warning(request, message)
    
    @staticmethod
    def info(request, message):
        """Dodaje wiadomość informacyjną"""
        messages.info(request, message)
    
    @staticmethod
    def debug(request, message):
        """Dodaje wiadomość debug (tylko gdy DEBUG=True)"""
        messages.debug(request, message)
    
    @classmethod
    def form_errors(cls, request, form):
        """Wyświetla błędy formularza jako wiadomości flash"""
        for field, errors in form.errors.items():
            for error in errors:
                cls.error(request, f"{form.fields[field].label if field in form.fields else field}: {error}")
    
    @classmethod
    def object_created(cls, request, object_name):
        """Standardowa wiadomość po utworzeniu obiektu"""
        cls.success(request, f"{object_name} został pomyślnie utworzony.")
    
    @classmethod
    def object_updated(cls, request, object_name):
        """Standardowa wiadomość po aktualizacji obiektu"""
        cls.success(request, f"{object_name} został pomyślnie zaktualizowany.")
    
    @classmethod
    def object_deleted(cls, request, object_name):
        """Standardowa wiadomość po usunięciu obiektu"""
        cls.success(request, f"{object_name} został pomyślnie usunięty.")
    
    @classmethod
    def permission_denied(cls, request):
        """Wiadomość o braku uprawnień"""
        cls.error(request, "Nie masz uprawnień do wykonania tej operacji.")

# Skrócone aliasy dla łatwiejszego użycia
def flash_success(request, message):
    FlashMessage.success(request, message)

def flash_error(request, message):
    FlashMessage.error(request, message)

def flash_warning(request, message):
    FlashMessage.warning(request, message)

def flash_info(request, message):
    FlashMessage.info(request, message)

def flash_form_errors(request, form):
    FlashMessage.form_errors(request, form)