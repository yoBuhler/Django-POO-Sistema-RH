from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Funcionario
from crud.models import Setor

# Funcionario

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sexo', 'data_nascimento', 'setor']

def funcionario_list(request, template_name='funcionario/funcionario_list.html'):
    funcionario = Funcionario.objects.all()
    data = {}
    data['object_list'] = funcionario
    return render(request, template_name, data)

def funcionario_view(request, pk, template_name='funcionario/funcionario_detail.html'):
    funcionario= get_object_or_404(Funcionario, pk=pk)    
    return render(request, template_name, {'object':funcionario})

def funcionario_create(request, template_name='funcionario/funcionario_form.html'):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('funcionario_list')
    return render(request, template_name, {'form':form})

def funcionario_update(request, pk, template_name='funcionario/funcionario_form.html'):
    funcionario= get_object_or_404(Funcionario, pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('funcionario_list')
    return render(request, template_name, {'form':form})

def funcionario_delete(request, pk, template_name='funcionario/funcionario_confirm_delete.html'):
    funcionario= get_object_or_404(Funcionario, pk=pk)    
    if request.method=='POST':
        funcionario.delete()
        return redirect('funcionario_list')
    return render(request, template_name, {'object':funcionario})

# Setor

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'pausa_cafe']

def setor_list(request, template_name='setor/setor_list.html'):
    setor = Setor.objects.all()
    data = {}
    data['object_list'] = setor
    return render(request, template_name, data)

def setor_view(request, pk, template_name='setor/setor_detail.html'):
    setor= get_object_or_404(Setor, pk=pk)    
    return render(request, template_name, {'object':setor})

def setor_create(request, template_name='setor/setor_form.html'):
    form = SetorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('setor_list')
    return render(request, template_name, {'form':form})

def setor_update(request, pk, template_name='setor/setor_form.html'):
    setor= get_object_or_404(Setor, pk=pk)
    form = SetorForm(request.POST or None, instance=setor)
    if form.is_valid():
        form.save()
        return redirect('setor_list')
    return render(request, template_name, {'form':form})

def setor_delete(request, pk, template_name='setor/setor_confirm_delete.html'):
    setor= get_object_or_404(Setor, pk=pk)    
    if request.method=='POST':
        setor.delete()
        return redirect('setor_list')
    return render(request, template_name, {'object':setor})