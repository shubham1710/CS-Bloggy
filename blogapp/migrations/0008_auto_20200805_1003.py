# Generated by Django 3.1 on 2020-08-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20200805_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdetails',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postdetails',
            name='name',
            field=models.CharField(default='Anonymous', max_length=100),
            preserve_default=False,
        ),
    ]