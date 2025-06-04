from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    img=models.ImageField(upload_to='profileimages/')
    join_date=models.DateField
    points=models.IntegerField(default=0)
    achivements=models.IntegerField(default=0)
    certificate=models.IntegerField(default=0)

    def __str__(self):
        return self.name