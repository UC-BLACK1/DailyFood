# Generated by Django 4.2.7 on 2023-12-19 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smallchop', '0011_delivery_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='shippingaddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smallchop.shippingaddress'),
        ),
    ]