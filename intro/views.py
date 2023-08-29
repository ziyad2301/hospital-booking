from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.
def home(request):



    return render(request, 'home.html')

def doctor(request):

    doctor = Doctors.objects.all()

    return render(request, 'doctor.html', {'doctor' : doctor})

def department(request):

    dept = Departments.objects.all()

    return render(request, 'department.html', {'dept' : dept})

def contact(request):


    return render(request, 'contact.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form' : form
    }

    return render(request, 'booking.html',dict_form)

def about(request):


    return render(request, 'about.html')

# def register(request):


#     return render(request, 'register.html')

# def login(request):


#     return render(request, 'login.html')

