# Generated by Django 5.0.1 on 2024-02-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_enterproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterproduct',
            name='quantity_enter_notation',
            field=models.SmallIntegerField(choices=[(0, 'Ayrish'), (1, 'Qo`shish')], default=1),
            preserve_default=False,
        ),
    ]
