from django.contrib import admin
from webapp.models import Quote, QuoteRating
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','date']
    list_filter = ['name', 'rating']
    search_fields = ['name', 'text']
    fields = ['id', 'text', 'name', 'email', 'status', 'date']
    readonly_fields = ['date', 'id',]


class QuoteRatingAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'quote']
    list_filter = ['user']
    search_fields = ['user']
    fields = ['id', 'user', 'quote']
    readonly_fields = ['id',]


admin.site.register(Quote, QuoteAdmin)
admin.site.register(QuoteRating, QuoteRatingAdmin)
