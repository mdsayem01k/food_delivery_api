# Generated by Django 5.1.1 on 2024-09-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_order_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='modified',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='modified',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='created',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='order',
            name='created_by',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_by',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='created_by',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='updated_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
