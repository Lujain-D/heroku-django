from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from .models import Country
from .models import Continent
from django.core.paginator import Paginator

from django.http import JsonResponse

import json

# Create your views here.


@csrf_exempt
def fetch_continent(request):

    if request.method == 'POST':
        payload = json.loads(request.body)
        county = payload["country"]
        country = Country.objects.filter(name__contains=county["name"])
        if len(country) == 1:
            return JsonResponse({"status": 200, "continent": {"name": country[0].continent.name, "code": country[0].continent.code}})

        else:
            return JsonResponse({"status": 400, "message":"multiple or no countries with the reqiested names were found."})
    else:
        return JsonResponse({"status": 400, "message": "wrong method"})


@csrf_exempt
def fetch_countries(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        continent = payload
        country_list = Country.objects.filter(continent__name__contains=continent["continent"]["name"])
        paginator = Paginator(country_list, 10)
        page_obj = paginator.get_page(payload["page_number"])
        return JsonResponse({"countries": list(page_obj.object_list.values())})
    else:
        return JsonResponse({"status": 400, "message": "wrong method"})
