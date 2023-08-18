from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Advertisement
from .serializers import AdvertisementSerializer, UserSerializer
from .filters import AdvertisementFilter
from .permissions import IsSuperuserOrOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        ads = self.queryset
        if self.request.user.is_anonymous:
            ads = ads.filter(is_draft=False)
        else:
            ads = ads.filter(Q(is_draft=False) | Q(creator = self.request.user))
        return ads


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsSuperuserOrOwnerOrReadOnly()]
        return []
 