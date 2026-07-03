from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .models import Organisation
from .serializers import OrganisationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_organisation(request):
    organisations = Organisation.objects.filter(membership__user=request.user)
    serializer = OrganisationSerializer(organisations, many=True)
    return Response(serializer.data)