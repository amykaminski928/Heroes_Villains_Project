
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seializers import SuperSerializer
from .models import Super


# Create your views here.
@api_view (['GET'])
def supers_list (request):
    supers = Super.objects.all()
    supers_serializer = SuperSerializer(supers, many = True)
    
    heroes = supers.filter(super_types__type='hero')
    villains = supers.filter(super_types__type='villain')
    serialized_heroes = SuperSerializer(heroes, many = True)
    serialized_villains = SuperSerializer(villains, many = True)

  
       
    custom_response_dict = {
        'Heroes': [serialized_heroes.data],
        'Villians': [serialized_villains.data]
    }
        

    return Response(custom_response_dict)
   

    
    
        

        
 
