# Generated by Django 3.1.7 on 2021-10-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=7000)),
                ('message', models.CharField(max_length=10000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
