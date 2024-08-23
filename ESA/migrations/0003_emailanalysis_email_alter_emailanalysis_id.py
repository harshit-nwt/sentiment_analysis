# Generated by Django 5.1 on 2024-08-12 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESA', '0002_alter_emailanalysis_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailanalysis',
            name='email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ESA.email'),
        ),
        migrations.AlterField(
            model_name='emailanalysis',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]