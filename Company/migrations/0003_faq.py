# Generated by Django 3.2.13 on 2022-09-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
    ]
