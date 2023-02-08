
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seializers import SuperSerializer
from super_types.serializers import SuperTypesSerializer
from .models import Super
from super_types.models import SuperTypes

# Create your views here.
@api_view (['GET'])
def supers_list (request):
    supers = Super.objects.all()
    super_types = SuperTypes.objects.all()
    supers_serializer = SuperSerializer(supers, many = True)
    super_types_serializer = SuperTypesSerializer(super_types, type={'hero', 'villain'})
#Tried to create parameters to accept requets thinking that I could create 
# an if True then this and if False then this loop so that if someone was trying to sort
# by type it would still work.  This is still what I think I should be doing, however,
# I can't seem to find a way to select the right object from my data set.  
#  question about the access to the data set: 
#   if I have the foreign key in supers model why do I need to import the super_types model and serializer?
# 
#So I tried this a few different ways...tried to sort in the variables above by making a variable heroes and variable villains equal to the 
#supers.super_type(1 )  then another for the villains.  THEN use that variable in the custom response dictionary below.  
#
#I tried what you see below just trying to point the response to the object...that isn't going to work, I just was running out of ideas.
#I read as much as I could find in the documentation and looked on stack overflow but can find the right words to search for what I am asking
#at this point I have spent too much time on this item and may have tried to do things out of order?  Help me sort out my mess please. :)


    sort_param = request.query_params.get('sort')
    super_type_param = request.query_params.order_by('super_types')
    
    if sort_param:
        supers = supers.order_by(sort_param)
    
    if super_type_param:
   
    
    custom_response_dict = [
        'heroes': [SuperTypes(1)],
        'villains': [SuperTypes(2)]
    ]
        
        

    return Response(custom_response_dict)
   

    
    
        

        
 
