from django.http import HttpResponse
from django.shortcuts import render, redirect
from votingapp.models import signUp
from django.contrib.auth.models import User 

# Create your views here.


def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        data = User.objects.create_user(username=email, email=email, password=password)
        data.save()
        return redirect('login')
    return render(request, 'signup.html')



def login_view(request):
    if request.method == 'POST':
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = User.objects.filter(email=email, password=password)
    
        return redirect('home')
    return render(request, 'login.html')


def raise_issue(request):
    return render(request, 'raise_issue.html')

def Select_solution(request):   
    return render(request, 'Select_solution.html')

def voting(request):
    return render(request, 'voting.html')

def issue_details(request):
    return render(request, 'Issue_details.html')    

def Approve(request):
    return render(request, 'Approve.html')

def Reject(request):
    return render(request, 'Reject.html')

def Notification(request):
    return render(request, 'Notifications.html') 

 





