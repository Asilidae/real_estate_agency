from django.db import migrations
import phonenumbers


def replace_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_parse = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phone_parse):
            flat.owner_phone_pure = phone_parse
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(replace_phone_number),
    ]
