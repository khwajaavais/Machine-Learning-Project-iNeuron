from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('ml_project.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        aggression = request.form['aggression']
        stamina = request.form['stamina']        
        reactions = request.form['reactions']
        potential = request.form['potential']
        positioning = request.form['positioning']
        ball_control = request.form['ball_control']
        strength = request.form['strength']
        marking = request.form['marking']
        crossing = request.form['crossing']
        finishing = request.form['finishing']
        dribbling = request.form['dribbling']
        interceptions = request.form['interceptions']        
        standing_tackle = request.form['standing_tackle']
        heading_accuracy = request.form['heading_accuracy']
        shot_power = request.form['shot_power']
        short_passing = request.form['short_passing']
        gk_reflexes = request.form['gk_reflexes']
        gk_handling = request.form['gk_handling']
        gk_diving = request.form['gk_diving']
        gk_positioning = request.form['gk_positioning']        

        try:    
            prediction = model.predict([[aggression, stamina, reactions, potential, positioning, ball_control, strength, marking, crossing, finishing, dribbling, interceptions, 
                                            standing_tackle, heading_accuracy, shot_power, short_passing, gk_reflexes, gk_handling, gk_diving, gk_positioning]])
        
            return render_template('result.html',prediction_text="PLAYER RATED: {}".format(prediction[0]))         
            print(prediction[0])
            
        except:
            return render_template('index.html')
        
        
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

