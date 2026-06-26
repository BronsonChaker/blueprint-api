from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from organisations.models import Organisation
from .serializers import OrganisationSerializer


@login_required
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Organisation': '/?organisation=organisation_name',
        'Search by Subcategory': '/?Subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_organisations(request):
    organisation = OrganisationSerializer(data=request.data)

    if Organisation.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if organisation.is_valid():
        organisation.save()
        return Response(organisation.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@login_required
@api_view(['GET'])
def view_organisations(request):
    if request.query_params:
        organisations = Organisation.obejcts.filter(**request.query_params.dict())
    else:
        organisations = Organisation.objects.all()

    if organisations:
        serializer = OrganisationSerializer(organisations, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)