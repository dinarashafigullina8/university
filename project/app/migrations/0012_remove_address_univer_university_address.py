# Generated by Django 4.1.7 on 2023-03-17 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_university_address_address_univer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='univer',
        ),
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.OneToOneField(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='Address', to='app.address', verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
