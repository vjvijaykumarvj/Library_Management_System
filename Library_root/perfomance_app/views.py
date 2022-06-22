from django.shortcuts import render,redirect
from .models import library_Model
from .forms import library_Forms
# Create your views here.

def Library_dashboard(request):
    # Load all libraryBooks from the Data base(EMPLOYEE)
    library_list = library_Model.objects.all()
    library_dict={
        'library_list': library_list
    }
    return render(request,'perfomance_app/Librarydashboard.html',context=library_dict)
def CreateBook(request):
    # Show the libraryBooks Creation Form
    if request . method == 'GET':
         return render(request,'perfomance_app/createbook.html')
    elif request . method == 'POST':
        # Read the input data from request
        library_form=library_Forms(request.POST)
        #by using modelforms validation
        if library_form.is_valid():
        # save the record from database
            library_form.save()
        #return back to the dashboard
        return redirect('/perfomance/dashboard/')
def book_id(request,pk):
    #create the perticular id dashboard
    #get the single book record(id=pk)
    library_db = library_Model.objects.get(id=pk)
    lib_dictt={
        'library' : library_db
    }
    return render(request,'perfomance_app/book_id.html',context=lib_dictt)
def book_update(request,pk):
    #update the perticular book record
    if request.method == 'GET':
        library_db = library_Model.objects.get(id=pk)
        library_form=library_Forms(instance=library_db)
        library_dict={
            'library' : library_db,
            'libraryform': library_form
        }
        return render(request,'perfomance_app/createbook.html',context=library_dict)
    elif request.method=='POST':
        library_db=library_Model.objects.get(id=pk)
        library_form=library_Forms(request.POST,instance=library_db)
        #using modelforms validations
        if library_form.is_valid():
            library_form.save()
        #return back to the dashboard page
        return redirect('/perfomance/dashboard/')

def book_delete(request,pk):
    #delete the perticular book
    library_db=library_Model.objects.get(id=pk)
    library_db.delete()
    #return ack to dashboard
    return redirect('/perfomance/dashboard/')