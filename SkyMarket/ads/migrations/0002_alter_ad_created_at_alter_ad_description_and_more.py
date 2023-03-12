# Generated by Django 4.1.7 on 2023-03-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
