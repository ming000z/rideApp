# Generated by Django 4.1.5 on 2023-02-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_share_share_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]