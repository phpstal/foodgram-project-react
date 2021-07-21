# Generated by Django 3.2.5 on 2021-07-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210721_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='is_favorited',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_in_shopping_cart',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
