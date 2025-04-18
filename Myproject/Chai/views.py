from django.shortcuts import render, redirect
from .forms import ReviewForm

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'chai/review_form.html', {'form': form})

def review_success(request):
    return render(request, 'chai/review_success.html')
