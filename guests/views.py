from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Guest
from .forms import GuestForm

# Create your views here.
def register_guest(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            try:
               
                form.save()
                return redirect('guest_list')
            except ValidationError as e:
                form.add_error(None, e) 
    else:
        form = GuestForm()
    
    return render(request, 'register_guests.html', {'form': form})


def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {'guests': guests})


def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'guest_detail.html', {'guest': guest})


def edit_guest(request, pk):
    # Fetch the guest we want to edit
    guest = get_object_or_404(Guest, pk=pk)
    
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    
    return render(request, 'edit_guest.html', {'form': form, 'guest': guest})


def delete_guest(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    guest.delete()
    return redirect('guest_list')
