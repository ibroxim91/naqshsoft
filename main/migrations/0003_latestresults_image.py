# Generated by Django 4.0.6 on 2022-09-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_latestresults_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestresults',
            name='image',
            field=models.ImageField(null=True, upload_to='latest_results'),
        ),
    ]
