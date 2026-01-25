from .models import AnimalProfile


def explain_match(a1, a2):
    reasons = []

    if a1.species == a2.species:
        reasons.append("Same species")

    if a1.habitat == a2.habitat:
        reasons.append("Same habitat")

    if a1.energy_level == a2.energy_level:
        reasons.append("Similar energy level")

    if a1.social_style == a2.social_style:
        reasons.append("Similar social style")

    if a1.bonding_style == a2.bonding_style:
        reasons.append("Compatible bonding style")

    return ", ".join(reasons)


def calculate_match_score(a1, a2):
    score = 0

    if a1.species == a2.species:
        score += 2
    if a1.habitat == a2.habitat:
        score += 2
    if a1.energy_level == a2.energy_level:
        score += 2
    if a1.social_style == a2.social_style:
        score += 2
    if a1.bonding_style == a2.bonding_style:
        score += 2

    return score


def get_matches(profile):
    animals = AnimalProfile.objects.exclude(user=profile.user)
    results = []

    for animal in animals:
        score = calculate_match_score(profile, animal)
        explanation = explain_match(profile, animal)
        results.append((animal, score, explanation))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
