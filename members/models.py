from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register_model(User):
    dor = models.DateField(default=timezone.now)

class Create_class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)
    college_code = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
    

class Join_class(models.Model):
    class_id = models.ManyToManyField(Create_class)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.class_id