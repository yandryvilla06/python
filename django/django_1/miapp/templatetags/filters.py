from django import template


register=template.Library()



@register.filter(name='add_apellido')
def add_apellido(nombre):

    return f"<h1>{nombre}</h1>"
