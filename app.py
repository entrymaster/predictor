from flask import Flask, jsonify, request
import numpy as np
import joblib

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    query = request.get_json()
    model_input = query['values'].split(' ')

    nitrogen_content = float(model_input[0])
    phosphorus_content = float(model_input[1])
    potassium_content = float(model_input[2])
    temperature_content = float(model_input[3])
    humidity_content = float(model_input[4])                                                                                                  
    ph_content = float(model_input[5])
    rainfall = float(model_input[6])

    predict_data = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall])

    predict1 = predict_data.reshape(1,-1)

    
        
    classifier = joblib.load('RegressorRFC.pkl')
    predict_crop = classifier.predict(predict1)

    crop_name = str()
    if predict_crop == 0:
        crop_name = 'Apple'
    elif predict_crop == 1:
        crop_name = 'Banana'
    elif predict_crop == 2:
        crop_name = 'Blackgram'
    elif predict_crop == 3:
        crop_name = 'Chickpea'
    elif predict_crop == 4:
        crop_name = 'Coconut'
    elif predict_crop == 5:
        crop_name = 'Coffee'
    elif predict_crop == 6:
        crop_name = 'Cotton'
    elif predict_crop == 7:
        crop_name = 'Grapes'
    elif predict_crop == 8:
        crop_name = 'Jute'
    elif predict_crop == 9:
        crop_name = 'Kidneybeans'
    elif predict_crop == 10:
        crop_name = 'Lentil'
    elif predict_crop == 11:
        crop_name = 'Maize'
    elif predict_crop == 12:
        crop_name = 'Mango'
    elif predict_crop == 13:
        crop_name = 'Mothbeans'
    elif predict_crop == 14:
        crop_name = 'Mungbeans'
    elif predict_crop == 15:
        crop_name = 'Muskmelon'
    elif predict_crop == 16:
        crop_name = 'Orange'
    elif predict_crop == 17:
        crop_name = 'Papaya'
    elif predict_crop == 18:
        crop_name = 'Pigeonpeas'
    elif predict_crop == 19:
        crop_name = 'Pomegranate'
    elif predict_crop == 20:
        crop_name = 'Rice'
    elif predict_crop == 21:
        crop_name = 'Watermelon'
    return jsonify({'prediction': crop_name})


if __name__ == '__main__':
     app.run(port=8080, debug=True)