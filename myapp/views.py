from django.shortcuts import render
from myapp.forms import ServiceForm, BookingForm
from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import ServiceForm, BookingForm
from myapp.models import Service, Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')
    services_list = Service.objects.all()  # Fetch all services
    return render(request, 'index.html', {'services': services})


def contact(request):
    return render(request, 'contact.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def shop(request):
    return render(request, 'shop.html')

def why(request):
    return render(request, 'why.html')




def services(request):
    print("Services page loaded")
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services})

@login_required
def add_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'services.html', {'form': form})
from django.contrib.auth.decorators import login_required

@login_required
def bookings(request):
    print("Bookings page loaded")
    user_bookings = Booking.objects.filter(user=request.user)  # Show only user's bookings
    return render(request, 'bookings.html', {'bookings': bookings})


from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required


@login_required
def book_service(request, service_id):
    service = Service.objects.get(id=service_id)  # Get the selected service
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service  # Set the selected service
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm(initial={'services': service})  # Pre-fill the service

    return render(request, 'book_service.html', {'form': form})
