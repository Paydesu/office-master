from django import forms
from django.db.models.fields import TextField
from .models import Post, KidPost, Customer
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget 


class OfficeForm(ModelForm):

    class Meta:
        model = Post
        fields = ("customer", "memo", 'my_company_deadline', "customer_deadline", "material", "supply", "quantity", "image")
        widgets = {
            'my_company_deadline': forms.SelectDateWidget,
            'customer_deadline': forms.SelectDateWidget,
        }
        
class OfficeKidForm(ModelForm):

    class Meta:
        model = KidPost
        fields = ("post_data","customer", "sirial_number", "quantity", "add_memo", 'my_company_deadline', "customer_deadline", "material_name", "supply", "price", "image")
        widgets = {
            'my_company_deadline': forms.SelectDateWidget,
            'customer_deadline': forms.SelectDateWidget,
        }
    
