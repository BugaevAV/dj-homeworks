from django_filters import rest_framework, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(rest_framework.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
