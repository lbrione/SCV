# Generated by Django 4.2.3 on 2023-07-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemAnalyticalPlans', '0004_alter_analytical_plan_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_version',
            name='creation_date',
            field=models.CharField(max_length=10),
        ),
    ]