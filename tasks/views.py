from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    tasks = Task.objects.filter(job__organisation__membership__user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

