from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_score, name='predict_score'),
    path('set_language', views.set_language, name='select_language'),
]
