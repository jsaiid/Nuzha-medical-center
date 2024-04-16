# Generated by Django 5.0.2 on 2024-04-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watad', '0003_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField()),
                ('exp_date', models.DateTimeField()),
                ('email', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('about_watad', models.TextField(default='', max_length=100)),
                ('proj_title', models.TextField(default='', max_length=100)),
                ('desc', models.TextField(default='', max_length=100)),
                ('training_prog', models.TextField(default='', max_length=100)),
                ('proj_length', models.TextField(default='', max_length=100)),
                ('quotation_currency', models.TextField(default='', max_length=100)),
                ('how_to_apply', models.TextField(default='', max_length=100)),
                ('note', models.TextField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('subject', models.TextField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
