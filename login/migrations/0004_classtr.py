# Generated by Django 4.1.7 on 2023-04-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_delete_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classtr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cltrid', models.CharField(max_length=20)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
            ],
        ),
    ]
