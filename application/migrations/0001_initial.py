# Generated by Django 2.1.7 on 2019-02-22 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter medication name', max_length=25)),
                ('category', models.CharField(help_text='Enter medication type', max_length=50)),
                ('initial_dose', models.FloatField(help_text='Enter medication initial dose in mg')),
                ('maximum_dose', models.FloatField(help_text='Enter medication maximum dose in mg')),
                ('titration', models.TextField(help_text='Enter medication titration information')),
                ('comments', models.TextField(help_text='Enter comments about medication')),
                ('side_effects', models.TextField(help_text='Enter side effects for medication')),
            ],
            options={
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter patient first name and middle initial', max_length=30)),
                ('last_name', models.CharField(help_text='Enter patient last name', max_length=50)),
                ('dob', models.DateField(help_text='Enter patient date of birth')),
                ('address', models.CharField(help_text='Enter patient current address', max_length=150)),
                ('email', models.EmailField(help_text='Enter patient current email', max_length=50)),
                ('phone', models.CharField(help_text='Enter patient current phone number', max_length=20)),
                ('next_visit', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='Enter the next visit date and time of the patient if applicable')),
                ('notes', models.TextField(help_text='Enter any prescriber notes about patient')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter step title', max_length=25)),
                ('description', models.TextField(help_text='Enter step description')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter disorder treatment type title', max_length=25)),
                ('steps', models.ManyToManyField(to='application.Step')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='current_step',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Step'),
        ),
        migrations.AddField(
            model_name='patient',
            name='medications',
            field=models.ManyToManyField(to='application.Medication'),
        ),
    ]
