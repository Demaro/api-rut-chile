from django.conf.urls import url
from django.urls import path, include



from .views import (
	SexoListarAPI,
	PersonaListarAPI,
	PersonaCreateAPI
	)

urlpatterns = [
	url(r'^sexo/', SexoListarAPI.as_view(), name='sexolist'),
	url(r'^$', PersonaListarAPI.as_view(), name='persona'),
	url(r'^add', PersonaCreateAPI.as_view(), name='personalist'),

]