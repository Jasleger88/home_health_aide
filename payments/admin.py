from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('method', 'amount', 'timestamp')
    list_filter = ('method',)
    search_fields = ('method',)

admin.site.register(Payment, PaymentAdmin)

