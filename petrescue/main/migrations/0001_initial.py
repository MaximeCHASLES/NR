# Generated by Django 5.0.4 on 2024-04-25 22:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=64)),
                ('description', models.TextField(max_length=150)),
                ('perdu', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now=True)),
                ('espece', models.CharField(max_length=64)),
                ('ville_nom', models.CharField(blank=True, max_length=64)),
                ('ville_code', models.CharField(blank=True, max_length=64)),
                ('departement_nom', models.CharField(blank=True, max_length=64)),
                ('departement_code', models.CharField(blank=True, max_length=5)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('photo1', models.ImageField(upload_to='photos_animaux/')),
                ('photo2', models.ImageField(blank=True, upload_to='photos_animaux/')),
                ('photo3', models.ImageField(blank=True, upload_to='photos_animaux/')),
                ('no_tatouage', models.CharField(blank=True, max_length=16)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
