from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Job
from users.models import User
from .serializers import JobSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_list(request):
    if request.method == "GET":
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_job_list(request):   
    jobs = Job.objects.filter(supervisor=request.user)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)



