# Generated by Django 4.0.1 on 2022-01-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=200)),
                ('service_title', models.CharField(max_length=200)),
                ('service_description', models.TextField()),
            ],
        ),
    ]
