# Generated by Django 4.1.7 on 2023-05-28 00:04

import datetime
from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ("office", "0003_auto_20220116_1404"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="customer_done",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="納品できたらチェック"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="my_company_done",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="自社で用意できたらチェック"
            ),
        ),
        migrations.AlterField(
            model_name="kidpost",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.date.today, null=True
            ),
        ),
        migrations.AlterField(
            model_name="kidpost",
            name="customer_deadline",
            field=models.DateField(
                blank=True, default=datetime.date.today, null=True, verbose_name="客先納期"
            ),
        ),
        migrations.AlterField(
            model_name="kidpost",
            name="my_company_deadline",
            field=models.DateField(
                blank=True, default=datetime.date.today, null=True, verbose_name="社内納期"
            ),
        ),
        migrations.AlterField(
            model_name="kidpost",
            name="supply",
            field=models.BooleanField(
                blank=True, default=True, verbose_name="支給されるならチェック"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.date.today, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="customer_deadline",
            field=models.DateField(
                blank=True, default=datetime.date.today, null=True, verbose_name="客先納期"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="excel_path",
            field=models.FilePathField(
                null=True,
                path=pathlib.PurePosixPath(
                    "/Users/genpeirentarou/Desktop/office/office-master/data/excel"
                ),
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="my_company_deadline",
            field=models.DateField(
                blank=True, default=datetime.date.today, null=True, verbose_name="社内納期"
            ),
        ),
    ]
