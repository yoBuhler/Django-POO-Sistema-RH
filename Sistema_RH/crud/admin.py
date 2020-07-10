from django.contrib import admin
from crud.models import Funcionario
from crud.models import Setor

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Setor)
