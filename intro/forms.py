from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
            'p_name' : "Patient Name",
            'p_phone' :  "Phone Number",
            'p_email' :  "Email id",
            'doc_name' :  "Doctor's Name",
            'booking_date' :  "Booking Date",
        }