from django.contrib import admin
from accounts.models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','is_staff','is_superuser')

admin.site.register(Account,AccountAdmin)
