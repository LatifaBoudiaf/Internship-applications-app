"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('forgotPass/', views.forgotPass, name='forgotPass'),
    path('signup/', views.signup, name='signup'),
    path('*', views.PageNotFound, name='page Not Found'),
    path('studentHome/', views.studentHome, name='studentHome'),
    path('studentProfile/', views.studentProfile, name='studentProfile'),
    path('createInternshipApplication/', views.createInternshipApp1,
         name='createInternshipApplication'),
    path('myMarks/', views.myMarks, name='myMarks'),
    path('myMarksDetails/', views.myMarksDetails, name='myMarksDetails'),
    path('myPresence/', views.myPresence, name='myPresence'),
    path('myPresenceDetails/', views.myPresenceDetails, name='myPresenceDetails'),
    path('myApplications/', views.myApplications, name='myApplications'),
    path('existingInternships/', views.existingInternships,
         name='existingInternships'),
    path('existingInternshipsDetails/', views.existingInternshipsDetails,
         name='existingInternshipsDetails'),

    path('adminHome/', views.adminHome, name='adminHome'),
    path('adminProfile/', views.adminProfile, name='adminProfile'),
    path('supervisorHome/', views.supervisorHome, name='supervisorHome'),
    path('supervisorProfile/', views.supervisorProfile, name='supervisorProfile'),
    path('deleteAccount/', views.deleteAccount, name='delete account'),
    path('Applicants/', views.Applicants, name='Applicants'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('deleteAccounts/', views.deleteAccounts, name='deleteAccounts'),
    path('createSupervisor/', views.createSupervisor, name='createSupervisor'),
    path('createAdmin/', views.createAdmin, name='createAdmin'),
    path('ApprovedByAdmin/<str:pk>/',
         views.ApprovedByAdmin, name='ApprovedByAdmin'),
    path('createStudentAccount/', views.createStudentAccount,
         name='createStudentAccount'),
]
