from django.urls import path 
from django.urls import path
from . import views

urlpatterns=[
    

    path('index',views.index,name='index'),
    # path('blog/<str:nombre>',views.blog,name='blog'),
    path('mesa/blog',views.blog,name='blog'),
    path('top',views.top,name='top'),
    # path('crear_articulo/<str:title>',views.crear_articulo,name='crear_articulo'),
    path('articulo/',views.articulo,name="articulo"),
    path('editar_articulo/<int:id>',views.editar_articulo,name="editar_articulo"),
    path('lista_articulo/',views.lista_articulo,name="lista_articulo"),
    path('borrar_articulo/<int:id>',views.borrar_articulo,name="borrar_articulo"),
    path('save_articulo/',views.save_articulo,name="save"),
    path('crear_articulo/',views.crear_articulo,name='crear_articulo'),
    path('create_full_article/',views.create_full_article , name="create_full_article")
]