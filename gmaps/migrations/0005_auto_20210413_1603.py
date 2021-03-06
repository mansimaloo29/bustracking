# Generated by Django 2.2.4 on 2021-04-13 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0004_auto_20210413_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driverdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busNo', models.IntegerField(max_length=12)),
                ('driverName', models.CharField(max_length=12)),
                ('selectroute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gmaps.Route')),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
