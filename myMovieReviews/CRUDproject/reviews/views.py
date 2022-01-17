from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

def show_list(request, order=None):
    if order == None:
        reviews = Review.objects.all()
    elif order == "h-rating":
        reviews = Review.objects.all().order_by("-rating")
    elif order == "l-rating":
        reviews = Review.objects.all().order_by("rating")
    elif order == "latest":
        reviews = Review.objects.all().order_by("-created_at")
    elif order == "l-runtime":
        reviews = Review.objects.all().order_by("-running_time")
    elif order == "s-runtime":
        reviews = Review.objects.all().order_by("running_time")   
    else:
        return redirect("/")       
    ctx = {"reviews":reviews}
    return render(request, template_name="reviews/list.html", context=ctx)

def write_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ReviewForm()
        ctx = {"form":form}
        return render(request, template_name="reviews/write.html", context=ctx)

def show_detail(request, pk):
    review = get_object_or_404(Review, id=pk)
    ctx = {"review":review}
    return render(request, template_name="reviews/detail.html", context=ctx)

def update_review(request, pk):
    review = get_object_or_404(Review, id=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid():
            form.save()
        return redirect("reviews:detail", pk)
    else:
        form = ReviewForm(instance = review)
        ctx = {"form":form, "pk":pk}
        return render(request, template_name="reviews/write.html", context=ctx)

def delete_review(request, pk):
    review = get_object_or_404(Review, id=pk)
    review.delete()
    return redirect("/")