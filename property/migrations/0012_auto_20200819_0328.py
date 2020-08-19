# Generated by Django 2.2.4 on 2020-08-19 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20200818_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors_complaint', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_complaint', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]
