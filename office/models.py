from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django import forms
import datetime

from django.core.validators import RegexValidator
import os

class Customer(models.Model):
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))

    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=31, blank=True, null=True)
    fax = models.CharField(validators=[tel_number_regex], max_length=15, blank=True, null=True)
    tel_number_1 = models.CharField(validators=[tel_number_regex], max_length=15, blank=True, null=True)
    tel_number_2 = models.CharField(validators=[tel_number_regex], max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name

class Post(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="顧客先")
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="材料")
    
    my_company_deadline = models.DateField(null=True, blank=True, default =datetime.date.today ,verbose_name="社内納期")
    customer_deadline = models.DateField(null=True, default = datetime.date.today, blank=True ,verbose_name="客先納期")

    memo = models.TextField(null=True, blank=True ,verbose_name="メモ")

    working_period = models.FloatField(null=True, blank=True ,verbose_name="実働期間")
    created_at = models.DateTimeField(null=True, blank=True, default = datetime.date.today)
    updated_at = models.DateTimeField(null=True, blank=True)

    quantity = models.IntegerField(null=True, blank=True ,verbose_name="図面の枚数", default=1)
    supply = models.BooleanField(default=False, blank=True ,verbose_name="支給されるならチェック")
    price = models.IntegerField(blank=True, null=True ,verbose_name="値段")

    excel_path = models.FilePathField(path=settings.EXCEL_DIR, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True ,verbose_name="図面")
       
    def __str__(self):
        return self.memo

class KidPost(models.Model):
    post_data = models.ForeignKey(Post, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="親情報")
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="顧客先")
    sirial_number = models.IntegerField(blank=True, null=True ,verbose_name="整理番号")
    add_memo = models.TextField(null=True, blank=True ,verbose_name="追加メモ")
    material_name = models.TextField(null=True, blank=True ,verbose_name="材質名")
    created_at = models.DateTimeField(null=True, blank=True, default = datetime.date.today)
    supply = models.BooleanField(default=True, blank=True ,verbose_name="支給されるならチェック")
    quantity = models.IntegerField(null=True, blank=True ,verbose_name="個数", default=1)
    my_company_deadline = models.DateField(null=True, blank=True, default = datetime.date.today ,verbose_name="社内納期")
    customer_deadline = models.DateField(null=True, default = datetime.date.today, blank=True ,verbose_name="客先納期")
    price = models.IntegerField(blank=True, null=True ,verbose_name="値段")
    image = models.ImageField(upload_to='images/',blank=True, null=True ,verbose_name="図面")

    def __str__(self):
        return self.sirial_number
