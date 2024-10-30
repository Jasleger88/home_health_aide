

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['stripeToken']
            amount = form.cleaned_data['amount']

            try:
                charge = stripe.Charge.create(
                    amount=int(amount * 100),  # amount in cents
                    currency='usd',
                    description='Payment description',
                    source=token,
                )
                # Record successful payment in the database
                Payment.objects.create(method='credit_card', amount=amount)
                return redirect('payment_success')  # Define this view accordingly
            except stripe.error.CardError:
                return redirect('payment_error')  # Define this view accordingly

    else:
        form = PaymentForm()
    return render(request, 'payments/checkout.html', {'form': form, 'stripe_key': settings.STRIPE_PUBLISHABLE_KEY})
