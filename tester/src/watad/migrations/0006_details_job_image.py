# Generated by Django 5.0.2 on 2024-04-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watad', '0005_details_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='details_job',
            name='image',
            field=models.FileField(default='', upload_to='media/job'),
        ),
    ]
