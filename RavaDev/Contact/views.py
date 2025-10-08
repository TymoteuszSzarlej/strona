from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm  # Import nowego formularza
from _common.logs import AppLogger
from _common.messages import FlashMessage
from Services.models import Service




def contact_success(request):
    FlashMessage.info(request, 'Przesłano wiadomość. Odezwiemy sie w ciągu kilku dni!')
    """Widok strony potwierdzenia po wysłaniu wiadomości"""
    
    return render(request, 'Contact/success.html')



def contact(request, service_id=None):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if service_id:
            try:
                service = Service.objects.get(id=service_id)
                form.instance.service = service
            except Service.DoesNotExist:
                AppLogger.warning(
                    f"Nie znaleziono usługi o ID {service_id} podczas próby powiązania z wiadomością",
                    "Contact"
                )

        if form.is_valid():
            try:
                message = form.save()
                AppLogger.info(
                    f"Nowa wiadomość od {message.sender} ({message.email})", 
                    "Contact"
                )
                FlashMessage.success(request, "Wiadomość została wysłana pomyślnie!")
                return redirect('Contact:contact_success')
            except Exception as e:
                AppLogger.error(
                    f"Błąd podczas zapisywania wiadomości od {form.cleaned_data.get('sender', 'Unknown')}",
                    "Contact", 
                    exc_info=e
                )
                FlashMessage.error(request, "Wystąpił błąd podczas wysyłania wiadomości. Spróbuj ponownie.")
        else:
            FlashMessage.form_errors(request, form)
            AppLogger.warning(
                f"Błąd walidacji formularza - {len(form.errors)} błędów", 
                "Contact"
            )
    else:
        form = MessageForm()
    
    return render(request, 'Contact/contact.html', {'form': form})
