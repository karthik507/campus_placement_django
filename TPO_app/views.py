from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import StudentInfo, JobInfo, EventInfo, CompanyInfo

# Create your views here.
def index(request):
    return render(request, 'includes/index.html')

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully registered.')
        return redirect("/")
    else:
        form = RegisterForm()
        
    return render(request, "registration/register.html", {"form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "registration/login.html",{"form": form})



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

@login_required(login_url='/login/')
def register_student(request):
    return render(request,'TPO_app/register_student.html')

def register_student_submit(request):
    print("Form is submitted")
    print(request.POST['name'])
    print(request.POST['event'])
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    event = request.POST['event']
    eventid = request.POST['eventid']
    Student_Info = StudentInfo(uname=name,email=email, phoneno=phoneno,event=event,eventid=eventid)
    Student_Info.save()
    messages.success(request, 'You have successfully registered.')
    return render(request,'TPO_app/register_student.html')

def eventss(request):
    results=EventInfo.objects.all()
    return render(request,'includes/Events_login.html',{"EventInfo":results})

def companies(request):
    results=CompanyInfo.objects.all()
    return render(request,'includes/company.html',{"CompanyInfo":results})

@login_required(login_url='/login/')
def register_job(request):
    return render(request,'includes/register_job.html')

def register_job_submit(request):
    print("Form is submitted")
    print(request.POST['name'])
    print(request.POST['college'])
    print(request.POST['company'])
    print(request.POST['profile'])
    print(request.POST['graduation'])
    print(request.POST['phoneno'])
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    college = request.POST['college']
    graduation = request.POST['graduation']
    company = request.POST['company']
    companyid = request.POST['companyid']
    profile = request.POST['profile']
    skills=request.POST['skills']

    Job_Info = JobInfo(uname=name, email=email, phoneno=phoneno, college=college, graduation=graduation, company=company,companyid=companyid, profile=profile,skills=skills)
    Job_Info.save()
    messages.success(request, 'Your Application is successfully sent.')
    return render(request,'includes/register_job.html')

def Events_login(request):
     return render(request,'includes/Events_login.html')
    

def upcoming_events(request):
    if request.method=="POST":
        if request.POST.get("eventname") and request.POST.get("description") and request.POST.get("eventdate") and request.POST.get("email1") :
            eventc=EventInfo()
            eventc.eventname=request.POST.get("eventname")
            eventc.description=request.POST.get("description")
            eventc.eventdate=request.POST.get("eventdate")
            eventc.email1=request.POST.get("email1")
            eventc.save()
            messages.success(request, 'Your Event  '+  eventc.eventname   +'  is successfully saved.')
            return render(request,'includes/upcoming_events.html')
    else:
        return render(request,'includes/upcoming_events.html')

def add_company(request):
    if request.method=="POST":
        if request.POST.get("cname") and request.POST.get("role") and request.POST.get("salary"):
            savec=CompanyInfo()
            savec.cname=request.POST.get("cname")
            savec.role=request.POST.get("role")
            savec.salary=request.POST.get("salary")
            savec.save()
            messages.success(request, 'Your Company  '+   savec.cname   +'  is successfully saved.')
            return render(request,'includes/add_company.html')
    else:
        return render(request,'includes/add_company.html')

    
def Statistics(request):
    return render(request,'includes/Statistics.html')
# def home_supply_submit(request):
#     print("Hello form is submitted")
#     companyname = request.POST["companyname"]
#     medicine = request.POST["medicine"]
#     quantity = request.POST["quantity"]
#     Supplier_Info = StudentInfo(medicine=medicine, quantity=quantity, companyname=companyname)
#     Supplier_Info.save()
#     return render(request, "supplier/home_supply.html")
