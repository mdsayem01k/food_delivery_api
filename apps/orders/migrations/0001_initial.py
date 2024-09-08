# Generated by Django 4.2.2 on 2023-06-21 05:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_customer'),
        ('restaurants', '0003_tablebooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete'), ('failed', 'Failed')], default='pending', max_length=255)),
                ('order_status', models.CharField(choices=[('processing', 'Processing'), ('cancelled', 'Cancelled'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')], default='processing', max_length=255)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customer')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitems', to='restaurants.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.cart')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.menuitem')),
            ],
            options={
                'unique_together': {('cart', 'menu_item')},
            },
        ),
    ]
