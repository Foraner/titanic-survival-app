from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib
import pickle


application = Flask(__name__)

# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------- ML Model Code --------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#

@application.route('/')
@application.route('/about')
def about():

    return render_template("about.html")

@application.route('/titanicPredictor')
def titanicPredictor():

    return render_template("titanicPredictor.html")

def preprocessDataAndPredict(age, sex, pclass):
    # Define and instantiate the variables for the encoded columns
    sex_f=0
    sex_m=0
    pclass_1=0
    pclass_2=0
    pclass_3=0

    if sex=='F':
        sex_f=1
    else:
        sex_m=1

    if pclass=='1':
        pclass_1=1
    elif pclass=='2':
        pclass_2=1
    else:
        pclass_3=1

    # Create the DataFrame for prediction

    age = float(age)

    
    input_df = pd.DataFrame({
        'Age': [age],
        'Sex_female': [sex_f],
        'Sex_male': [sex_m],
        'Pclass_1': [pclass_1],
        'Pclass_2': [pclass_2],
        'Pclass_3': [pclass_3]
    })

    print(input_df)

    # Open the model pickle file
    with open('titanic.pkl', 'rb') as f:
        model = pickle.load(f)

    # Load trained model using joblib
    #model = joblib.load('../../titanic.pkl')

    # Use the model to predict
 
    prediction = model.predict_proba(input_df)[0][1]

    return round(prediction * 100, 1)

@application.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # get form data
        age = request.form.get('age')
        sex = request.form.get('sex')
        pclass = request.form.get('pclass')

        # call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(age, sex, pclass)
            # pass prediction to template
            return render_template('predict.html', prediction=prediction)

        # except ValueError:
        #      return "Please Enter valid values"
        except Exception as e:
            return f"Error: {e}"

    return render_template('predict.html')



# Run on Correct Port
if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host="localhost", port=5000, debug=True)