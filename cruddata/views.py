from django.shortcuts import render,redirect
from cruddata.forms import CrudForm
from cruddata.models import Crud 
import mysql.connector


# Create your views here.
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Quocanh0972108427",
        database="nckh"
    )
def emp(request):  
    if request.method == "POST":  
        form = CrudForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CrudForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Crud.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Crud.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Crud.objects.get(id=id)  
    form = CrudForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Crud.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  