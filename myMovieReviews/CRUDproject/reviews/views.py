from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

def show_list(request):
    reviews = Review.objects.all()   
    ctx = {"reviews":reviews}
    return render(request, template_name="reviews/list.html", context=ctx)

def show_ordered_list(request, pk):
    if pk == 4:
        return redirect("/")
    elif pk == 1:
        reviews = Review.objects.all().order_by("-rating")
    elif pk == 2:
        reviews = Review.objects.all().order_by("rating")
    elif pk == 3:
        reviews = Review.objects.all().order_by("-created_at") 
    elif pk == 5:
        reviews = Review.objects.all().order_by("-running_time")
    elif pk == 6:
        reviews = Review.objects.all().order_by("running_time")    
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