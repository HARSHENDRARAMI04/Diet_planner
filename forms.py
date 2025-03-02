from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UserProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    weight = IntegerField('Weight (kg)', validators=[DataRequired()])
    height = IntegerField('Height (cm)', validators=[DataRequired()])
    activity_level = SelectField('Activity Level', choices=[
        ('sedentary', 'Sedentary'),
        ('light', 'Lightly active'),
        ('moderate', 'Moderately active'),
        ('active', 'Very active'),
        ('extra', 'Extra active')
    ], validators=[DataRequired()])
    health_goal = SelectField('Health Goal', choices=[
        ('lose_weight', 'Lose Weight'),
        ('maintain_weight', 'Maintain Weight'),
        ('gain_weight', 'Gain Weight')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')
