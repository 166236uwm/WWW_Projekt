from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse

@api_view(['GET'])
def getData(request):
    person = {'imie':'Jan', 'wiek':28}
    return Response(person)

def members(request):
    return HttpResponse("Hello world!")