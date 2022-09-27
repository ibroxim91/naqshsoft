# Generated by Django 4.0.6 on 2022-09-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_latestresults_name_en_latestresults_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefits_portfolio',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='benefits_portfolio',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='benefits_portfolio',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comunity',
            name='job_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='comunity',
            name='job_ru',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='comunity',
            name='job_uz',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='comunity',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comunity',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comunity',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='banefit_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='banefit_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='banefit_uz',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='detail_name_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='detail_name_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='detail_name_uz',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='text_en',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='text_ru',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='text_uz',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detail_portfolio',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_uz',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]