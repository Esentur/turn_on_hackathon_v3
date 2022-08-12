from django.contrib import admin
from apps.account.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email']
    search_fields = ['username','email']


############################################

admin.site.register(MyUser, MyUserAdmin)
