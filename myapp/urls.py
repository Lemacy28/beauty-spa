from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact.html',views.contact ,name='contact'),
    path('shop.html',views.shop ,name='shop'),
    path('testimonial.html',views.testimonial ,name='testimonial'),
    path('why.html',views.why,name='why'),
    path('services.html', views.services, name='services'),
    path('bookings.html', views.bookings, name='bookings'),
    path('book/<int:service_id>/', views.book_service, name='book_service'),




]