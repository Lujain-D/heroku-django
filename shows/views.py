from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier

from django.http import JsonResponse

import json

import numpy as np


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


#  Request shape
# {
#     "age": 18,
#     "year": 2013,
#     "netflix": 1,
#     "hulu": 0,
#     "prime video": 0,
#     "disney": 1
# }

@csrf_exempt
def predict_rating(request):
    if request.method == 'POST':

        # scaled = scaler.transform(np.array([2005, 7, 0, 0, 1, 0]).reshape(1, -1))
        # score = score_prediction_model.predict(scaled)
        #
        # print('The nltk version is {}.'.format(sklearn.__version__))

        try:

            json_data = json.loads(request.body)
            linear_reg = joblib.load("shows/lin-reg.sav")
            scaler = joblib.load("shows/lin-reg_scaler.sav")
            payload_info = np.array([json_data["year"], json_data["age"], json_data["netflix"], json_data["hulu"], json_data["prime video"], json_data["disney"]]).reshape(1, -1)
            scaled = scaler.transform(payload_info).reshape(1, -1)
            predicted_score = round(linear_reg.predict(scaled)[0], 1)
            payload = {"Predicted IMDb": predicted_score, "status": 200}
            return JsonResponse(payload)

        except:
            return JsonResponse({"status": 500,  })

    else:
        return JsonResponse({"status": 400, "message": "wrong method"})



#{
#    "age": 18,
#    "year": 2000,
#    "imdb": 9
#}
@csrf_exempt
def predict_best_application(request):
    if request.method == 'POST':

        try:

            application_dictionary = {
                0: "Disney+",
                1: "Netflix",
                2: "Hulu",
                4: "Prime Video"
            }

            json_data = json.loads(request.body)

            classifier = joblib.load("shows/xg_classifier2.sav")

            scaler = joblib.load("shows/classification_scaler2.sav")


            payload_info = np.array([json_data["year"], json_data["age"], json_data["imdb"]]).reshape(1, -1)
            scaled = scaler.transform(payload_info).reshape(1, -1)

            channel_number = classifier.predict(scaled)[0]

            payload = {"channel": application_dictionary[channel_number], "status": 200}
            return JsonResponse(payload)

    #
        except:

            return JsonResponse({"status": 500 })

    else:
        return JsonResponse({"status": 400})
