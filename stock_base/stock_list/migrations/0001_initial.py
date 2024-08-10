# Generated by Django 4.1.3 on 2024-08-10 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ticker', models.CharField(max_length=10, unique=True)),
                ('sector', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('market_cap', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ESGScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environmental_score', models.FloatField()),
                ('social_score', models.FloatField()),
                ('governance_score', models.FloatField()),
                ('overall_score', models.FloatField()),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stock_list.stock')),
            ],
        ),
    ]
