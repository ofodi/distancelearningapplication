# Generated by Django 4.0.6 on 2022-09-15 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='creg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.courses'),
        ),
    ]