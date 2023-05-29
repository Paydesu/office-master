from django import forms
from django.db.models.fields import TextField
from .models import Post, Customer
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget 
import datetime

class OfficeForm(ModelForm):
    class Meta:
        model = Post
        fields = ("customer", "memo", 'my_company_deadline', "customer_deadline", "material", "supply", "quantity", "image", "my_company_done", "customer_done")
        widgets = {
            'my_company_deadline': forms.SelectDateWidget,
            'customer_deadline': forms.SelectDateWidget,
            }
        

class OfficeUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ("customer", "memo", 'my_company_deadline', "customer_deadline", "material", "supply", "quantity", "image", "my_company_done", "customer_done", "price")
        widgets = {
            'my_company_deadline': forms.SelectDateWidget,
            'customer_deadline': forms.SelectDateWidget,
            }


    
