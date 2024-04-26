from django.utils import timezone
from django.db import models
from user.models import User

# Create your models here.
class Actor(models.Model):
    type = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Document(models.Model):
    type = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class AccessLog(models.Model): 
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   

class AccessPermission(models.Model):
    PERMISSION_CHOICES = [
        ('read', 'Read'),
        ('write', 'Write'),
        ('noPermission' , 'NoPermission')
        # Add more permissions if needed...
    ]
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    permission = models.CharField(max_length=12, choices=PERMISSION_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('actor', 'document', 'permission')
        