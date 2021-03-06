# Generated by Django 3.0.3 on 2020-09-28 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiry_month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiry_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='ratings',
            field=models.IntegerField(),
        ),
    ]
