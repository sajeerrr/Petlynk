from django.contrib.auth.models import User
from core.models import AnimalProfile
from django.core.files.base import ContentFile
import requests
import random
import time

def seed_animals():
    AnimalProfile.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()
    
    print("Cleaned old data.")

    animals = [
        # --- Wild/Exotic ---
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
            "preference": "Strong companion",
            "image_url": "https://images.unsplash.com/photo-1549480017-d76466a4b7e8?w=500&q=80" # Wolf/Dog
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
            "preference": "Fun partner",
            "image_url": "https://images.unsplash.com/photo-1516934024742-b461fba47600?w=500&q=80" # Fox
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
            "preference": "Gentle soul",
            "image_url": "https://images.unsplash.com/photo-1598556776373-ac23f790c885?w=500&q=80" # Deer
        },
        {
            "name": "Thumper",
            "species": "Rabbit",
            "gender": "Male",
            "age": 1,
            "habitat": "Burrow",
            "territory": "Garden",
            "activity_cycle": "Dawn/Dusk",
            "personality": "Skittish",
            "energy_level": "High",
            "social_style": "Group",
            "diet": "Herbivore",
            "bonding_style": "Slow",
            "favorite_activity": "Hopping",
            "preference": "Quiet companion",
            "image_url": "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb?w=500&q=80" # Rabbit
        },
        {
            "name": "Sky",
            "species": "Eagle",
            "gender": "Female",
            "age": 4,
            "habitat": "Mountains",
            "territory": "Sky",
            "activity_cycle": "Day",
            "personality": "Proud",
            "energy_level": "High",
            "social_style": "Pair",
            "diet": "Carnivore",
            "bonding_style": "Lifetime",
            "favorite_activity": "Soaring",
            "preference": "Free spirit",
            "image_url": "https://images.unsplash.com/photo-1534063673739-1cf414246872?w=500&q=80" # Eagle
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
            "preference": "Peaceful partner",
            "image_url": "https://images.unsplash.com/photo-1589656966895-2f33e7653819?w=500&q=80" # Bear
        },
        # --- Domestic ---
        {
             "name": "Milo",
             "species": "Cat",
             "gender": "Male",
             "age": 1,
             "habitat": "Urban",
             "territory": "House",
             "activity_cycle": "Any",
             "personality": "Curious",
             "energy_level": "High",
             "social_style": "Solo",
             "diet": "Carnivore",
             "bonding_style": "Fast",
             "favorite_activity": "Chasing lasers",
             "preference": "Playful friend",
             "image_url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&q=80" # Cat
        },
        {
            "name": "Bella",
            "species": "Dog",
            "gender": "Female",
            "age": 2,
            "habitat": "Suburban",
            "territory": "Backyard",
            "activity_cycle": "Day",
            "personality": "Friendly",
            "energy_level": "High",
            "social_style": "Pack",
            "diet": "Omnivore",
            "bonding_style": "Instant",
            "favorite_activity": "Fetch",
            "preference": "Energetic buddy",
            "image_url": "https://images.unsplash.com/photo-1552053831-71594a27632d?w=500&q=80" # Golden Retriever
        },
        {
            "name": "Shadow",
            "species": "Panther",
            "gender": "Male",
            "age": 5,
            "habitat": "Jungle",
            "territory": "Canopy",
            "activity_cycle": "Night",
            "personality": "Mysterious",
            "energy_level": "High",
            "social_style": "Solo",
            "diet": "Carnivore",
            "bonding_style": "Slow",
            "favorite_activity": "Stalking",
            "preference": "Patient partner",
            "image_url": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=500&q=80" # Cat (Panther lookalike)
        },
        {
            "name": "Thumper",
            "species": "Rabbit",
            "gender": "Male",
            "age": 1,
            "habitat": "Burrow",
            "territory": "Garden",
            "activity_cycle": "Dawn/Dusk",
            "personality": "Skittish",
            "energy_level": "High",
            "social_style": "Group",
            "diet": "Herbivore",
            "bonding_style": "Slow",
            "favorite_activity": "Hopping",
            "preference": "Quiet companion",
            "image_url": "https://images.unsplash.com/photo-1589574828135-2c97486e92c2?w=500&q=80" # Rabbit
        },
        {
            "name": "Sky",
            "species": "Eagle",
            "gender": "Female",
            "age": 4,
            "habitat": "Mountains",
            "territory": "Sky",
            "activity_cycle": "Day",
            "personality": "Proud",
            "energy_level": "High",
            "social_style": "Pair",
            "diet": "Carnivore",
            "bonding_style": "Lifetime",
            "favorite_activity": "Soaring",
            "preference": "Free spirit",
            "image_url": "https://images.unsplash.com/photo-1626278772322-297eb0089575?w=500&q=80" # Eagle
        },
        {
            "name": "Leo",
            "species": "Lion",
            "gender": "Male",
            "age": 5,
            "habitat": "Savanna",
            "territory": "Pride Lands",
            "activity_cycle": "Day",
            "personality": "Dominant",
            "energy_level": "Low",
            "social_style": "Pride",
            "diet": "Carnivore",
            "bonding_style": "Loyal",
            "favorite_activity": "Napping",
            "preference": "Queen",
            "image_url": "https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?w=500&q=80" # Lion
        },
         {
            "name": "Bubbles",
            "species": "Fish",
            "gender": "Female",
            "age": 1,
            "habitat": "Reef",
            "territory": "Coral",
            "activity_cycle": "Day",
            "personality": "Forgetful",
            "energy_level": "Medium",
            "social_style": "School",
            "diet": "Omnivore",
            "bonding_style": "Easy",
            "favorite_activity": "Swimming",
            "preference": "Schoolmate",
            "image_url": "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?w=500&q=80" # Fish
        },
         {
            "name": "Ziggy",
            "species": "Zebra",
            "gender": "Male",
            "age": 3,
            "habitat": "Savanna",
            "territory": "Plains",
            "activity_cycle": "Day",
            "personality": "Social",
            "energy_level": "High",
            "social_style": "Herd",
            "diet": "Herbivore",
            "bonding_style": "Group",
            "favorite_activity": "Running",
            "preference": "Striped friend",
            "image_url": "https://images.unsplash.com/photo-1501706362039-c06b2d715385?w=500&q=80" # Zebra
        },
        {
            "name": "Rocky",
            "species": "Raccoon",
            "gender": "Male",
            "age": 2,
            "habitat": "Urban",
            "territory": "Alley",
            "activity_cycle": "Night",
            "personality": "Clever",
            "energy_level": "High",
            "social_style": "Solo",
            "diet": "Omnivore",
            "bonding_style": "Nut-based",
            "favorite_activity": "Scavenging",
            "preference": "Partner in crime",
            "image_url": "https://images.unsplash.com/photo-1497752531616-c3afd9760a11?w=500&q=80" # Raccoon
        },
        {
            "name": "Penny",
            "species": "Penguin",
            "gender": "Female",
            "age": 3,
            "habitat": "Ice",
            "territory": "Glacier",
            "activity_cycle": "Day",
            "personality": "Dapper",
            "energy_level": "Medium",
            "social_style": "Colony",
            "diet": "Carnivore",
            "bonding_style": "Lifetime",
            "favorite_activity": "Sliding",
            "preference": "Cool cat",
            "image_url": "https://images.unsplash.com/photo-1598439210625-5067c578f3f6?w=500&q=80" # Penguin
        },
        {
            "name": "Oliver",
            "species": "Owl",
            "gender": "Male",
            "age": 7,
            "habitat": "Barn",
            "territory": "Farm",
            "activity_cycle": "Night",
            "personality": "Wise",
            "energy_level": "Low",
            "social_style": "Solo",
            "diet": "Carnivore",
            "bonding_style": "Intellectual",
            "favorite_activity": "Observing",
            "preference": "Good listener",
            "image_url": "https://images.unsplash.com/photo-1579353977828-2a4eab540b9a?w=500&q=80" # Owl
        }
    ]

    for data in animals:
        check_name = data["name"].lower()
        
        # Don't skip if exists, delete old user to refresh image if needed (or just skip)
        # For this request, we want to fix images, so lets rebuild if user exists
        if User.objects.filter(username=check_name).exists():
             User.objects.filter(username=check_name).delete()

        print(f"Creating {data['name']}...")
        user = User.objects.create_user(
            username=check_name,
            password="password123"
        )
        
        image_url = data.pop("image_url")
        
        profile = AnimalProfile(user=user, **data)
        
        # Download image
        try:
            # Add a small delay/headers to avoid rate limits
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(image_url, headers=headers, timeout=10)
            if response.status_code == 200:
                profile.image.save(f"{check_name}.jpg", ContentFile(response.content), save=True)
            else:
                print(f"Failed to download image for {check_name}: Status {response.status_code}")
                profile.save()
        except Exception as e:
            print(f"Error downloading image for {check_name}: {e}")
            profile.save()

    print("Seeding complete! 15 profiles added.")
