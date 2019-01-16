from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm, changeform, catgarysform, brandform, subcatgarysform, catalogform
from django.core.files.storage import FileSystemStorage
from .models import Categary, subcategary, Brand, catalog


def home(request):
    return render(request,'home.html')

def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Registration/Register.html', {'form': form})

def profile(request):
    args = {'user': request.user}
    return render(request, 'Registration/profile.html',args)

def edit(request):
    if request.method == 'POST':
        form = changeform(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = changeform(instance=request.user)
        args = {'form':form}
        return render(request,'Registration/edit_profile.html',args)


def add_categary(request):
    if request.method == 'POST':
        form = catgarysform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categaryview')
    else:
        form = catgarysform()
    return render(request, 'myfile/Create.html',{'form': form})

class categaryview(ListView):
    model = Categary
    template_name= 'myfile/view_categary.html'
    context_object_name = "viewcategary"

class updatecategary(UpdateView):
    fields = '__all__'
    model = Categary
    template_name= 'myfile/update.html'


def delete_cateview(request,pk):
    if request.method == 'POST':
        cate = Categary.objects.get(pk=pk)
        cate.delete()
    return redirect('categaryview')


def add_subcategary(request):
    if request.method == 'POST':
        form = subcatgarysform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subcategaryv')
    else:
        form = subcatgarysform()
    return render(request, 'myfile/Create.html',{'form': form})

class subcategaryv(ListView):
    model = subcategary
    template_name= 'myfile/view_subcategary.html'
    context_object_name = "subviewcategary"

class updatesubcate(UpdateView):
    fields = '__all__'
    model = subcategary
    template_name= 'myfile/update.html'

def Deletesubcate(request,pk):
    if request.method == 'POST':
        d = subcategary.objects.get(pk=pk)
        d.delete()
    return redirect('subcategaryv')


def add_brand(request):
    if request.method == 'POST':
        form = brandform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewbrand')
    else:
        form = brandform()
    return render(request, 'myfile/Create.html',{'form': form})


class viewbrand(ListView):
    model = Brand
    template_name= 'myfile/view_brand.html'
    context_object_name = "viewbrand"

def Deletebrand(request,pk):
    if request.method == 'POST':
        d = Brand.objects.get(pk=pk)
        d.delete()
    return redirect('viewbrand')

def add_catalog(request):
    if request.method == 'POST':
        form = catalogform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogview')
    else:
        form = catalogform()
    return render(request, 'myfile/Create.html',{'form': form})

def addcatlog(request):
    if request.method == 'POST':
        form = catalogform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogview')
    else:
        form = catalogform()
    return render(request, 'myfile/Create.html',{'form': form})

class catalogview(ListView):
    model = catalog
    template_name= 'myfile/view_catalog.html'
    context_object_name = "viewcatalog"
