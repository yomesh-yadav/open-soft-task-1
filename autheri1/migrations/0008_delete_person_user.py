# Generated by Django 4.0.1 on 2022-01-25 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autheri1', '0007_alter_person_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='person_user',
        ),
    ]
