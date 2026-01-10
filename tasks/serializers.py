from rest_framework import serializers

from tasks.models import Task,Status
from tasks.constants import STATUS_CHOICES,STATUS_PENDING

def field_length(fieldname):
    field = next(field for field in Task._meta.fields if field.name == fieldname)
    return field.max_length

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'status')
        read_only_fields = ('id',)

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