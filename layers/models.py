from django.db import models

# Create your models here.

class OSILayerManager(models.Manager):
    def get_by_natural_key(self, layer_id):
        return self.get(number=layer_id)

class OSILayer(models.Model):
    number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    rgb = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"Уровень {self.number}: {self.name}"

class Question(models.Model):
    layer = models.ForeignKey(OSILayer, on_delete=models.CASCADE)
    text = models.TextField()
    explanation = models.TextField(blank=True)
    answer = models.CharField(max_length=255)
    num_of_correct = models.IntegerField(default=0)
    num_of_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:50] + "..." if len(self.text) > 50 else self.text
    