from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,

)



from .serializers import SexoSerializer, PersonaSerializer, PersonaCreate
from api_rut.models import Persona, Sexo
#
#PERMISOS
#
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly


class SexoListarAPI(ListAPIView):
	queryset = Sexo.objects.all()
	serializer_class = SexoSerializer
	permission_classes = [AllowAny]


class PersonaListarAPI(ListAPIView):
	queryset = Persona.objects.all()
	serializer_class = SexoSerializer
	permission_classes = [AllowAny]


class PersonaCreateAPI(CreateAPIView):
	""""
	Creacion de Persona
	"""
	queryset = Persona.objects.all()
	serializer_class = PersonaCreate
	permission_classes = [AllowAny]