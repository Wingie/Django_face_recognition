from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models




# for admins

# all photos in the dabase must be linked to one person

class batch(models.Model):
    batch_id = models.CharField(primary_key=True,max_length=20)
    date_time = models.DateTimeField()
    

class image(models.Model):
    image_id = models.CharField(primary_key=True,max_length=20)
    image_name = models.CharField(max_length=100)
    batch_id = models.ForeignKey(batch)
    image_pic = models.ImageField(upload_to="images/")
	

class person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'), 
        (u'F', u'Female'),
    )
    person_id = models.CharField(primary_key=True,max_length=20)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    cover = models.ForeignKey(image)



    
    	
class parameter(models.Model):
    parameter_id= models.CharField(primary_key=True,max_length=20)
    batch_id = models.ForeignKey(batch)
    

	
