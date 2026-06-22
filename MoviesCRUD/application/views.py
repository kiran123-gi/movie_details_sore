from django.shortcuts import render,redirect
from .models import movies
from .forms import moviesForms

# create movies

def create_movies(request):
    if request.method == "POST":
        form = moviesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create")
    else:
        form = moviesForms()
    return render(request,"frontend/create.html",{'form':form})

#read Movie

def read_movies(request):
    object1 = movies.objects.all()
    return render(request,'frontend/read.html',{'object1':object1})

#update Movie

def update_movies(request,pk):
    object2 = movies.objects.get(pk=pk)
    if request.method == "POST":
        form = moviesForms(request.POST,instance=object2)
        if form.is_valid():
            form.save()
            return redirect("update")
    else:
        form = moviesForms()
    return render(request,'frontend/update.html',{'form':form})

#delete movie

def delete_movies(request,pk):
    object3 = movies.objects.get(pk=pk)
    if request.method == "POST":
        object3.delete()
        return redirect("read")
    return render(request,"frontend/delete.html",{"object3":object3})