# Generated by Django 5.1 on 2024-08-15 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESA', '0018_rename_content_berttweet_emailanalysis_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test',
        ),
        migrations.RemoveField(
            model_name='emailanalysis',
            name='content',
        ),
        migrations.AddField(
            model_name='emailanalysis',
            name='email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ESA.email'),
        ),
        migrations.AlterField(
            model_name='emailanalysis',
            name='sentiment_berttweet',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emailanalysis',
            name='sentiment_huggingface',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
