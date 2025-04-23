from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Jobs

def job(request):
    jobs_list = Jobs.objects.all()
    form = ApplicationForm()
    return render(request, 'jobs.html', {'jobs': jobs_list, 'form': form})

def job_apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Jobs')
    else:
        form = ApplicationForm()
    jobs_list = Jobs.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs_list, 'form': form})
