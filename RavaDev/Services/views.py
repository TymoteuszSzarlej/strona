from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'Services/services.html')

def service_detail(request, service_id):
    return render(request, 'Services/service_detail.html', {'service_id': service_id})