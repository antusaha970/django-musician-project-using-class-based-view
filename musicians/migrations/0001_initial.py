# Generated by Django 5.0.6 on 2024-05-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(error_messages="Name can't be more than 255 characters", max_length=255)),
                ('last_name', models.CharField(error_messages="Name can't be more than 255 characters", max_length=255)),
                ('email', models.EmailField(error_messages='Email must be unique and valid', max_length=254, unique=True)),
                ('phone_number', models.CharField(error_messages='Phone number must be 11 digits', max_length=11)),
                ('instrument', models.CharField(choices=[('Guitar', 'Guitar'), ('Drum', 'Drum'), ('Flute', 'Flute')], max_length=50)),
            ],
        ),
    ]