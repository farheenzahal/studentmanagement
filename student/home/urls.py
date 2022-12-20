from django.urls import path
from . import views

urlpatterns= [
    path('home/',views.Home.as_view(),name='home'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('showstaff/',views.Showstaff.as_view(),name='showstaff'),
    path('showstudents/',views.Showstudent.as_view(),name='showstudents'),
    path('forms/',views.Form.as_view(),name='forms'),
    path('showstudents/',views.Show.as_view(),name='showstudents'),
    path('edit/',views.Edit.as_view(),name='edit'),
    path('delete/',views.Delete.as_view(),name='delete'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('editprofile/',views.Editprofile.as_view(),name='editprofile'),


]    