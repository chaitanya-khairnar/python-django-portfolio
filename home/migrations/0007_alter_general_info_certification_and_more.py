# Generated by Django 4.0.5 on 2022-08-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_summary_general_info_job_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_info',
            name='certification',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='general_info',
            name='programming',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='general_info',
            name='techniques',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='general_info',
            name='tools',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
