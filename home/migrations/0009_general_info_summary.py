# Generated by Django 4.0.5 on 2022-08-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_general_info_contact_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='general_info',
            name='summary',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
