from django.shortcuts import render
from .models import Service, Field
from django.shortcuts import get_object_or_404

# Create your views here.
def services(request):
    fields_list = Field.objects.all()
    service_list = Service.objects.all()
    return render(request, 'Services/services.html', {'services': service_list})

def service_detail(request, service_id):
    # Pobierz obiekt usługi zamiast tylko ID
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'Services/service_detail.html', {'service': service})