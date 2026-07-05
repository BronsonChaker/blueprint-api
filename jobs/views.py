from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from users.models import User
from tasks.serializers import TaskSerializer
from tasks.models import Task
from .serializers import JobSerializer


@api_view(['GET'])
def job_list(request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
        

@api_view(['GET'])
def user_job_list(request):   
    jobs = Job.objects.filter(supervisor=request.user)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filter_tasks_completed(request, pk):
    completed_tasks = Task.objects.filter(
        job__pk = pk,
        job__organisation__membership__user=request.user,
        status ='completed'
    )
    serializer = TaskSerializer(completed_tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_tasks_not_completed(request, pk):
    completed_tasks = Task.objects.filter(
        job__pk = pk,
        job__organisation__membership__user=request.user,
        status ='not complete'
    )
    serializer = TaskSerializer(completed_tasks, many=True)
    return Response(serializer.data)



