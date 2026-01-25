from django.db import models
from django.contrib.auth.models import User


class AnimalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    SPECIES_CHOICES = [
        ('Wolf', 'Wolf'),
        ('Fox', 'Fox'),
        ('Deer', 'Deer'),
        ('Bear', 'Bear'),
        ('Owl', 'Owl'),
    ]

    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    habitat = models.CharField(max_length=50)
    activity_cycle = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)
    preference = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bond(models.Model):
    animal1 = models.ForeignKey(
        AnimalProfile, related_name='bond_from', on_delete=models.CASCADE
    )
    animal2 = models.ForeignKey(
        AnimalProfile, related_name='bond_to', on_delete=models.CASCADE
    )
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.animal1} ❤️ {self.animal2}"
