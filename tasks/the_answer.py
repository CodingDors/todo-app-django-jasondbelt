from django.shortcuts import render

tasks = []

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "tasks/index.html", {
            "tasks": tasks
        })
    else:
        new_task = request.POST["new_task"]
        tasks.append(new_task)
        return render(request, "tasks/index.html", {
            "tasks": tasks
        }) 

def remove(request):
    if request.method == "POST":
        task = request.POST["task"]
        tasks.remove(task)
        return render(request, "tasks/index.html", {
            "tasks": tasks
        })
