# Generated by Django 4.1.7 on 2023-03-16 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_university_id_alter_university_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Address', to='app.address', verbose_name='Адрес'),
        ),
    ]
