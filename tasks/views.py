from django.shortcuts import render

from rest_framework import viewsets,status
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('-id')
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        response = {}
        records = self.get_queryset()
        ser = self.get_serializer(records,many=True,context={'request':request})
        response['result'],response['message'],response['records'],status_code = 'success','Task details fetched successfully',ser.data,status.HTTP_200_OK
        return Response(response,status=status_code)
    
    def create(self, request, *args, **kwargs):
        response,status_code = {},status.HTTP_200_OK
        try:
            serializer = self.get_serializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save() 
                response['result'],response['message'],status_code = 'success','Task created successfully.',status.HTTP_201_CREATED      
            else:
                response['result'],response['errors'],status_code = 'failure', {key:serializer.errors[key][0] for key in serializer.errors.keys()}, status.HTTP_400_BAD_REQUEST
        except Exception as error:
            response['result'],response['message'],status_code = 'failure','Something went wrong',status.HTTP_400_BAD_REQUEST
        return Response(response,status=status_code)