from django.shortcuts import render

tasks = []

# Create your views here.
def index(request):
    """ 
    Handle GET Requests in index Function:
        Add a conditional check for the request method.
        If the method is "GET", use `render` function to render "index.html" and pass the tasks list as a variable.
    """
    # TODO
    
    """
    Handle POST Requests in index Function for Adding Tasks:
        Still in the index function, add an else block to handle POST requests.
        Retrieve the task from the form data using request.POST["new_task"].
        Append the retrieved task to the tasks list.
        Finally, use `render` function to render "index.html" and pass the tasks list as a variable.
    """
    # TODO
    return render(request, "tasks/index.html")

def remove(request):
    """
    Handle POST Requests in remove Function:
        In the remove function, add code to handle POST requests.
        Retrieve the task to be removed from the form data using request.POST["task"].
        Remove the specified task from the tasks list using tasks.remove(task).
        Finally, use `render` function to render "index.html" and pass the tasks list as a variable.
    """
    # TODO
