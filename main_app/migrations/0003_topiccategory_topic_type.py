# Generated by Django 2.0.5 on 2018-05-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20180506_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='topiccategory',
            name='topic_type',
            field=models.CharField(choices=[('YT', 'Youtube'), ('UR', 'URL')], default='YT', max_length=2),
        ),
    ]