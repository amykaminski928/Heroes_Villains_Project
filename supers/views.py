
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seializers import SuperSerializer
from .models import Super
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view (['GET', 'POST'])
def supers_list (request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many = True)
    heroes = supers.filter(super_types__type= 'hero')
    villains = supers.filter(super_types__type= 'villain')
    serialized_heroes = SuperSerializer(heroes, many = True)
    serialized_villains = SuperSerializer(villains, many = True)
    type_param = request.query_params.get('type')

    if type_param == True:
        supers = supers.filter(super_types__type=type_param)
        return Response(serializer.data)   

    if request.method == 'GET':  
        custom_response_dict = {
            'Heroes': [serialized_heroes.data],
            'Villians': [serialized_villains.data]
            }
        return Response(custom_response_dict, status=status.HTTP_200_OK)
        
    if request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
   

@api_view (['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = Super.objects.get(pk=pk)
    
    if request.method == 'GET':
        try:
            serializer = SuperSerializer(supers)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Super.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)