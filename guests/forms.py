from django import forms
from .models import Guest
from rooms.models import Room

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'id_number', 'room']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +256...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Passport or ID number'}),
            # 2. Styling the room dropdown for Bootstrap 5
            'room': forms.Select(attrs={'class': 'form-select'}),
        }
        
        labels = {
            'id_number': 'National ID / Passport Number',
            'room': 'Assign to Room No',
        }

        error_messages = {
            'first_name': {
                'required': "Please enter the guest's first name.",
            },
            'last_name': {
                'required': "Please enter the guest's last name.",
            },
            'email': {
                'invalid': "This email address doesn't look right. Please check it.",
                'unique': "A guest with this email is already registered.",
            },
            'id_number': {
                'unique': "This ID/Passport number already exists in our records.",
            },
            'phone_number': {
                'required': "We need a phone number to contact the guest.",
            }
        }

    # Only show rooms that are NOT occupied
    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        # Filters the dropdown list to show only available rooms
        self.fields['room'].queryset = Room.objects.filter(is_occupied=False)