from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name','last_name','dob','age']
        # '__all__'