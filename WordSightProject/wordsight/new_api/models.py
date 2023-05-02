import uuid
from django.db import models

# Create your models here.
class News(models.Model):
    news_id = models.UUIDField("News Id", primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=200)
    news_agency = models.CharField("News Agency", max_length=10)
    reporter = models.CharField("Reporter", max_length=20)
    created_date = models.DateField("Created Date")
    news_content = models.TextField("News Content")
    origin_address = models.URLField("Origin Address")
    image_link = models.URLField("Image Link")
    tag = models.CharField("max_length", max_length=200)

class News_Keyword(models.Model):
    news_id = models.ForeignKey("News", on_delete=models.CASCADE)
    keyword_id = models.OneToOneField("Keyword", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=60)

class Keyword(models.Model):
    keyword_id = models.UUIDField("Keyword Id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=60)
    count = models.IntegerField("Count")
    in_date = models.DateField("In Date")

