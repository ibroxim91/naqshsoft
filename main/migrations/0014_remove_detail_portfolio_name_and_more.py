# Generated by Django 4.0.6 on 2022-09-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_name_portfolio_portfolio_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail_portfolio',
            name='name',
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='detail_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]