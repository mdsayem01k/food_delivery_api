# Generated by Django 5.1.1 on 2024-09-08 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_rename_modified_menuitem_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablebooking',
            name='table',
        ),
        migrations.RemoveField(
            model_name='tablebooking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='location',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=255)),
                ('updated_by', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modifiers', to='restaurants.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=255)),
                ('updated_by', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash')], max_length=20)),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=255)),
                ('updated_by', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='RestaurantTable',
        ),
        migrations.DeleteModel(
            name='TableBooking',
        ),
    ]
