# Generated by Django 4.2 on 2023-05-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(related_name='related_tag', to='new_api.tag'),
        ),
    ]