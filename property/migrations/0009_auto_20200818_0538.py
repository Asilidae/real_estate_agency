# Generated by Django 2.2.4 on 2020-08-18 02:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_replace_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализированный номер владельца'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owner_phone_pure', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=20, null=True, region=None, verbose_name='Нормализированный номер владельца')),
                ('owners_phonenumber', models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца')),
                ('owners_flats', models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
