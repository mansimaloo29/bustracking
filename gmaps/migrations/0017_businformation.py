# Generated by Django 2.2.4 on 2021-06-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0016_image_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='businformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busnumber', models.CharField(max_length=20)),
                ('busplateno', models.CharField(max_length=20)),
            ],
        ),
    ]