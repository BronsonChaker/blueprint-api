from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vendor_list(request):
    vendors = Vendor.objects.filter(organisation__membership__user=request.user)
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)
        

    
