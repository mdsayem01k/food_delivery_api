# Generated by Django 5.1.1 on 2024-09-08 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_menuyyitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu_items', to='restaurants.menucategory'),
        ),
        migrations.DeleteModel(
            name='MenuyyItem',
        ),
    ]
