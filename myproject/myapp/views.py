
from django.shortcuts import render, redirect, HttpResponse
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *
from django.core.paginator import Paginator
from .form import *


from django.views.generic import TemplateView, ListView,DeleteView, View
# from .form import *
# from django.contrib.auth import User


def homepage(request):
    # h_data = Diseases.objects.all()
    # context = {'h_data': h_data}
    return render (request, 'index.html')

def meddetail(request):
    # md_data = Diseases.objects.all()
    # context = {'md_data':md_data}
    return render(request, 'detail.html')

def emedlist(request):
    ml_data = Item.objects.all()
    paginator = Paginator(ml_data, 2)
    page_number = request.GET.get("page")

    
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'elist.html', {'ml_data':ml_data, 'page_obj':page_obj})


def adddisease(request):
    form = DiseaseModelForm()
    context = {'form':form}

    if request.method =='POST':
        form =DiseaseModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('created new item')
        else:
            print('Error')
        return redirect('/')
    
    return render (request, 'diseasecreateform.html',context)
   


# def dis_updateview(request,id):
#     uv_data = Disease.objects.get(id=id)
#     if request.method == 'POST':
#         item_photo = request.FILES('photo_fm')
#         disease_name = request.POST.get('name_fm')
#         disease_symptom = request.POST.get('sym_fm')
        

#         disease = Disease.objects.filter(id=id)
#         disease.update(item_photo=item_photo, disease_name=disease_name, disease_symptom=disease_symptom)
#         return redirect('/')
#     else:
#         # context = {'uv_data': uv_data}
#         return render(request,'diseaseform.html',{'uv_data': uv_data})


def dis_updateview(request,id):
    # pid = request.GET['pid']
    edit_data = Disease.objects.get(id=id)
    
    
    form = DiseaseModelForm(instance=edit_data)
    

    if request.method == 'POST':

        form = DiseaseModelForm(request.POST, instance=edit_data)
        
        if form.is_valid():
            form.save()
        return redirect('/diseasecreateview/')
    context = {'form': form}
    return render  (request,'diseasecreateform.html',context)




def dis_view(request):
    dis_data = Disease.objects.all()
    context = {'dis_data':dis_data}
    return render(request,'disview.html', context)

# def addproduct(request):
#     dis_data = Item.objects.all()
#     context = {'dis_data':dis_data}
#     return render(request,'addproduct.html',context)

def addproduct(request):
    form1 = MedicineModelForm()
    med_data = Item.objects.all()
    context = {'form1':form1,'med_data':med_data}
    if request.method =='POST':
        form1 =MedicineModelForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            

            print('created new item')
            return redirect('/')
        else:
            print('Error')
        return redirect('/')
    
    return render (request, 'addproduct.html',context)





def shop_view(request):
    return render(request,'shop.html' )

def cart_view(request):
    return render(request,'cart.html' )

def checkout(request):
    return render(request,'checkout.html' )


def loginView(request):
    return render(request,'login.html')


def register_view(request):
    if request.method == 'POST':
        Username = request.POST['user_fm']
        password = request.POST['password1_fm']
        
        first_name = request.POST['firstname_fm']
        last_name = request.POST['lastname_fm']
        usr = User.objects.filter(username= Username)
        if usr.exists():
            redirect('/register/')
        else:
            user_obj = User.objects.create_user(username=Username, first_name=first_name, last_name=last_name )
            user_obj.set_password(password)
            # user_obj.is_staff=True
            user_obj.save()
            return redirect('/')
    else:
        return render(request,'register.html')
    

# class UserLoginView(FormView):
#     template_name = 'login.html'
class UserRequiredMixin(object):
    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect('myapp:UserLoginView')
        return super().dispatch(request,*args,**kwargs)
    
class HomeView(UserRequiredMixin,View):
    def get(self, request):
        return render(request, 'register.html')
    

def deleteitem(request,id):
    item_delete = Item.objects.filter(id=id)
    item_delete.delete()
    return redirect('addproduct')
def deletedisease(request,id):
    disease_delete = Disease.objects.filter(id=id)
    disease_delete.delete()
    return redirect('diseaseview')

def medview(request):
    med_data = Item.objects.all()
    
    context ={'med_data':med_data}
    return render(request,'medicineview.html', context )




