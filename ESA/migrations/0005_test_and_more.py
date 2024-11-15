# Generated by Django 4.1.6 on 2024-08-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESA', '0004_emailanalysis_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='emailanalysis',
            old_name='sentiment',
            new_name='sentiment_huggingface',
        ),
        migrations.RemoveField(
            model_name='emailanalysis',
            name='category',
        ),
        migrations.AddField(
            model_name='emailanalysis',
            name='probability_huggingface',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailanalysis',
            name='probability_openai',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailanalysis',
            name='sentiment_openai',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='emailanalysis',
            name='time_consumed_huggingface',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailanalysis',
            name='time_consumed_openai',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
