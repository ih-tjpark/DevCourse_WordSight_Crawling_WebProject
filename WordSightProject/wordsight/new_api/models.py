from django.db import models
import uuid

class News(models.Model):
    news_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin_address = models.URLField()
    title = models.CharField(max_length=200)
    created_date = models.DateField(null=True, blank=True)
    news_agency = models.CharField(max_length=10)
    reporter = models.CharField(max_length=20)
    region = models.CharField(max_length=200, null=True)
    people = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    tag = models.CharField(max_length=200)              # 추후 결정 
    news_contents = models.TextField()
    image_link = models.URLField()
    
class Keyword(models.Model):
    keyword_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    count = models.IntegerField()
    in_date = models.CharField(max_length=200)

    
class News_Keyword(models.Model): # pk 자동생성
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, db_column="news_id")
    keyword_id = models.OneToOneField(Keyword, on_delete=models.CASCADE, db_column="keyword_id") # 여러 개 
    name = models.CharField(max_length=200) # 추후 결정 

