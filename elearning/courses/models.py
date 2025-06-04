from django.db import models
from users.models import Users

# Create your models here.
class Courses(models.Model):
    cos_id=models.CharField(max_length=30)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    thump=models.ImageField(upload_to='thumpnails/')
    users=models.ManyToManyField(Users,related_name='reg_courses',null=True)

    def __str__(self):
        return self.name