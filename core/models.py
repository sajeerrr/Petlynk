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
        ('Rabbit', 'Rabbit'),
        ('Tiger', 'Tiger'),
        ('Lion', 'Lion'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    ENERGY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    SOCIAL_CHOICES = [
        ('Solo', 'Solo'),
        ('Pack', 'Pack'),
        ('Mixed', 'Mixed'),
    ]

    DIET_CHOICES = [
        ('Herbivore', 'Herbivore'),
        ('Carnivore', 'Carnivore'),
        ('Omnivore', 'Omnivore'),
    ]

    BOND_STYLE_CHOICES = [
        ('Slow', 'Slow'),
        ('Balanced', 'Balanced'),
        ('Fast', 'Fast'),
    ]

    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    age = models.IntegerField()

    habitat = models.CharField(max_length=50)
    territory = models.CharField(max_length=50)

    activity_cycle = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)

    energy_level = models.CharField(max_length=10, choices=ENERGY_CHOICES)
    social_style = models.CharField(max_length=10, choices=SOCIAL_CHOICES)
    diet = models.CharField(max_length=10, choices=DIET_CHOICES)
    bonding_style = models.CharField(max_length=10, choices=BOND_STYLE_CHOICES)

    favorite_activity = models.CharField(max_length=100)
    preference = models.CharField(max_length=200)

    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_online(self):
        if not self.last_activity:
            return False
        from django.utils import timezone
        import datetime
        now = timezone.now()
        # Active is within last 5 minutes
        return self.last_activity >= now - datetime.timedelta(minutes=5)

class Bond(models.Model):
    from_animal = models.ForeignKey(
        AnimalProfile,
        on_delete=models.CASCADE,
        related_name='sent_bonds'
    )
    to_animal = models.ForeignKey(
        AnimalProfile,
        on_delete=models.CASCADE,
        related_name='received_bonds'
    )
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    notified = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_animal} → {self.to_animal} ({self.status})"

class Message(models.Model):
    sender = models.ForeignKey(
        AnimalProfile, 
        on_delete=models.CASCADE, 
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        AnimalProfile, 
        on_delete=models.CASCADE, 
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"
