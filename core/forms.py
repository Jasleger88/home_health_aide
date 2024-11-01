# core/forms.py

from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stripeToken = forms.CharField(max_length=255, required=True)
