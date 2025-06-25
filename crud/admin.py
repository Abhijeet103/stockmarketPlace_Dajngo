from django.contrib import admin

# Register your models here.
from  .models import *

admin.site.register(UserStock)



@admin.register(Stock)
class StockAdmin(admin.ModelAdmin) :
    list_display = ('ticker' , 'name' ,  'curr_price')
    search_fields = ('ticker' , 'name')
    #list_filter

