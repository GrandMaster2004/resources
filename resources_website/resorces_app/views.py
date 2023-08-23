from django.shortcuts import render
from .models import AddBranch,pyq

# Create your views here.

def def_home(request):
    all_branch = AddBranch.objects.all()
    return render(request, 'home.html',{'branch':all_branch})

def def_pyq(request,branch_name):
    print(branch_name)
    branch = branch_name
    print(branch)
    pyq_data = pyq.objects.filter(branch_name=branch)
    return render(request, 'pyq_show.html',{'data':pyq_data,'branch':branch})

def show_year(request,student_year,branch_name):
    print(f'{student_year} *******************%%%%%%%%%%%%%%%%%%')
    sem_year = student_year
    branch = branch_name
    pyq_year = pyq.objects.filter(student_year=sem_year,branch_name=branch)
    print(f'{pyq_year} -_________________________________----------')
    return render(request, 'year_wise.html',{'data':pyq_year})

def year_year(request,student_year,branch_name,year):
    print(f'{year} *******************%%%000%%%%%%%%%%%%%%% year')
    sem_year = student_year
    branch = branch_name
    pyq_year = pyq.objects.filter(student_year=sem_year,branch_name=branch,year=year)
    pyq_year1 = pyq.objects.filter(student_year=sem_year,branch_name=branch)
    length = len(pyq_year1)
    li = []
    for i in range(length):
        li.append(pyq_year1[i].year)
    print(f'{pyq_year1[1].year} -_________________________________----------')
    print(set(li))
    return render(request, 'year_wise.html',{'show':pyq_year,'data':pyq_year1,'date':set(li)})

def def_about(request):
    return render(request, 'about.html')
def def_team(request):
    return render(request, 'team.html')
def def_contact(request):
    return render(request, 'contact.html')
