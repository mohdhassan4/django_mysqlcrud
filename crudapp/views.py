from django.shortcuts import render

# Create your views here.
#imp file hy
from crudapp.forms import employeeform
from crudapp.models import employee

def emp(request):
    if request.method == "POST":
        form = employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=employeeform()

    return render(request,"", {'form':form})
def show(request):
    employees=employee.objects.all()
    return render(request,"",{'employees':employees})

def edit(request, id):
    Employee=employee.objects.get(id=id)
    return render(request,"",{'Employee':Employee})

def update(request, id):
    Employee=employee.objects.get(id=id)
    form=employeeform(request.POST, instance=Employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"",{'Employee':Employee})
def delete(request, id):
    Employee=employee.objects.get(id=id)
    Employee.delete()
    return redirect('/show')