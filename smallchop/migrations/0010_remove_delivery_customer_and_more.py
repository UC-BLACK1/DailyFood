# Generated by Django 4.2.7 on 2023-12-19 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smallchop', '0009_delivery_customer_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingaddress',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='smallchop.order'),
        ),
    ]
