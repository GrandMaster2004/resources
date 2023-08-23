from django.shortcuts import render
from .models import AddBranch,pyq,pdf_formate

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
    sem_year = student_year
    branch = branch_name
    pyq_year = pdf_formate.objects.filter(student_year=sem_year,branch_name=branch)
    return render(request, 'year_wise.html',{'data':pyq_year})

def year_year(request,student_year,branch_name,year):
    sem_year = student_year
    branch = branch_name
    pyq_year = pyq.objects.filter(student_year=sem_year,branch_name=branch,year=year)
    pyq_year1 = pdf_formate.objects.filter(student_year=sem_year,branch_name=branch)
    pyq_pdf1 = pdf_formate.objects.filter(student_year=sem_year,branch_name=branch,year=year)
    # print(f'{pyq_pdf[0].pyq_pdf}  ---------------')
    return render(request, 'year_wise.html',{'show':pyq_year,'data':pyq_year1,'pdf':pyq_pdf1[0].pyq_pdf})



def def_about(request):
    return render(request, 'about.html')
def def_team(request):
    return render(request, 'team.html')
def def_contact(request):
    return render(request, 'contact.html')
