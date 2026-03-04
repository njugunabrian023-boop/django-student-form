from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to = 'students/', null=True, blank=True)
    name = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=20,null=True)
    date =   models.DateField(null=True)

    def __str__(self):
        return self.name

class Exams(models.Model):
        name = models.CharField(max_length=20)
        exam_code = models.IntegerField()
        date = models.DateField()

        def __str__(self):
            return self.name
class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=15)
    amount = models.IntegerField()
    checkout_request_id = models.IntegerField(max_length=100,blank=True,null=True)
    status = models.IntegerField(max_length=20,default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone