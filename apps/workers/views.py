from django.shortcuts import render, get_object_or_404, redirect
from .forms import WorkerForm
from .models import Worker

# Create your views here.
def add_worker(request):
    template_name = 'workers/add_worker.html'
    context = {}
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('workers:list_workers')
    form = WorkerForm()
    context['form'] = form
    return render(request, template_name, context)

def list_workers(request):
    template_name = 'workers/list_workers.html'
    workers = Worker.objects.filter()
    context = {
        'workers': workers
    }
    return render(request, template_name, context)

def edit_worker(request, id_worker):
    template_name = 'workers/add_worker.html'
    context ={}
    worker = get_object_or_404(Worker, id=id_worker)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('workers:list_workers')
    form = WorkerForm(instance=worker)
    context['form'] = form
    return render(request, template_name, context)

def delete_worker(request, id_worker):
    worker = Worker.objects.get(id=id_worker)
    worker.delete()
    return redirect('workers:list_workers')