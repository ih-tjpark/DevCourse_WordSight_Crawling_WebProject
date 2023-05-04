from .models import *
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        
        
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
<<<<<<< Updated upstream
        fields = '__all__'        
=======
        fields = '__all__'
        
>>>>>>> Stashed changes
        
        
class NewsKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Keyword
        fields = '__all__'
        
