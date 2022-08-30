# Generated by Django 4.0.5 on 2022-08-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_project_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='post',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='subheading',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
