from django.db import models

class Persona(models.Model):
	rut 	  		= models.CharField(max_length=9)
	nombres   		= models.CharField(max_length=100)
	apellidos 		= models.CharField(max_length=100)
	pais			= models.CharField(max_length=20)
	region    		= models.CharField(max_length=20)
	comuna   		= models.CharField(max_length=20)
	provincia 		= models.CharField(max_length=20)
	circunscripcion = models.CharField(max_length=50)
	mesa			= models.CharField(max_length=50)
	domicilio_electoral = models.CharField(max_length=100)
	sexo				= models.ForeignKey("Sexo", on_delete=models.CASCADE)


	def __str__(self):
		return self.nombre



class Sexo(models.Model):
	nombre = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre