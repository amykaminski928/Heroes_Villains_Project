
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seializers import SuperSerializer
from .models import Super

# Create your views here.
@api_view (['GET'])
def supers_list (request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many = True)

    if request.method == 'GET':
        super_type = request.query_params.get('super_type')
        print(super_type)    
    return Response(serializer.data)
