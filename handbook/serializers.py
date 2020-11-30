from rest_framework import serializers

from .models import Handbook, ElementHandbook


class HandbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbook
        fields = ('id', 'title', 'short_title', 'description', 'version', 'start_date')


class ElementHandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementHandbook
        fields = ('id', 'handbook_id', 'code', 'value')
