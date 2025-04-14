'''Models of layers django app'''
from django.db import models

# Create your models here.

class OSILayerManager(models.Manager):
    '''OSI Layer manager to get model rows by natural key'''
    def public_method(self):
        '''plug for pylint'''
    def get_by_natural_key(self, layer_id):
        '''Method to get model raw by natural key'''
        return self.get(number=layer_id)

class OSILayer(models.Model):
    '''OSI Layer model'''
    number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    rgb = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"Уровень {self.number}: {self.name}"

class Question(models.Model):
    '''Test question model'''
    layer = models.ForeignKey(OSILayer, on_delete=models.CASCADE)
    text = models.TextField()
    explanation = models.TextField(blank=True)
    answer = models.CharField(max_length=255)
    num_of_correct = models.IntegerField(default=0)
    num_of_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:50] + "..." if len(self.text) > 50 else self.text
