from django.http import HttpResponse
from django.shortcuts import redirect, render
from miapp.models import Article,Category
from miapp.forms import FormArticle


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
    nombre='pepe'
    idiomas=["español","ingles","mandarin","japones"]
    return render(request,'index.html',{'variable':"BY YANDRY",'nombre':nombre,'idiomas':idiomas})

def blog(request):
     return render(request,'blog.html')   
    
def top(request):

     return render(request,'top.html')

# def crear_articulo(request,title):

#    articulo=Article(

#       title=title,
#       content='Contenido del articulo',
#       public=True
#    )
#    articulo.save()
#    return HttpResponse("Usuario creado: ")

def articulo(request):
   
   articulo=Article.objects.get(id=2)
     
   return HttpResponse(f"Articulo :{articulo.title} ")

def editar_articulo(request,id):

   articulo=Article.objects.get(pk=id)

   articulo.title="Batman"
   articulo.content="Pelicula del 2017"
   articulo.public=True

   articulo.save()

   return HttpResponse(f"Articulo name  :{articulo.title} Content:{articulo.content} Public:{articulo.public}")


def lista_articulo(request):

   articulos=Article.objects.all()

   return render(request,'articulos.html',{

      'articulos':articulos 
     
   })

def borrar_articulo(request,id):
   
    articulos=Article.objects.get(pk=id)
    articulos.delete()
    return redirect('lista_articulo')

def save_articulo(request):
   if request.method=='POST':

      title=request.POST['title'],
      content=request.POST['content'],
      public=request.POST['public']
     
      
      articulo=Article(

          title=title,
          content=content,
          public=public
      )
     
      articulo.save()
         
      return HttpResponse("<h2> articulo CREADO</h2>")


   else:

      return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

def crear_articulo(request):
  
  return render(request,'crear_articulo.html')


def create_full_article(request):

   if request.method=='POST':

      formulario=FormArticle(request.POST)

      if formulario.is_valid():

         data_form=formulario.cleaned_data

         title=request.POST['title'],
         content=request.POST['content'],
         public=request.POST['public']

         articulo=Article(

          title=title,
          content=content,
          public=public
         )
     
         articulo.save()
        
         return redirect('lista_articulo')

   else:

       formulario=FormArticle()

   return render(request,'create_full_article.html',{
        
         'form':formulario

   })
