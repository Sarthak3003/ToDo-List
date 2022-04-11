from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

#showing ordered list
def index(request):
    todo_list = Todo.objects.order_by('id')                     #creates ordered list
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form}          #passes context to index.html
    return render(request, 'todo/index.html', context)

@require_POST                                                   #only accepts POST requests
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request, todo_id):                             #manage completed tasks ;)
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):                                   #this is to manage deleted task
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):                                         #when you want to delete all task 
    Todo.objects.all().delete()

    return redirect('index')