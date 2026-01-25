from django.contrib.auth.models import User
from core.models import AnimalProfile
from django.core.files import File
import os

def seed_animals():
    # 1. Clean data
    AnimalProfile.objects.all().delete()
    # Keep the superuser, delete all other users
    User.objects.filter(is_superuser=False).delete()
    
    print("🧹 Purging old data. Creating your 14 custom pets from local folder...")

    # 2. Define the community based on the images in media/pets_image
    pets = [
        {
            "username": "buck", "name": "Buck", "species": "Deer",
            "gender": "Male", "age": 4, "habitat": "Forest", "territory": "Mountain",
            "activity_cycle": "Dusk", "personality": "Majestic", "energy_level": "Medium",
            "social_style": "Herd", "diet": "Herbivore", "bonding_style": "Balanced",
            "favorite_activity": "Running", "preference": "Adventurer",
            "image_filename": "deer.jpg"
        },
        {
            "username": "buddy", "name": "Buddy", "species": "Dog",
            "gender": "Male", "age": 3, "habitat": "Urban", "territory": "House",
            "activity_cycle": "Day", "personality": "Loyal", "energy_level": "High",
            "social_style": "Social Butterfly", "diet": "Omnivore", "bonding_style": "Fast",
            "favorite_activity": "Playing Fetch", "preference": "Playful Friend",
            "image_filename": "dog.jpg"
        },
        {
            "username": "tembo", "name": "Tembo", "species": "Elephant",
            "gender": "Male", "age": 30, "habitat": "Savanna", "territory": "River Bed",
            "activity_cycle": "Day", "personality": "Wise", "energy_level": "Low",
            "social_style": "Pack", "diet": "Herbivore", "bonding_style": "Slow",
            "favorite_activity": "Sunbathing", "preference": "Gentle Soul",
            "image_filename": "elephant.jpg"
        },
        {
            "username": "foxy", "name": "Foxy", "species": "Fox",
            "gender": "Female", "age": 2, "habitat": "Forest", "territory": "Burrow",
            "activity_cycle": "Night", "personality": "Clever", "energy_level": "High",
            "social_style": "Solo", "diet": "Omnivore", "bonding_style": "Fast",
            "favorite_activity": "Hunting", "preference": "Adventurer",
            "image_filename": "fox.jpg"
        },
        {
            "username": "alpaca", "name": "Lama", "species": "Alpaca",
            "gender": "Female", "age": 5, "habitat": "Mountain", "territory": "Valley",
            "activity_cycle": "Day", "personality": "Chill", "energy_level": "Low",
            "social_style": "Solo", "diet": "Herbivore", "bonding_style": "Slow",
            "favorite_activity": "Watching Birds", "preference": "Gentle Soul",
            "image_filename": "lama.jpg"
        },
        {
            "username": "leo", "name": "Leo", "species": "Lion",
            "gender": "Male", "age": 7, "habitat": "Savanna", "territory": "Plains",
            "activity_cycle": "Day", "personality": "Regal", "energy_level": "Medium",
            "social_style": "Pack", "diet": "Carnivore", "bonding_style": "Protective",
            "favorite_activity": "Running", "preference": "Strong Companion",
            "image_filename": "lion.jpg"
        },
        {
            "username": "hoot", "name": "Hoot", "species": "Owl",
            "gender": "Male", "age": 10, "habitat": "Forest", "territory": "Tree",
            "activity_cycle": "Night", "personality": "Wise", "energy_level": "Low",
            "social_style": "Solo", "diet": "Carnivore", "bonding_style": "Slow",
            "favorite_activity": "Watching Birds", "preference": "Gentle Soul",
            "image_filename": "owl.jpg"
        },
        {
            "username": "panda", "name": "Panda", "species": "Panda",
            "gender": "Female", "age": 6, "habitat": "Forest", "territory": "Mountain",
            "activity_cycle": "Day", "personality": "Chill", "energy_level": "Low",
            "social_style": "Solo", "diet": "Herbivore", "bonding_style": "Slow",
            "favorite_activity": "Climbing", "preference": "Gentle Soul",
            "image_filename": "panda.jpg"
        },
        {
            "username": "bagheera", "name": "Bagheera", "species": "Panther",
            "gender": "Male", "age": 8, "habitat": "Jungle", "territory": "Canopy",
            "activity_cycle": "Night", "personality": "Clever", "energy_level": "High",
            "social_style": "Solo", "diet": "Carnivore", "bonding_style": "Fast",
            "favorite_activity": "Hunting", "preference": "Adventurer",
            "image_filename": "panther.jpg"
        },
        {
            "username": "kiwi", "name": "Kiwi", "species": "Parrot",
            "gender": "Female", "age": 12, "habitat": "Jungle", "territory": "Treetops",
            "activity_cycle": "Day", "personality": "Playful", "energy_level": "Medium",
            "social_style": "Mixed", "diet": "Herbivore", "bonding_style": "Fast",
            "favorite_activity": "Watching Birds", "preference": "Playful Friend",
            "image_filename": "parrot.jpg"
        },
        {
            "username": "bandit", "name": "Bandit", "species": "Raccoon",
            "gender": "Male", "age": 2, "habitat": "Urban", "territory": "Garden",
            "activity_cycle": "Night", "personality": "Mischievous", "energy_level": "High",
            "social_style": "Solo", "diet": "Omnivore", "bonding_style": "Instant",
            "favorite_activity": "Hunting", "preference": "Adventurer",
            "image_filename": "racoon.jpg"
        },
        {
            "username": "scrat", "name": "Nutty", "species": "Squirrel",
            "gender": "Male", "age": 1, "habitat": "Forest", "territory": "Tree",
            "activity_cycle": "Day", "personality": "Playful", "energy_level": "Very High",
            "social_style": "Solo", "diet": "Omnivore", "bonding_style": "Fast",
            "favorite_activity": "Climbing", "preference": "Playful Friend",
            "image_filename": "squirrel.jpg"
        },
        {
            "username": "shere_khan", "name": "Shere Khan", "species": "Tiger",
            "gender": "Male", "age": 9, "habitat": "Jungle", "territory": "Grasslands",
            "activity_cycle": "Night", "personality": "Regal", "energy_level": "High",
            "social_style": "Solo", "diet": "Carnivore", "bonding_style": "Slow",
            "favorite_activity": "Hunting", "preference": "Strong Companion",
            "image_filename": "tiger.jpg"
        },
        {
            "username": "ziggy", "name": "Ziggy", "species": "Zebra",
            "gender": "Male", "age": 5, "habitat": "Savanna", "territory": "Plains",
            "activity_cycle": "Day", "personality": "Social", "energy_level": "High",
            "social_style": "Herd", "diet": "Herbivore", "bonding_style": "Balanced",
            "favorite_activity": "Running", "preference": "Gentle Soul",
            "image_filename": "zebra.jpg"
        }
    ]

    # The user says the images are in media/pets_image
    source_folder = "media/pets_image/"

    for data in pets:
        username = data.pop("username")
        image_filename = data.pop("image_filename")
        
        print(f"✨ Creating {data['name']} the {data['species']}...")
        
        # Create User
        user = User.objects.create_user(
            username=username,
            password="password123",
            email=f"{username}@petlynk.com"
        )
        
        # Create Profile
        profile = AnimalProfile(user=user, **data)
        
        # Attach the local image from media/pets_image/
        img_path = os.path.join(source_folder, image_filename)
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                # Save into pet_images/ (where the model expects it)
                profile.image.save(image_filename, File(f), save=True)
        else:
            print(f"⚠️ Warning: Image {image_filename} not found in {source_folder}")
            profile.save()

    print(f"\n✅ Success! Your targeted community of {len(pets)} custom animals is ready.")

if __name__ == "__main__":
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petlynk.settings')
    django.setup()
    seed_animals()
