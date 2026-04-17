from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        # Corrected: Added 'price_per_night' and removed the non-existent 'room'
        fields = ['room_number', 'category', 'price_per_night', 'is_occupied']
        
        widgets = {
            'room_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 101'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price_per_night': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'is_occupied': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            'is_occupied': 'Is this room currently occupied?',
            'price_per_night': 'Nightly Rate',
        }
        
        error_messages = {
            'room_number': {
                'unique': "A room with this number already exists.",
            }
        }

    # Custom validation for exactly 3 digits
    def clean_room_number(self):
        room_no = self.cleaned_data.get('room_number')

        # Since it's an Integer, we convert to string to count digits
        if len(str(room_no)) != 3:
            raise forms.ValidationError("Room numbers must be exactly 3 digits (e.g., 101).")

        return room_no