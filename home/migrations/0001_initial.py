# Generated by Django 4.0.5 on 2022-08-04 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_experience', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='General_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('contact_num', models.IntegerField(null=True)),
                ('e_mail', models.EmailField(max_length=50)),
                ('birth_date', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'General info',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('heading', models.CharField(max_length=100)),
                ('subheading', models.CharField(blank=True, max_length=100)),
                ('summary', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('job_location', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('general_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobs', to='home.general_info')),
                ('job_experience', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='experience', to='home.experience')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
