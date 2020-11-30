from django.contrib import admin
from django.urls import path

from school_app import views

app_name = 'school_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('registration/', views.StudentRegisterView, name='registration'),
    path('apply/', views.StudentApplyView, name='apply'),
    path('studentlist/', views.StudentListView, name='studentlist'),
    path('detail/', views.detail, name='detail'),

]
