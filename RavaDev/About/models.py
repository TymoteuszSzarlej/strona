from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name