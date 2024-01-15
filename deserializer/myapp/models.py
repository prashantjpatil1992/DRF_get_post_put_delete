from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=100,null=True)


    # def __str__(self):
    #     return f'{self.id} {self.name} {self.age} {self.city}'