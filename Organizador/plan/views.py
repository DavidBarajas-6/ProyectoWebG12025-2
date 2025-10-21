from django.shortcuts import render, redirect
from .forms import PlanForm,MenuFormSet
from django.contrib.auth.models import User  
from .models import Plan 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        plans = Plan.objects.all().order_by('-created_at')
    else:
        plans = Plan.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'plan/index.html', {'plans': plans})

@login_required
def nuevo(request):
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        formset = MenuFormSet(request.POST)

        if plan_form.is_valid() and formset.is_valid():
            plan = plan_form.save(commit=False)
            plan.author = request.user
            plan.save()
            formset.instance = plan
            formset.save()

            return redirect('index')
    else:
        plan_form = PlanForm()
        formset = MenuFormSet()

    return render(request, 'plan/nuevo.html', {
        'form': plan_form,
        'formset': formset
    })

@login_required
def editar(request, post_id):
    plan = Plan.objects.get(id=post_id)

    if request.method == 'POST':
        plan_form = PlanForm(request.POST, instance=plan)
        formset = MenuFormSet(request.POST, instance=plan)

        if plan_form.is_valid() and formset.is_valid():
            plan_form.save()
            formset.save()
            return redirect('index')
        else:
            print("❌ Error en validación:")
            print("Errores en plan_form:", plan_form.errors)
            print("Errores en formset:", formset.errors)
    else:
        plan_form = PlanForm(instance=plan)
        formset = MenuFormSet(instance=plan)

    return render(request, 'plan/editar.html', {
        'form': plan_form,
        'formset': formset,
        'plan': plan
    })


@login_required
def borrar(request, post_id):
    plan = Plan.objects.get(id=post_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('index')
    return render(request, 'plan/borrar.html', {'plan': plan})
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('index') 
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'plan/registro.html', {'form': form})
