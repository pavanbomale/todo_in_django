from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
        
        todo_obj = Todo.objects.create(title=title, desc=desc)
        todo_obj.save()
    return render(request, 'index.html')

def mytodos(request):
    data = Todo.objects.all()

    p = Paginator(data, 5)
    page = request.GET.get('page')
    finaldata = p.get_page(page)

    if request.method == 'POST':
        q = request.POST['q']
        if not q == '':
            multiple_q = Q(Q(title__icontains=q))
            finaldata = Todo.objects.filter(multiple_q)

    return render(request, 'mytodos.html', {'data':finaldata})
       

def delete(request, id):
    flag = Todo.objects.filter(id=id).exists()
    if flag:
        todo_obj = Todo.objects.get(id=id)
        todo_obj.delete()

    data = Todo.objects.all()
    p = Paginator(data, 5)
    page = request.GET.get('page')
    finaldata = p.get_page(page)
    return render(request, 'mytodos.html', {'data':finaldata})


def edit(request, *args, **kwargs):
    id = kwargs['id']
    if request.method == 'POST':
        title = request.POST['edit_title']
        desc = request.POST['edit_description']
        todo_obj = Todo.objects.get(id= id)
        todo_obj.title=title
        todo_obj.desc=desc
        todo_obj.save()
        return redirect(mytodos)
    todo_obj=[Todo.objects.get(id=id)]
    return render(request, 'mytodos.html', {'todo_obj':todo_obj})