from flask import Flask, render_template, request, jsonify
import os
import json
import pickle

import dice_ml
import pandas as pd
from dice_ml import Dice

app = Flask(__name__)

model = pickle.load(open("student_performance_regressor.pk1", "rb"))
data = pd.read_csv("Transformed_Student_Performance.csv")

@app.route("/hello")
def say_hello():
    return json.dumps({"msg": "Hello from Flask"})


@app.route("/counterfactual", methods=['GET', 'POST'])
def counterfactuals():

    request_args = request.json
    
    continuous_features = [
        'Hours Studied',
        'Sleep Hours',
        'Sample Question Papers Practiced',
        'Extracurricular Activities',
      ]
    target_name = "Target"
        
    d = dice_ml.Data(dataframe=data, continuous_features=continuous_features, outcome_name=target_name)
    m = dice_ml.Model(model=model, backend="sklearn", model_type='regressor')
    
    exp = Dice(d, m, method="random")

    for key, val in request_args.items():
        request_args[key] = [val]

    request_dataframe = pd.DataFrame(request_args)
        
    predicted_performance = float(model.predict(request_dataframe))

    # Choose a reasonable goal, expressed as a % increase from the predicted performance
    lower_bound = predicted_performance*1.1
    upper_bound = max(predicted_performance*1.4, 100)

    result = exp.generate_counterfactuals(
        request_dataframe,
        total_CFs=2,
        desired_range=[lower_bound, upper_bound],
        features_to_vary=[
            'Hours Studied',
            'Sleep Hours',
            'Sample Question Papers Practiced',
        ]
    )

    return json.dumps(genetic.to_json())
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
