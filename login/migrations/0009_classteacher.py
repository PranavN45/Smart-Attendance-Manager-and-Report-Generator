# Generated by Django 4.1.7 on 2023-04-21 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_delete_classteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('classTeacher_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
            ],
        ),
    ]
