# Generated by Django 4.1.7 on 2023-04-21 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_remove_classteacher_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClassTeacher',
        ),
    ]
