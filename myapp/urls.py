from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("score_predict.urls")),  # Make sure the app name is 'score_predict'
]
