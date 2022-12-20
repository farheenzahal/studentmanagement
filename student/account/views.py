from django.shortcuts import render,redirect
from .models import Course,Contact,Staff
from django.contrib import messages


def sign(request):
    return render(request,'sign.html')

def signup(request):
    return render(request,'signup.html')

def mainbase(request):
    return render(request,'mainbase.html')    

def mainhome(request):
    return render(request,'mainhome.html')  

def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses) 

def contact(request):
    if request.method=="POST":
        if request.POST['name']is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')   

def signup(request):
    if request.method == "POST":
        name=request.POST['name'] 
        email=request.POST['email']  
        password=request.POST['password']  
        phno=request.POST['phno']  
        password2=request.POST['password2']
        if password == password2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer=Staff.objects.create(email = email,name = name,password = password,phno = phno)
                customer.save()
                messages.info(request,'user created')  
                return redirect('sign')  
        else:
            messages.info(request,'password did not match')  
            return redirect('signup') 
    else:
        return render(request,'signup.html')             

def sign(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno

            return redirect('home')
        except Staff.DoesNotExist:
            messages.error(request,'invalid username and password')  
            return redirect('sign') 
    return render(request,'sign.html') 


def forgot(request):
    if request.method =='POST':
        email1=request.POST['email']
        password1=request.POST['password']
        if Staff.objects.filter(email=email1).exists():
           Staff.objects.filter(email=email1).update(password=password1)
           return redirect("sign")
        else:
           messages.error(request,"Invalid email ID")   
           return redirect('forgot') 
    return render(request,'forgot.html')     


def gallery(request):
    return render(request,'gallery.html')


