# Generated by Django 2.2.4 on 2021-04-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=1)),
                ('destination', models.CharField(max_length=1)),
            ],
        ),
    ]
