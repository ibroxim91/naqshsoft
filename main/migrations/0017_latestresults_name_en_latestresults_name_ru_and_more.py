# Generated by Django 4.0.6 on 2022-09-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_detail_portfolio_banefit'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestresults',
            name='name_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='latestresults',
            name='name_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='latestresults',
            name='name_uz',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
