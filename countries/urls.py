
from django.urls import path


from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('fetch_continent', views.fetch_continent, name='fetch_continent'),
    path('fetch_countries', views.fetch_countries, name='fetch_countries'),
]

