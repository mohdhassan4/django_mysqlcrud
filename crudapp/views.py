from django.shortcuts import render

# Create your views here.
#imp file hy
from crudapp.forms import EmployeeForm
from crudapp.models import employee

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=EmployeeForm()

    return render(request,"index.html", {'form':form})
def show(request):
    employees=employee.objects.all()
    return render(request,"show.html",{'employees':employees})

def edit(request, id):
    Employee=employee.objects.get(id=id)
    return render(request,"edit.html",{'Employee':Employee})

def update(request, id):
    Employee=employee.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=Employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'Employee':Employee})
def delete(request, id):
    Employee=EmployeeForm.objects.get(id=id)
    Employee.delete()
    return redirect('/show')