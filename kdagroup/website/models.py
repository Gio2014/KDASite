from django.db import models
from django.forms import ModelForm

# Create your models here.


class EmailTemplate(models.Model):
	name = models.CharField(max_length=255)
	from_email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.CharField(max_length=1000)
	

	
		
	