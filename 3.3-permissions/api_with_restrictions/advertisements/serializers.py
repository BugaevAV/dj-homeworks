from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name')


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'is_draft')

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate_status(self, value):
        """Проверка соответсвия OPEN может быть только десять обьявлений."""
        open_qty = Advertisement.objects.filter(creator=self.context['request'].user).\
            filter(status='OPEN').count()>=10
        if self.instance.status == value:
            raise ValidationError(f'Текущее обьявление уже имеет статус {value}')
        elif value == 'OPEN' and open_qty:
            raise ValidationError('Превышен лимит открытых обьявлений!')
        elif value == 'OPEN' and self.context['view'].action == 'create' and open_qty:
            raise ValidationError('Новое обьявление превысит лимит открытых обьявлений.\
                                   Закройте либо удалите одно из существующих')
        return value
    