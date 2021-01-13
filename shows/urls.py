from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_rating', views.predict_rating, name='predict_rating'),
    path('predict_best_application', views.predict_best_application, name='predict_best_application'),
]
