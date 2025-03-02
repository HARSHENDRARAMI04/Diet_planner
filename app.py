from flask import Flask, render_template, request, redirect, url_for
from forms import UserProfileForm
from utils import calculate_bmr, generate_recommendations
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserProfileForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            age=form.age.data,
            gender=form.gender.data,
            weight=form.weight.data,
            height=form.height.data,
            activity_level=form.activity_level.data,
            health_goal=form.health_goal.data
        )
        bmr, daily_calories = calculate_bmr(user)
        recommendations = generate_recommendations(user, daily_calories)
        return render_template('recommendation.html', user=user, bmr=bmr, daily_calories=daily_calories, recommendations=recommendations)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
