from django.contrib.auth.models import User
from core.models import AnimalProfile
from django.core.files import File
import os

def seed_animals():
    # 1. Clean data
    AnimalProfile.objects.all().delete()
    # Keep the superuser, delete all other users
    # Adjust this if you want to keep specific users
    User.objects.filter(is_superuser=False).delete()
    
    print("🧹 Purging old data. Rebuilding your 14-pet community...")

    # 2. Define the new community based on local images
    pets = [
        {
            "username": "whiskers", "name": "Whiskers", "species": "Cat",
            "gender": "Female", "age": 3, "habitat": "Urban", "territory": "Living Room",
            "activity_cycle": "Any", "personality": "Chill", "energy_level": "Low",
            "social_style": "Solo", "diet": "Carnivore", "bonding_style": "Slow",
            "favorite_activity": "Sunbathing", "preference": "Gentle Soul",
            "image_filename": "cat.jpg"
        },
        {
            "username": "buck", "name": "Buck", "species": "Deer",
            "gender": "Male", "age": 5, "habitat": "Forest", "territory": "High Ridge",
            "activity_cycle": "Dusk", "personality": "Majestic", "energy_level": "Medium",
            "social_style": "Herd", "diet": "Herbivore", "bonding_style": "Balanced",
            "favorite_activity": "Running", "preference": "Adventurer",
            "image_filename": "deer.jpg"
        },
        {
            "username": "buddy", "name": "Buddy", "species": "Dog",
            "gender": "Male", "age": 2, "habitat": "Garden", "territory": "Backyard",
            "activity_cycle": "Day", "personality": "Loyal", "energy_level": "High",
            "social_style": "Social Butterfly", "diet": "Omnivore", "bonding_style": "Fast",
            "favorite_activity": "Playing Fetch", "preference": "Playful Friend",
            "image_filename": "dog.jpg"
        },
        {
            "username": "tembo", "name": "Tembo", "species": "Elephant",
            "gender": "Male", "age": 35, "habitat": "Savanna", "territory": "River Bed",
            "activity_cycle": "Day", "personality": "Wise", "energy_level": "Low",
            "social_style": "Pack", "diet": "Herbivore", "bonding_style": "Slow",
            "favorite_activity": "Playing in Water", "preference": "Strong Companion",
            "image_filename": "elephant.jpg"
        },
        {
            "username": "goldie", "name": "Goldie", "species": "Fish",
            "gender": "Female", "age": 1, "habitat": "Aquatic", "territory": "Coral Reef",
            "activity_cycle": "Day", "personality": "Quiet", "energy_level": "Low",
            "social_style": "Mixed", "diet": "Omnivore", "bonding_style": "Balanced",
            "favorite_activity": "Watching Birds", "preference": "Gentle Soul",
            "image_filename": "fish.jpg"
        },
        {
            "username": "foxy", "name": "Foxy", "species": "Fox",
            "gender": "Female", "age": 4, "habitat": "Forest", "territory": "Burrow",
            "activity_cycle": "Night", "personality": "Clever", "energy_level": "High",
            "social_style": "Solo", "diet": "Omnivore", "bonding_style": "Fast",
            "favorite_activity": "Hunting", "preference": "Adventurer",
            "image_filename": "fox.jpg"
        },
        {
            "username": "nibbles", "name": "Nibbles", "species": "Hamster",
            "gender": "Male", "age": 1, "habitat": "Urban", "territory": "Tunnel System",
            "activity_cycle": "Night", "personality": "Timid", "energy_level": "Medium",
            "social_style": "Solo", "diet": "Omnivore", "bonding_style": "Instant",
            "favorite_activity": "Running", "preference": "Gentle Soul",
            "image_filename": "hamster.jpg"
        },
        {
            "username": "spirit", "name": "Spirit", "species": "Horse",
            "gender": "Male", "age": 8, "habitat": "Mountain", "territory": "Plains",
            "activity_cycle": "Day", "personality": "Regal", "energy_level": "High",
            "social_style": "Herd", "diet": "Herbivore", "bonding_style": "Protective",
            "favorite_activity": "Running", "preference": "Strong Companion",
            "image_filename": "horse.jpg"
        },
        {
            "username": "azure", "name": "Azure", "species": "Kingfisher",
            "gender": "Male", "age": 2, "habitat": "River Bed", "territory": "High Branch",
            "activity_cycle": "Day", "personality": "Quick", "energy_level": "Medium",
            "social_style": "Solo", "diet": "Carnivore", "bonding_style": "Stoic",
            "favorite_activity": "Watching Birds", "preference": "Adventurer",
            "image_filename": "kingfisher.jpg"
        },
        {
            "username": "kiwi", "name": "Kiwi", "species": "Parrot",
            "gender": "Female", "age": 15, "habitat": "Jungle", "territory": "Treetops",
            "activity_cycle": "Day", "personality": "Playful", "energy_level": "Medium",
            "social_style": "Pair", "diet": "Herbivore", "bonding_style": "Social",
            "favorite_activity": "Watching Birds", "preference": "Playful Friend",
            "image_filename": "parrot.jpg"
        },
        {
            "username": "thumper", "name": "Thumper", "species": "Rabbit",
            "gender": "Female", "age": 2, "habitat": "Garden", "territory": "Burrow",
            "activity_cycle": "Dusk", "personality": "Playful", "energy_level": "High",
            "social_style": "Solo", "diet": "Herbivore", "bonding_style": "Fast",
            "favorite_activity": "Watching Birds", "preference": "Gentle Soul",
            "image_filename": "rabbit.jpg"
        },
        {
            "username": "tank", "name": "Tank", "species": "Rinosaures",
            "gender": "Male", "age": 12, "habitat": "Savanna", "territory": "Water Hole",
            "activity_cycle": "Dusk", "personality": "Stoic", "energy_level": "Medium",
            "social_style": "Solo", "diet": "Herbivore", "bonding_style": "Protective",
            "favorite_activity": "Sunbathing", "preference": "Strong Companion",
            "image_filename": "rinosaures.jpg"
        },
        {
            "username": "khan", "name": "Shere Khan", "species": "Tiger",
            "gender": "Male", "age": 7, "habitat": "Jungle", "territory": "Canopy",
            "activity_cycle": "Night", "personality": "Regal", "energy_level": "High",
            "social_style": "Solo", "diet": "Carnivore", "bonding_style": "Slow",
            "favorite_activity": "Hunting", "preference": "Strong Companion",
            "image_filename": "tiger.jpg"
        },
        {
            "username": "rocky", "name": "Rocky", "species": "Wolf",
            "gender": "Male", "age": 6, "habitat": "Mountain", "territory": "Summit",
            "activity_cycle": "Night", "personality": "Loyal", "energy_level": "Medium",
            "social_style": "Pack", "diet": "Carnivore", "bonding_style": "Protective",
            "favorite_activity": "Running", "preference": "Strong Companion",
            "image_filename": "wolf.jpg"
        }
    ]

    base_media_path = "media/pet_images/"

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
        
        # Attach the local image
        img_path = os.path.join(base_media_path, image_filename)
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                # We save it into the record. Django's ImageField will handle the move/copy to its upload_to location.
                profile.image.save(image_filename, File(f), save=True)
        else:
            print(f"⚠️ Warning: Image {image_filename} not found in {base_media_path}")
            profile.save()

    print(f"\n✅ Success! Your targeted community of {len(pets)} custom animals is ready.")

if __name__ == "__main__":
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petlynk.settings')
    django.setup()
    seed_animals()
