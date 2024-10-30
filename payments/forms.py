from django import forms

class PaymentForm(forms.Form):
    stripeToken = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount (in USD)")

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("The payment amount must be greater than zero.")
        return amount
