# Generated by Django 4.1.7 on 2023-03-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_created_at_alter_ad_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
