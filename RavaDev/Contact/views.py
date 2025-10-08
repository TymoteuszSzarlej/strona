from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm  # Import nowego formularza
from _common.logs import AppLogger
from _common.messages import FlashMessage




def contact_success(request):
    FlashMessage.info(request, 'Przesłano wiadomość. Odezwiemy sie w ciągu kilku dni!')
    """Widok strony potwierdzenia po wysłaniu wiadomości"""
    
    return render(request, 'Contact/success.html')



def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            try:
                # Zapis wiadomości do bazy
                message = form.save()
                
                # Logowanie sukcesu
                AppLogger.info(
                    f"Nowa wiadomość od {message.sender} ({message.email})", 
                    "Contact"
                )
                
                # Wiadomość flash o sukcesie
                FlashMessage.success(request, "Wiadomość została wysłana pomyślnie!")
                
                return redirect('/contact/success/')  # Strona potwierdzenia
                
            except Exception as e:
                # Logowanie błędu przy zapisie
                AppLogger.error(
                    f"Błąd podczas zapisywania wiadomości od {form.cleaned_data.get('sender', 'Unknown')}",
                    "Contact", 
                    exc_info=e
                )
                FlashMessage.error(request, "Wystąpił błąd podczas wysyłania wiadomości. Spróbuj ponownie.")
        
        else:
            # Formularz zawiera błędy walidacji
            FlashMessage.form_errors(request, form)
            AppLogger.warning(
                f"Błąd walidacji formularza - {len(form.errors)} błędów", 
                "Contact"
            )
    
    else:
        # GET request - pusty formularz
        form = MessageForm()
    
    return render(request, 'Contact/contact.html', {'form': form})

