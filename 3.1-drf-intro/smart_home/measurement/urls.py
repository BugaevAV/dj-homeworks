from django.urls import path
from .views import ListCreateSensorsView, RetriveUpdateSensorView, CreateMeasurementView


urlpatterns = [
    path('sensors/', ListCreateSensorsView.as_view()),
    path('sensors/<pk>/', RetriveUpdateSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()), 
]
