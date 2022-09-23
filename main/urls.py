from django.urls import path,include
from .import views


app_name='main'

urlpatterns = [
    path('',views.index,name="index"),
   path('contact.html',views.contact,name="contact"),

]
