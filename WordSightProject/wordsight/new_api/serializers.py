from .models import *
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["news_id", "origin_address", "title", "created_date"]
        
        
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

<<<<<<< HEAD


=======
# class NewsKeywordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = News_Keyword
#         fields = '__all__'
        
>>>>>>> 0325a71cf69aa3e4b4613a8ca6af87c502172085
