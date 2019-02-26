# Generated by Django 2.0 on 2019-02-09 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_auto_20190205_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item_total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=40),
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.Cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Выполняется', 'Выполняется'), ('Оплачен', 'Оплачен')], default='Принят в обработку', max_length=100),
        ),
    ]