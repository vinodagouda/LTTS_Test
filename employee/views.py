from django.shortcuts import render
from .serializers import *
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):

	# DOB logic

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
