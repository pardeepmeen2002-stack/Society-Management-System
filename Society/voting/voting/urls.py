from turtle import home
from django.contrib import admin
from django.urls import path, include
from votingapp.views import home, signup, login_view, raise_issue, Select_solution, voting, issue_details, Approve, Reject, Notification


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('raise_issue/', raise_issue, name='raise_issue'),
    path('Select_solution/', Select_solution, name='Select_solution'),
    path('voting/', voting, name='voting'),
    path('issue_details/', issue_details, name='issue_details'),
    path('approve/', Approve, name='approve'),
    path('Reject/', Reject, name='Reject'),
    path('notification/', Notification, name='notification'),
    

]
