from django.contrib import admin

from .models import Produto, Cliente, Fornecedore, Venda, Funcionário, Marca

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Fornecedore)
admin.site.register(Venda)
admin.site.register(Funcionário)
admin.site.register(Marca)







