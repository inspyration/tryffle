# Generated by Django 5.0.6 on 2024-05-28 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaded_pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpdf',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentpdf',
            name='page_number',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='documentpdf',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentpdf',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]