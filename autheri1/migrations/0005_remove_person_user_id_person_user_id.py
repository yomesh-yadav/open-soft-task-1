# Generated by Django 4.0.1 on 2022-01-25 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheri1', '0004_rename_service_icon_person_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person_user',
            name='ID',
        ),
        migrations.AddField(
            model_name='person_user',
            name='id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]