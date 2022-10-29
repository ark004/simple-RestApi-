from unittest.util import _MAX_LENGTH
from . models import Task
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Task
        fields=['id','task_nm','task_desc','date_created','image']