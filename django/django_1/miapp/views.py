from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.


layout=""" 
   <h1>MIAPP</h1>
   <ul>
      <li><a href="blog">Inicicio</a></li>
   </ul>

"""

def index(request):
    #layout concatenado en return
    # return HttpResponse(f"Hola")

    return render(request,'index.html')

def blog(request):
     return render(request,'blog.html')   
    
def top(request):

     return render(request,'top.html')
