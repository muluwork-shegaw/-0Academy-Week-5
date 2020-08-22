import numpy as np
from flask import Flask, request, jsonify,render_template,request 
import json
import pickle
from datetime import datetime

app = Flask(__name__)
model = pickle.load(open('21-08-2020-20-44-58-031.pkl','rb'))


@app.route('/')
def home():
    return render_template('index_2.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    for rendering results on HTML GUI
    '''
    print("here")
    print("maggie :",request.get_json())
    # int_features = [datetime.strptime(x, "%m-%d-%Y") for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # print(final_features)
    # prediction = model.predict(final_features)
    return render_template('index.html')
    # output = round(prediction[0],2)
    # return render_template('index.html',
    #  prediction_text = 'salary is {}'.format(output) )

if __name__ == '__main__':
    app.run(debug = True)


# @app.route('/about',methods=['GET'])
# def about():
#     return "<h1> About maggie</h1>"
# if __name__ == '__main__':
#     app.run(host = 'localhost',port=3333,debug = True)