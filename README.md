# Diet Planner

Diet Planner is a Flask-based web application that helps users calculate their Basal Metabolic Rate (BMR) and provides personalized dietary recommendations based on their activity level and health goals.

## Features
- User profile form for inputting personal details (name, age, gender, weight, height, activity level, health goal)
- BMR and daily calorie calculation
- Dynamic meal recommendations based on user input
- Simple and user-friendly UI with HTML and CSS

## Tech Stack
- Python (Flask)
- Flask-WTF for form handling
- HTML, CSS for frontend design

## Installation

### Prerequisites
Ensure you have Python installed on your system.

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/DIet_planner.git
   cd DIet_planner
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask app:
   ```sh
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Project Structure
```
DIet_planner/
│── app.py              # Main Flask application
│── forms.py            # User profile form handling
│── models.py           # User data model
│── utils.py            # BMR calculation & recommendations
│── templates/          # HTML files for frontend
│── static/             # CSS and other static files
│── requirements.txt    # List of dependencies
│── README.md           # Project documentation
```


