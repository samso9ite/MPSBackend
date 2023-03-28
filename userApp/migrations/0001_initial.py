# Generated by Django 4.1.7 on 2023-03-28 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naira_rate', models.CharField(max_length=50)),
                ('bank_rate', models.CharField(max_length=50)),
                ('alipay_rate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='382E50D', max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('yarn_amount', models.CharField(max_length=50)),
                ('naira_amount', models.CharField(max_length=50)),
                ('order_status', models.CharField(choices=[('1', 'PENDING'), ('2', 'APPROVED'), ('3', 'PROCESSING'), ('4', 'ON-SHIP'), ('5', 'ARRIVED'), ('6', 'DELIVERED'), ('7', 'FAILED')], default='Pending', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
