from django.contrib.auth.models import User
from .models import AnimalProfile


def seed_animals():
    if AnimalProfile.objects.count() > 5:
        return

    animals = [
        {
            "name": "Luna",
            "species": "Wolf",
            "gender": "Female",
            "age": 4,
            "habitat": "Forest",
            "territory": "Mountains",
            "activity_cycle": "Night",
            "personality": "Loyal",
            "energy_level": "High",
            "social_style": "Pack",
            "diet": "Carnivore",
            "bonding_style": "Balanced",
            "favorite_activity": "Moon howling",
            "preference": "Strong companion"
        },
        {
            "name": "Flint",
            "species": "Fox",
            "gender": "Male",
            "age": 3,
            "habitat": "Forest",
            "territory": "Meadow",
            "activity_cycle": "Night",
            "personality": "Playful",
            "energy_level": "Medium",
            "social_style": "Solo",
            "diet": "Omnivore",
            "bonding_style": "Fast",
            "favorite_activity": "Exploring",
            "preference": "Fun partner"
        },
        {
            "name": "Willow",
            "species": "Deer",
            "gender": "Female",
            "age": 2,
            "habitat": "Forest",
            "territory": "River",
            "activity_cycle": "Day",
            "personality": "Calm",
            "energy_level": "Low",
            "social_style": "Pack",
            "diet": "Herbivore",
            "bonding_style": "Slow",
            "favorite_activity": "Grazing",
            "preference": "Gentle soul"
        },
        {
            "name": "Bruno",
            "species": "Bear",
            "gender": "Male",
            "age": 6,
            "habitat": "Forest",
            "territory": "Cave",
            "activity_cycle": "Day",
            "personality": "Protective",
            "energy_level": "Medium",
            "social_style": "Solo",
            "diet": "Omnivore",
            "bonding_style": "Balanced",
            "favorite_activity": "Fishing",
            "preference": "Peaceful partner"
        }
    ]

    for data in animals:
        user = User.objects.create_user(
            username=data["name"].lower(),
            password="password123"
        )
        AnimalProfile.objects.create(user=user, **data)

    print("Sample animals created")
