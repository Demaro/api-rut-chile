from api_rut.models import Persona, Sexo

from rest_framework import serializers
from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError,    
	EmailField,
	CharField,
	IntegerField,
	ValidationError
)
from django.db.models import Q

from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _

from rest_framework.compat import authenticate


class SexoSerializer(ModelSerializer):

	class Meta: 
		model = Sexo
		fields = ('id', 'nombre')


class PersonaSerializer(ModelSerializer):
	sexo = SexoSerializer(read_only=True)
	class Meta:
		model = Persona
		fields = ('id', 'rut', 'nombres', 'apellidos', 
			'pais', 'region',' comuna', 'provincia', 
			'circunscripcion', 'mesa', 'domicilio_electoral', 'sexo')



class PersonaCreate(ModelSerializer):
	rut = serializers.CharField(validators=[UniqueValidator(queryset=Persona.objects.all(),
	message="Ya existe una persona con este rut")])
	class Meta:
		model = Persona
		fields = ('rut', 'nombres', 'apellidos', 
			'pais', 'region',' comuna', 'provincia', 
			'circunscripcion', 'mesa', 'domicilio_electoral', 'sexo')

		def create(self, validate_data):
			rut                 = validate_data['rut']
			nombres             = validate_data['nombres']
			apellidos           = validate_data['apellidos']
			pais                = validate_data['pais']
			region              = validate_data['region']
			comuna              = validate_data['region']
			provincia           = validate_data['region']
			circunscripcion     = validate_data['circunscripcion']
			mesa                = validate_data['mesa']
			domicilio_electoral = validate_data['domicilio_electoral']
			sexo                = validate_data['sexo']

			persona_obj = Persona(
				rut = rut,
				nombres = nombres,
				apellidos = apellidos,
				pais = pais,
				region = region,
				comuna = comuna,
				provincia = provincia,
				circunscripcion = circunscripcion,
				mesa = mesa,
				domicilio_electoral = domicilio_electoral,
				sexo = sexo
				)
			persona_obj.save()
			










