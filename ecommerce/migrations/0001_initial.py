# Generated by Django 3.0.3 on 2020-09-28 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(max_length=11)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=20)),
                ('ratings', models.IntegerField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(max_length=20)),
                ('csv_number', models.CharField(max_length=20)),
                ('expiry_month', models.IntegerField(max_length=10)),
                ('expiry_year', models.IntegerField(max_length=10)),
                ('card_type', models.CharField(max_length=20)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.IntegerField(max_length=20)),
                ('delivered', models.CharField(max_length=20)),
                ('order_number', models.IntegerField()),
                ('paid', models.CharField(max_length=20)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Payment')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Product')),
            ],
        ),
    ]
