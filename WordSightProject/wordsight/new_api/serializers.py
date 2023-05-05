from .models import *
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        
        
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


