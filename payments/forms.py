from django import forms
from .models import Payment
from rooms.models import Room


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['room', 'amount', 'payment_type', 'payment_date']

        widgets = {
            'room': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 150000',
                'step': '0.01',
                'min': '1',
            }),
            'payment_type': forms.Select(attrs={'class': 'form-select'}),
            'payment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

        labels = {
            'room': 'Room Being Paid For',
            'amount': 'Amount Paid (UGX)',
            'payment_type': 'Payment Method',
            'payment_date': 'Date of Payment',
        }

        error_messages = {
            'room': {'required': 'Please select a room.'},
            'amount': {'required': 'Please enter the amount paid.'},
            'payment_type': {'required': 'Please select a payment method.'},
            'payment_date': {'required': 'Please enter the date of payment.'},
        }
