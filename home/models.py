from django.db import models
import uuid

# Create your models here.

class Tasks(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=124)
    description=models.TextField()
    completed=models.BooleanField(default=False)


