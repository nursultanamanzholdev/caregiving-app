from django.urls import path
from . import views

urlpatterns = [
    path('https://caregiving-app.onrender.com/', views.dashboard, name='dashboard'),
    path('user_create/', views.user_create, name='user_create'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_update/<int:user_id>', views.user_update, name='user_update'),
    path('user_confirm_delete/<int:user_id>', views.user_confirm_delete, name='user_confirm_delete'),
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),
    path('member_list/', views.member_list, name='member_list'),
    path('member_update/<int:user_id>', views.member_update, name='member_update'),
    path('member_delete/<int:user_id>', views.member_delete, name='member_delete'),
    path('member_create/', views.member_create, name='member_create'),
    path('caregiver_list/', views.caregiver_list, name='caregiver_list'),
    path('caregiver_update/<int:user_id>', views.caregiver_update, name='caregiver_update'),
    path('caregiver_delete/<int:user_id>', views.caregiver_delete, name='caregiver_delete'),
    path('caregiver_create/', views.caregiver_create, name='caregiver_create'),
    path('address_list/', views.address_list, name='address_list'),
    path('address_update/<int:member_user_id>', views.address_update, name='address_update'),
    path('address_delete/<int:member_user_id>', views.address_delete, name='address_delete'),
    path('address_create/', views.address_create, name='address_create'),
    path('job_list/', views.job_list, name='job_list'),
    path('job_update/<int:member_user_id>', views.job_update, name='job_update'),
    path('job_delete/<int:member_user_id>', views.job_delete, name='job_delete'),
    path('job_create/', views.job_create, name='job_create'),
    
    path('jobApplication_list/', views.jobApplication_list, name='jobApplication_list'),
    path('jobApplication_create/', views.jobApplication_create, name='jobApplication_create'),

    path('appointment_create/', views.appointment_create, name='appointment_create'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
]
