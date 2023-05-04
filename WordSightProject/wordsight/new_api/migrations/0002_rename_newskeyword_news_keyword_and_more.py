# Generated by Django 4.2 on 2023-05-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsKeyword',
            new_name='News_Keyword',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='news',
            name='news_agency',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_contents',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='reporter',
            field=models.CharField(max_length=20),
        ),
    ]