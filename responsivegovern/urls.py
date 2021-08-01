"""responsivegovern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from respgovapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CommonHome,name='CommonHome'),
    path('CustomerHome/',views.CustomerHome,name='Customer Home'),
    path('SignUp/',views.Customer_Registration,name='Sign Up'),
    path('SignIn/',views.SignIn,name='Sign In'),
    
    
    
    
    path('AdminHome/',views.AdminHome,name='Admin Home'),
    path('AdminAddDepartment/',views.AdminAddDepartment,name='AdminAddDepartment'),
    path('AdminAddDepartmentHead/',views.AdminAddDepartmentHead,name='AdminAddDepartmentHead'),
    path('AdminViewDeptHead/',views.AdminViewDeptHead,name='AdminViewDeptHead'),
    path('AdminViewConsumers/',views.AdminViewConsumers,name='AdminViewConsumers'),
    path('AdminViewFeedback/',views.AdminViewFeedback,name='AdminViewFeedback'),
    
    
    
    path('DeptHeadHome/',views.DeptHeadHome,name='DeptHeadHome'),
    path('DeptHeadViewDetailComplaint/',views.DeptHeadViewDetailComplaint,name='DeptHeadViewDetailComplaint'),
    path('DeptHeadForwardComplaint/',views.DeptHeadForwardComplaint,name='DeptHeadForwardComplaint'),
    path('DeptHeadAddEmployee/',views.DeptHeadAddEmployee,name='DeptHeadAddEmployee'),
    path('DeptHeadViewEmployee/',views.DeptHeadViewEmployee,name='DeptHeadViewEmployee'),
    path('DeptHeadViewStatusForwarded/',views.DeptHeadViewStatusForwarded,name='DeptHeadViewStatusForwarded'),
    path('DeptHeadViewFeedback/',views.DeptHeadViewFeedback,name='DeptHeadViewFeedback'),

    
    
    
    
    path('CustomerAddComplaint/',views.CustomerAddComplaint,name='CustomerAddComplaint'),
    path('CustomerViewComplaintStatus/',views.CustomerViewComplaintStatus,name='CustomerViewComplaintStatus'),
    path('CustomerAddFeedback/',views.CustomerAddFeedback,name='CustomerAddFeedback'),
    path('CustomerViewNotification/',views.CustomerViewNotification,name='CustomerViewNotification'),
    path('Customerviewprofile/',views.Customerviewprofile,name='Customerviewprofile'),
    
    
    
    
    path('EmployeeHome/',views.EmployeeHome,name='EmployeeHome'),
    path('EmployeeViewComplaints/',views.EmployeeViewComplaints,name='EmployeeViewComplaints'),
]
