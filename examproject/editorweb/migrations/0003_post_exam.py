# Generated by Django 2.2 on 2019-05-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorweb', '0002_auto_20190525_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exam',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]