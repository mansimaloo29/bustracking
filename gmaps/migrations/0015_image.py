# Generated by Django 2.2.4 on 2021-06-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0014_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]