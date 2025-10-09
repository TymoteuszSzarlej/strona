import os
from django.conf import settings
from django.shortcuts import render
from Blog.models import Category
from Services.models import Service, Field
from Projects.models import Project
from Contact.forms import MessageForm

# Create your views here.
def index(request):
    form = MessageForm()
    media_root = os.path.join(settings.BASE_DIR, '_media')
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    image_paths = []
    categories = Category.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    fields = Field.objects.all()
    for root, dirs, files in os.walk(media_root):
        for file in files:
            if file.lower().endswith(image_extensions):
                rel_dir = os.path.relpath(root, media_root)
                rel_file = os.path.join(rel_dir, file) if rel_dir != '.' else file
                image_paths.append(rel_file.replace('\\', '/'))
    print(image_paths)  # Debug: print the list of image paths
    return render(request, 'Main/index.html.jinja', {
        'cta_images': image_paths,
        'categories': categories,
        'services': services,
        'fields': fields,
        'projects': projects,
        'form': form

    })