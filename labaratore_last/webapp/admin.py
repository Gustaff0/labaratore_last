from django.contrib import admin
from webapp.models import Quote
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'rating', 'date']
    list_filter = ['name', 'rating']
    search_fields = ['name', 'text']
    fields = ['id', 'text', 'name', 'email', 'rating', 'status', 'date']
    readonly_fields = ['date', 'id',]


admin.site.register(Quote, QuoteAdmin)
