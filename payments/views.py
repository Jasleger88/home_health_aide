import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from decimal import Decimal

# Set Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Cleaned form data
            token = form.cleaned_data['stripeToken']
            amount = form.cleaned_data['amount']

            try:
                # Convert the amount to cents as Stripe expects amounts in the smallest currency unit (e.g., cents for USD)
                charge = stripe.Charge.create(
                    amount=int(Decimal(amount) * 100),  # convert to cents
                    currency='usd',
                    description='Payment description',
                    source=token,  # Stripe token from the form
                )

                # Record the payment in the database if successful
                Payment.objects.create(
                    method='credit_card',
                    amount=amount
                )
                return redirect('payment_success')

            # Handle specific Stripe errors
            except stripe.error.CardError as e:
                return redirect('payment_error')
            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                return redirect('payment_error')
            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                return redirect('payment_error')
            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                return redirect('payment_error')
            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                return redirect('payment_error')
            except stripe.error.StripeError as e:
                # Display a generic error message to the user
                return redirect('payment_error')
            except Exception as e:
                # Something else happened unrelated to Stripe
                return redirect('payment_error')

    else:
        # For GET requests, render the form
        form = PaymentForm()

    # Pass the form and Stripe publishable key to the template
    return render(request, 'payments/checkout.html', {
        'form': form,
        'stripe_key': settings.STRIPE_PUBLISHABLE_KEY
    })
