from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')
    email = models.EmailField(default='kontakt.ravadev@gmail.com')
    phone = models.CharField(max_length=20, default='+48 000 000 000')

    def __str__(self):
        return self.name
    

class Info(models.Model):
    title = models.TextField(max_length=200, verbose_name="Tytuł")
    content = models.CharField(verbose_name="Treść", max_length=10240)
    def __str__(self):
        return f"{self.id}. {self.title}"
    
    class Meta:
        verbose_name = "Informacja"
        verbose_name_plural = "Informacje"
        ordering = ['id']
