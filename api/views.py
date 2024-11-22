from rest_framework.response import Response
from rest_framework.decorators import api_view
from projektWWW.models import Users
from api.serializers import  UsersSerializer

@api_view(['GET'])
def getUser(request):
    person = Users.objects.all()
    serializer = UsersSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUsers(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)