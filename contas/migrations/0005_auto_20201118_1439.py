# Generated by Django 3.1.3 on 2020-11-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20201118_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
