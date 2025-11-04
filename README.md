
# Titanic Survival Prediction Web App

## Project Overview
This is a Flask web application that predicts whether a Titanic passenger would have survived based on input features like age, fare, cabin class, and more. The model is a **logistic regression** classifier built in scikit-learn and saved with `pickle` for deployment.

This app was originally part of a machine learning assignment and later updated to demonstrate full model deployment.

## Tools & Libraries
- Python (Flask, Pandas, scikit-learn)
- HTML/CSS (Jinja2 templating)
- Pickle (model serialization)

## How It Works
1. User enters passenger data in a form.
2. The app loads a pickled model (`titanic.pkl`).
3. The model predicts whether the passenger would have survived (0 or 1).
4. The final result is displayed back to the user.

## Folder Structure
```
titanic-survival-app/
│
├── application.py        # Main Flask app
├── titanic.pkl           # Pre-trained ML model
├── requirements.txt      # App dependencies
├── templates/
│   ├── index.html        # Form page
│   └── result.html       # Results page
├── static/
│   └── style.css         # (Optional) Styling for front-end
└── README.md             # You're reading it :)
```

## Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/Foraner/titanic-survival-app.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python application.py
   ```
4. Go to `http://127.0.0.1:5000/` in your browser.

## 📝 What I Learned
- How to deploy a scikit-learn model through a Flask back-end.
- Basics of HTML templating with Jinja2.
- Using pickled models and validating form input.

---

**Author:** Patrick Foran  
[LinkedIn](https://www.linkedin.com/in/patrickmforan) · patrickmforan@gmail.com
