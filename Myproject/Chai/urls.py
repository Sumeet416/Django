from django.urls import path
from . import views

urlpatterns = [
    path('submit-review/', views.submit_review, name='submit_review'),
    path('review-success/', views.review_success, name='review_success'),
]
