# Generated by Django 3.1.8 on 2022-06-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_auto_20220613_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='refrence',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sales_person',
            field=models.CharField(max_length=100, null=True),
        ),
    ]