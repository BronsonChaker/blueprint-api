from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .models import Organisation
from users.models import User, Membership
from users.serializers import UserSerializer  
from users.serializers import MembershipSerializer  
from .serializers import OrganisationSerializer

@api_view(['GET'])
def user_organisation(request):
    organisations = Organisation.objects.filter(membership__user=request.user)
    serializer = OrganisationSerializer(organisations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_organisation(request):
    serializer = OrganisationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_organisation_supervisors(request):
    membership = request.user.membership_set.first()

    org = membership.organisation

    supervisors = Membership.objects.filter(
        organisation=org,
        role=Membership.Role.SUPERVISOR
    )

    serializer = MembershipSerializer(supervisors, many=True)
    return Response(serializer.data)