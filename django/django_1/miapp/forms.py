from django import forms
from django.forms.widgets import Textarea
from django.core import validators


class FormArticle(forms.Form):
  
     title=forms.CharField(
         
         label='Titulo',
         max_length=20,
         required=True,

        validators=[
            
                validators.MinLengthValidator(4,'el titulo es demasiado corto')

            ]

     )

    

     content=forms.CharField(
       
        label='content',
        widget=forms.Textarea

    )

     public_options=[

        (1,'si'),
        (2,'no')
     ]

     public=forms.TypedChoiceField(
         
         label='publicado?',
         choices=public_options
 

     )


     


