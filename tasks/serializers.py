from rest_framework import serializers

from tasks.models import Task
from tasks.constants import STATUS_CHOICES,STATUS_PENDING

def field_length(fieldname):
    field = next(field for field in Task._meta.fields if field.name == fieldname)
    return field.max_length

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=field_length("title"), 
        required=True,
        error_messages={
            'required': 'Please enter the task title.',
        }
    )

    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')