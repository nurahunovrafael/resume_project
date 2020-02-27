from django.contrib import admin
from .models import Person

# Register your models here.

@admin.register(Person)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name', 'last_name', 'middle_name', 'birth_date', 'email', 'sex', 
                    'marital_status', 'phone', 'citizenship', 'city' )
    list_filter = ('sex', 'citizenship', 'marital_status', 'last_name', 'first_name')
    search_fields = ('sex', 'citizenship', 'marital_status', 'last_name', 'first_name')