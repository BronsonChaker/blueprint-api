from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.filter(job__organisation__membership__user=request.user).order_by('booking_date')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_critical_tasks(request):
    tasks = Task.objects.filter(job__organisation__membership__user=request.user, is_critical=True).order_by('booking_date')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_milestone_tasks(request):
    tasks = Task.objects.filter(job__organisation__membership__user=request.user, is_milestone=True).order_by('booking_date')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

