from django.db import models
from projects.models import Project  
# Create your models here.


class Bug(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    AssignedTo = models.CharField(max_length= 100)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, to_field='id')
   