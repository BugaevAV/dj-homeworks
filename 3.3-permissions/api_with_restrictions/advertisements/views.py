from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Advertisement
from .serializers import AdvertisementSerializer, UserSerializer
from .filters import AdvertisementFilter
from .permissions import IsSuperuserOrOwnerOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    """ViewSet для объявлений."""

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsSuperuserOrOwnerOrReadOnly()]
        return []
 