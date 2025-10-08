from django.db import models
from django.utils import timezone

# Zakładam, że About.TeamMember to model w innej aplikacji
from About.models import TeamMember



class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    email = models.EmailField()
    phoneCode = models.PositiveSmallIntegerField()
    phoneNumber = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Message from {self.sender}"
