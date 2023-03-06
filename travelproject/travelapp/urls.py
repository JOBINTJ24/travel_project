from. import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('add/',views.addition,name='addition')
    # path('add/', views.multiplication, name='multiplication'),
    # path('add/',views.substraction,name='substraction'),
    # path('add/',views.division,name='division')

]