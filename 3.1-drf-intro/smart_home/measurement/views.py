# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement


class ListCreateSensorsView(ListCreateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class RetriveUpdateSensorView(RetrieveUpdateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class CreateMeasurementView(CreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer