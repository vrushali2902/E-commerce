# Generated by Django 3.2.7 on 2022-02-28 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='OrderesdDate',
            new_name='ordered_date',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='quantiy',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]