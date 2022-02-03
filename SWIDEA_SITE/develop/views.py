from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def list_idea(request):
    objects = Idea.objects.all()   
    return render(request, "develop/list.html", {"objects":objects, "idea_yes":True})

def show_idea(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    return render(request, "develop/show.html", {"idea":idea, "idea_yes":True})

def create_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect("develop:show_idea", instance.id)
    else:
        form = IdeaForm()
        return render(request, "develop/form_idea.html", {"form":form})

def edit_idea(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
        return redirect("develop:show_idea", pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {"form":form, "pk":pk}
        return render(request, template_name="develop/form_idea.html", context=ctx)

def delete_idea(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    idea.delete()
    return redirect("/")

def list_tool(request):
    objects = Tool.objects.all()
    return render(request, "develop/list.html", {"objects":objects})

def show_tool(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    return render(request, "develop/show.html", {"tool":tool})

def create_tool(request):
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("develop:show_tool", instance.id)
    else:
        form = ToolForm()
        return render(request, "develop/form_tool.html", {"form":form})

def edit_tool(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    if request.method == "POST":
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
        return redirect("develop:show_tool", pk)
    else:
        form = ToolForm(instance=tool)
        ctx = {"form":form, "pk":pk}
        return render(request, template_name="develop/form_tool.html", context=ctx)

def delete_tool(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    tool.delete()
    return redirect("develop:list_tool")

@csrf_exempt
def edit_interest(request):
    req = json.loads(request.body)
    idea_id = req["id"]
    btn_type = req["type"]
    idea = get_object_or_404(Idea, id=idea_id)

    if btn_type == "plus":
        idea.interest += 1
    else:
        idea.interest -= 1
    idea.save()

    return JsonResponse({"id":idea_id, "type":btn_type})