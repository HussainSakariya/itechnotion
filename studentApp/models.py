from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to="student")
    std=models.IntegerField()
    address=models.TextField(max_length=50)
    mo_number=models.IntegerField()
