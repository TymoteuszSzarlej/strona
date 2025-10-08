from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='Projects/')
    image2 = models.ImageField(upload_to='Projects/')
    image3 = models.ImageField(upload_to='Projects/')
    service = models.OneToOneField('Services.Service', on_delete=models.CASCADE)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title