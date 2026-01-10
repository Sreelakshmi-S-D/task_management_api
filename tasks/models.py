from django.db import models
from .constants import STATUS_CHOICES,STATUS_PENDING

# Create your models here.

class Status(models.Model):
    status = models.CharField(
        'Status',
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
class Task(models.Model):
    title = models.CharField('Title',max_length=255)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1,
        related_name='tasks'
    )
    created_at = models.DateTimeField('Created At',auto_now_add=True)
    updated_at = models.DateTimeField('Updated At',auto_now=True)

    def __str__(self):
        return self.title
    

