# Generated by Django 2.2.4 on 2021-04-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('password1', models.CharField(max_length=15)),
                ('password2', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('0', 'Student'), ('1', 'Driver')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='route',
            name='destination',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='route',
            name='source',
            field=models.CharField(max_length=12),
        ),
    ]