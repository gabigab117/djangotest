# Generated by Django 5.2 on 2025-05-20 17:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_submitted', models.DateTimeField(auto_now_add=True, verbose_name='Date de soumission')),
                ('status', models.CharField(choices=[('pending', 'En attente'), ('resolved', 'Résolu')], default='pending', max_length=50, verbose_name='Statut')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Réclamation',
                'verbose_name_plural': 'Réclamations',
            },
        ),
    ]
