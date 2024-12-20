# Generated by Django 5.1.3 on 2024-12-01 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('user_type', models.CharField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')], max_length=10)),
                ('verification_state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('condition', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('property_type', models.CharField(choices=[('house', 'House'), ('flat', 'Flat'), ('commercial', 'Commercial')], max_length=15)),
                ('posted_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='home.person')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='home.person')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.property')),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('L_id', models.AutoField(primary_key=True, serialize=False)),
                ('listing_status', models.BooleanField(default=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.property')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bid_status', models.BooleanField(default=False)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.property')),
            ],
        ),
    ]
