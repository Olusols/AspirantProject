# Generated by Django 4.0.8 on 2023-07-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_fact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=2000),
        ),
    ]