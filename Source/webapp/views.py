from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.models import ToDoList


# Create your views here.

def todolist_view(request):
    todolist = ToDoList.objects.order_by("-updated_at")
    context = {"todolist": todolist}
    return render(request, "todolist.html", context)


def todolist_detail(request):
    todolist_id = request.GET.get("id")
    todolist = ToDoList.objects.get(id=todolist_id)
    return render(request, "detail.html", {"todolist": todolist})


def todolist_delete(request):
    todo_id = request.GET.get('id')
    todolist = ToDoList.objects.get(id=todo_id)
    todolist.delete()
    return HttpResponseRedirect("/")


def todolist_create(request):
    if request.method == "GET":
        return render(request, "create.html")
    if request.method == 'POST':
        ToDoList.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            time=request.POST.get('time'),
            created_at=request.POST.get('created_at'),
            updated_at=request.POST.get('update_at')
        )
        return HttpResponseRedirect("/")
