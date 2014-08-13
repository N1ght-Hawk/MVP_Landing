from django.contrib import admin

# Register your models here.
from .models import signup

class signupAdmin(admin.ModelAdmin):
    class Meta:
        model = signup

admin.site.register(signup,signupAdmin)
