from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ToDoList


# Create your views here.

def todolist_view(request):
    todolist = ToDoList.objects.order_by("-updated_at")
    context = {"todolist": todolist}
    return render(request, "todolist.html", context)


def todolist_detail(request, *args, **kwargs):
    pk = kwargs.get('pk')
    todolist = ToDoList.objects.get(id=pk)
    return render(request, "detail.html", {"todolist": todolist})


def todolist_delete(request, pk):
    todolist = get_object_or_404(ToDoList, id=pk)
    todolist.delete()
    return redirect('todolist')


def todolist_create(request):
    if request.method == "GET":
        return render(request, "create.html")
    if request.method == 'POST':
        todolist = ToDoList.objects.create(
            description=request.POST.get('description'),
            detailed_description=request.POST.get('detailed_description'),
            status=request.POST.get('status'),
            time=request.POST.get('time'),
            created_at=request.POST.get('created_at'),
            updated_at=request.POST.get('update_at')
        )
        return redirect('todolist')
