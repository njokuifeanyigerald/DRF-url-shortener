from rest_framework import serializers
from .models import LinkModel

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkModel
        fields= [
            'original_link','short_link'
        ]