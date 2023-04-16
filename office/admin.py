from django.contrib import admin
from .models import Post, Customer, Material, KidPost

admin.site.register(Post)
admin.site.register(Customer)
admin.site.register(Material)
admin.site.register(KidPost)