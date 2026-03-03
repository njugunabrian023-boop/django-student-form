from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from Dashboard.models import Student



# Create your views here.
@login_required
def dashboard(request):
    students= Student.objects.all()
    return render(request, 'dashboard.html', {'students':students})
def delete_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request,'Student deleted')
        return redirect('dashboard')
    return render(request, 'delete_student.html')

def add_student(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        Student.objects.create(
            image=image,
            name=name,
            age=age,
            course=course,
            email=email,
            gender=gender,
            date=date,
           )

        return redirect('dashboard')
    return render(request, 'add_student.html')

def update_student(request,id):
    student =get_object_or_404(Student,id=id)
    if request.method == 'POST':

       if request.FILES.get('image'):
        student.image = request.FILES.get('image')
       student.name = request.POST.get('name')
       student.age = request.POST.get('age')
       student.course = request.POST.get('course')
       student.email = request.POST.get('email')
       student.gender = request.POST.get('gender')
       student.date = request.POST.get('date')
       student.save()
       return redirect('dashboard')
    return render(request, 'update_student.html', {'student':student})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
            return redirect('signup')
        user =User.objects.create_user(username=username,email=email, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'sign_up.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate (username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request,messages, 'Invalid username or password')
            return redirect('login')
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')