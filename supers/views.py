
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seializers import SuperSerializer
from .models import Super
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view (['GET'])
def supers_list (request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many = True)
    heroes = supers.filter(super_types__type='1')
    villains = supers.filter(super_types__type='2')
    serialized_heroes = SuperSerializer(heroes, many = True)
    serialized_villains = SuperSerializer(villains, many = True)
           
    custom_response_dict = {
        'Heroes': [serialized_heroes.data],
        'Villians': [serialized_villains.data]
    }
    return Response(custom_response_dict)
   
@api_view (['GET', 'PUT'])
def supers_detail(request, pk):
    supers = Super.objects.get(pk=pk)
    
    if request.method == 'GET':
        try:
            serializer = SuperSerializer(super, many=True)
            return Response(serializer.data)
        except Super.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)