from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'date_sent')
    search_fields = ('name', 'email', 'message')
    list_filter = ('date_sent',)
    ordering = ('-date_sent',)

    def short_message(self, obj):
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')
    short_message.short_description = 'Message'