from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from todoapp.models import TodoListItem


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',{'all_items':all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/')