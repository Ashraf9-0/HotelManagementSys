from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()

    return render(request, 'add_payment.html', {'form': form})


def payment_list(request):
    payments = Payment.objects.select_related('room').order_by('-payment_date')
    return render(request, 'payment_list.html', {'payments': payments})


def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('payment_list')
