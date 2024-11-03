# Generated by Django 5.1.2 on 2024-11-03 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_passport_citizen_alter_citizen_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('created_at', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True)),
                ('age', models.IntegerField()),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile', to='users.userprofile')),
            ],
        ),
    ]
