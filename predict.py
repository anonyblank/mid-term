import pickle5 as pickle
import xgboost as xgb
from flask import Flask, request, jsonify

with open('./model/model.bin', 'rb') as f_in: # very important to use 'rb' here, it means read-binary
  dv, model = pickle.load(f_in)


app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return "Hello"

@app.route('/predict', methods=['POST'])
def predict():
    employee = dict(request.json)
    employee_feature = dv.transform(employee)
    dtest = xgb.DMatrix(employee_feature, feature_names=list(dv.get_feature_names_out()))
    pred_label = model.predict(dtest)
    return jsonify({'proba': float(pred_label)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9696', debug=True)
      