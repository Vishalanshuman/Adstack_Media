# Generated by Django 5.1.4 on 2024-12-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
