# Generated by Django 2.2.4 on 2019-10-17 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_purchase', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.Client'),
        ),
    ]
