# Generated by Django 4.0.6 on 2022-09-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_latestresults_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='latest_results')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
