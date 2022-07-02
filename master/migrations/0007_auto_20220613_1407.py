# Generated by Django 3.1.8 on 2022-06-13 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0006_auto_20220610_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='company',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='individual',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='individual',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='individual',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date'),
        ),
    ]
