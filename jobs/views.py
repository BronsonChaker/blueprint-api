from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Job
from users.models import User
from .serializers import JobSerializer

@api_view(['GET'])
def job_list(request):
    if request.method == "GET":
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def user_job_list(request ,uuid):
        
    supervisor = get_object_or_404(User, id=uuid)
    jobs = Job.objects.filter(supervisor=supervisor)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


