# Generated by Django 5.1 on 2024-08-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESA', '0016_rename_content_gbr_emailanalysis_content_berttweet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailanalysis',
            name='content_huggingface',
            field=models.TextField(),
        ),
    ]