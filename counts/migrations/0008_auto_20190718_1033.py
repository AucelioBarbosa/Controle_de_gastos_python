# Generated by Django 2.2.3 on 2019-07-18 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counts', '0007_auto_20190717_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counts.Category'),
        ),
    ]
