# Generated by Django 3.2.6 on 2021-09-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20210512_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('correct', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]