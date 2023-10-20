from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from crudmodel.models import MyUser
from django.contrib import messages
from .forms import AddUSerForm,Myform,MyModelForm

def home(request):
       form=MyModelForm(request.POST or None)
       if form.is_valid():
              form.save()
              messages.success(request," Successfully Data Saved!!")
              
              return redirect('home')
              
              
       return render(request,"home.html",{'form':form})


def editdata(request,cid): 
        venu=MyUser.objects.get(id=cid)
        form=MyModelForm(request.POST or None,instance=venu)
        if form.is_valid():
              form.save()
              messages.success(request," Successfully Updated!!")
              return redirect('home')

       
        return render(request,"edit_data.html",{'venu':venu,'form':form})  
                        

def adduser(request):
         dbdata=MyUser.objects.all()
         data={
                "dbdata":dbdata
        }
         return render(request,"adduser.html",data)

def new_save(request):
      
        return render(request,"new_save.html") 
def delete(request,cid):    
         delete_it=MyUser.objects.get(id=cid)
         delete_it.delete()
         messages.success(request," Successfully Deleted")
         return redirect('home')
         


