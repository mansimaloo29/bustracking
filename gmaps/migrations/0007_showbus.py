# Generated by Django 2.2.4 on 2021-04-15 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0006_showroutes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showbus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showbus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gmaps.Driverdetails')),
                ('showbuses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gmaps.Route')),
            ],
        ),
    ]
