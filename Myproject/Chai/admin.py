from django.contrib import admin
from .models import ChaiVarity, Reviews

@admin.register(ChaiVarity)
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_varity', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'review')
