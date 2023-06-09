from django.db import models
import uuid
import json

class Keyword(models.Model):
    keyword_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    count = models.IntegerField()
    in_date = models.CharField(max_length=200)

class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class1 = models.CharField(max_length=20,null=True)
    class2 = models.CharField(max_length=20, null=True)

class News(models.Model):
    news_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin_address = models.URLField()
    title = models.CharField(max_length=200)
    created_date = models.DateField()
    news_agency = models.CharField(max_length=10)
    reporter = models.CharField(max_length=20)
    region = models.CharField(max_length=200, null=True)
    people = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    tag = models.ManyToManyField(Tag)            # 추후 결정
    tag_list = models.TextField(null=True)
    news_contents = models.TextField()
    image_link = models.URLField()
    keyword_list = models.TextField(null=True)
    keyword = models.ManyToManyField(Keyword)


