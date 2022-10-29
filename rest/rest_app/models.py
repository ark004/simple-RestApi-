from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Task(models.Model):
    task_nm = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to ='Image/',default="Image/None/Noimg.jpg")