def calculate_bmr(user):
    if user.gender == 'male':
        bmr = 10 * user.weight + 6.25 * user.height - 5 * user.age + 5
    else:
        bmr = 10 * user.weight + 6.25 * user.height - 5 * user.age - 161

    activity_factors = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'extra': 1.9
    }
    
    daily_calories = bmr * activity_factors[user.activity_level]

    if user.health_goal == 'lose_weight':
        daily_calories -= 500
    elif user.health_goal == 'gain_weight':
        daily_calories += 500

    return bmr, daily_calories

def generate_recommendations(user, daily_calories):
    # Placeholder for actual recommendation logic
    recommendations = [
        "Breakfast: Oatmeal with fruits",
        "Lunch: Grilled chicken with quinoa",
        "Dinner: Baked salmon with vegetables",
        "Snacks: Nuts, yogurt, and fruits"
    ]
    return recommendations
