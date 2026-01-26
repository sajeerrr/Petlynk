import random
from .models import AnimalProfile

def calculate_match_score(a1, a2):
    """
    Recalibrated matching logic for 11 specific fields:
    - TARGET: Best ~80%, Average ~50%, Worst ~20%
    - Formula: Percentage = (RawPoints * 6.5) + 20 + Jitter
    """
    raw_points = 0
    
    # 1. Species (True compatibility)
    if a1.species == a2.species: raw_points += 1
    
    # 2. Gender (Variety/Diversity boost)
    if a1.gender != a2.gender: raw_points += 1
    
    # 3. Habitat
    if a1.habitat == a2.habitat: raw_points += 1

    # 4. Territory
    if a1.territory == a2.territory: raw_points += 1
    
    # 5. Activity Cycle
    if a1.activity_cycle == a2.activity_cycle or a1.activity_cycle == "Any" or a2.activity_cycle == "Any": 
        raw_points += 1
        
    # 6. Personality
    if a1.personality == a2.personality: raw_points += 1
    
    # 7. Energy Level
    if a1.energy_level == a2.energy_level: raw_points += 1
    
    # 8. Social Style
    if a1.social_style == a2.social_style: raw_points += 1
    
    # 9. Diet
    if a1.diet == a2.diet: raw_points += 1
    
    # 10. Bonding Style
    if a1.bonding_style == a2.bonding_style: raw_points += 1
    
    # 11. Favorite Activity
    if a1.favorite_activity == a2.favorite_activity: raw_points += 1

    # Transformation for ~20% -> ~80% target
    # 9/11 matches will give: (9 * 6.5) + 20 = 78.5%
    base_percentage = (raw_points * 6.5) + 20
    
    # Organic jitter for a premium feel
    jitter = random.randint(-2, 2)
    return max(18, min(92, int(base_percentage + jitter)))

def explain_match(a1, a2):
    reasons = []
    if a1.species == a2.species: reasons.append("Same species")
    if a1.habitat == a2.habitat: reasons.append("Same habitat")
    if a1.energy_level == a2.energy_level: reasons.append("Similar energy")
    if a1.social_style == a2.social_style: reasons.append("Socially compatible")
    if a1.bonding_style == a2.bonding_style: reasons.append("Matching bonding style")
    
    if not reasons:
        return "New horizons await!"
    return ", ".join(reasons[:3]) # Show top 3 reasons

def get_matches(profile):
    animals = AnimalProfile.objects.exclude(user=profile.user)
    results = []

    for animal in animals:
        score = calculate_match_score(profile, animal)
        explanation = explain_match(profile, animal)
        
        match_data = {
            "id": animal.id,
            "name": animal.name,
            "species": animal.species,
            "gender": animal.gender,
            "age": animal.age,
            "image": animal.image,
            "score": score,
            "explanation": explanation,
            "favorite_activity": animal.favorite_activity,
            "energy_level": animal.energy_level,
            "social_style": animal.social_style,
            "bonding_style": animal.bonding_style,
        }
        results.append(match_data)

    # Sort by score for dashboard immersion
    results.sort(key=lambda x: x['score'], reverse=True)
    return results
