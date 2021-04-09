from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
   
    RegNo = models.CharField(max_length=40)
    course = models.CharField(max_length=40)
    current_GPA = models.CharField(max_length=20)
    

    def __str__(self):
        return self.firstname + " " + self.lastname
        