# Generated by Django 5.1.4 on 2024-12-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('directory', models.CharField(max_length=100)),
                ('release_year', models.DateField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
