from django.shortcuts import redirect, render
from .models import Task, Priority
from django.db import models

priority_order = {
    Priority.HIGH: 0,
    Priority.MEDIUM: 1,
    Priority.LOW: 2
}

# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by(
        models.Case(
            *[models.When(priority=prio, then=val) for prio, val in priority_order.items()]
        )
    )
    
    return render(request, "index.html", {'tasks' : tasks})

def save(request):
    _nome = request.POST.get("name")
    _description = request.POST.get("description")
    _priority = request.POST.get("priority")
    Task.objects.create(name=_nome, description=_description, priority=Priority[_priority])
    return redirect(home)

def update(request, _id):
    _name = request.POST.get("name")
    _description = request.POST.get("description")
    _priority = request.POST.get("priority")
    task = Task.objects.get(id= _id)
    task.name = _name;
    task.description = _description;
    task.priority = Priority[_priority];
    task.save()
    return redirect(home)

def deletar(request, _id):
    Task.objects.get(id=_id).delete()
    return redirect(home)