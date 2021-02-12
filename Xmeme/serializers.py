from rest_framework import serializers
from . models import memes

class memesSerializer(serializers.Serializer):
    class Meta:
        model = memes
        fields = '__all__'