# Generated by Django 4.0 on 2021-12-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_alter_eventlist_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='list1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='list2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='list3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EventList',
        ),
    ]