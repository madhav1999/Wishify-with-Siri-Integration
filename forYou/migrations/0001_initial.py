# Generated by Django 4.0.3 on 2022-04-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fordb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('description', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
