from django.db import models
from django.urls import reverse

# Create your models here.

class Teacher(models.Model):
    tname = models.CharField(max_length=30)
    phno = models.IntegerField()

    def __str__(self):
        return self.tname

class info(models.Model):
    sname = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    tname = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher')

    def __str__(self):
        return self.sname
    
    def get_absolute_url(self):
        return reverse('facinfo',kwargs={'pk':self.pk})