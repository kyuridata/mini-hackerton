# Generated by Django 2.2 on 2019-05-25 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editorweb', '0003_post_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='editorweb.Person'),
        ),
    ]