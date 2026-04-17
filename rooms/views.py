from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import RoomForm

# Create your views here.
def room_list(request):
    all_rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': all_rooms})

def register_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms_list')
    else:
        form = RoomForm()
    
    return render(request, 'register_room.html', {'form': form})


def room_detail(request, pk):
    single_room = get_object_or_404(Room, pk=pk)
    
    return render(request, 'view_room.html', {'room': single_room})

def edit_room(request, pk):
    # 1. Fetch the specific room using its ID (PK)
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == "POST":
        # 2. Fill the form with the NEW data from the user, 
        # but tell it which OLD record to update (instance=room)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms_list')
    else:
        # 3. If they just arrived, show the form with the CURRENT data already filled in
        form = RoomForm(instance=room)

    return render(request, 'edit_room.html', {'form': form, 'room': room})


def delete_room(request, pk):
    # 1. Find the room you want to get rid of
    room = get_object_or_404(Room, pk=pk)
    
    # 2. Delete it from the database
    room.delete()
    
    # 3. Immediately go back to the list page
    return redirect('rooms_list')