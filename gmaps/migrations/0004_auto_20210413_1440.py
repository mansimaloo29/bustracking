# Generated by Django 2.2.4 on 2021-04-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0003_auto_20210413_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='password2',
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
