from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    path('thanks/',views.thanks,name='thanks')
]