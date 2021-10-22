from django.urls import path 
from django.urls import path
from . import views

urlpatterns=[
    

    path('index',views.index,name='index'),
    # path('blog/<str:nombre>',views.blog,name='blog'),
    path('blog',views.blog,name='blog'),
    path('top',views.top,name='top')
]