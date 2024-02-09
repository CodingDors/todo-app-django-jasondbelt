# ToDo App Exercise - Django
Welcome to the ToDo App Exercise with Django! In this assignment, you'll create a basic ToDo application using Django.

This exercise is designed to be straightforward, where you'll need to work only on the `tasks/views.py`. Your goal is to make the page built in `tasks/templates/tasks/index.html` to bring the ToDo application to life.

## 🎯 Objective:
Your task is to create a simple ToDo application that allows a user to:
- Enter a task using a form.
- View the entered task appended to an unordered list on the page.
- Remove the task they want to delete (by clicking in a individual button for each item)

You'll only write in the `tasks/views.py` file. In case you need to see the solution, it is at `tasks/the_answer.py`.

## 📚 Starter Code
The HTML code consists of two primary components:

1. **Task Display List**
   - **List Container**: Uses a `<ul>` element to create an unordered list. Each task in the application is represented as an individual list item (`<li>`) within this container.
   - **Dynamic Task Listing**: The `{% for task in todo %}` loop dynamically populates the list with tasks. For each task, it creates a list item (`<li>`) displaying the task content.
   - **Remove Button**: Each task has an associated form with a "Remove" button. This form submits a POST request to the `/remove` route, indicating the task to be removed. The task to be removed is passed as a hidden field in the form.

2. **Task Input Form**
   - **Form Element**: A separate `<form>` tag at the bottom of the page, designated for adding new tasks. This form submits to the root route (`"/"`) as a POST request.
   - **Task Input Field**: An `<input>` element of the type text, allowing users to input a new task. It includes a placeholder text "Add Task" to guide users.
   - **Submit Button**: A submit button within the form, enabling users to submit the new task. Upon submission, the task is sent to the server and is expected to be added to the task list.

## ✅ Specific Tasks:
You will be responsible for the following in `tasks/views.py`:
1. **Handle GET Requests in index Function:**
  - Inside the index function, add a conditional check for the request method.
  - If the method is `"GET"`, use `render` function to render `"index.html"` and pass the `tasks` list as a variable.

2. **Handle POST Requests in index Function for Adding Tasks:**
  - Still in the index function, add an `else` block to handle `POST` requests.
  - Retrieve the task from the form data using `request.POST["new_task"]`.
  - Append the retrieved task to the `tasks` list.
  - Finally, use `render` function to render `"index.html"` and pass the `tasks` list as a variable.

3. **Handle POST Requests in remove Function:**
  - In the remove function, add code to handle `POST` requests.
  - Retrieve the task to be removed from the form data using `request.POST["task"]`.
  - Remove the specified task from the tasks list using `todo.remove(task)`.
  - Use `render` function to render `"index.html"` and pass the `tasks` list as a variable.

## Sample Solutions:
  If you're stuck or would like to compare your implementation with our version, check the `tasks/the_answer.py` for the view logic.

## 📘 How to Run Your Website:
1. Install the required packages: `pip install -r requirements.txt`
2. Start the Django development server: `python manage.py runserver`
3. Access the application via your web browser at the URL provided by the terminal

## 🚀 How to Run Tests:
To make sure your application is working as expected:

1. Stop the server if it's still running (you can use Ctrl+C in the terminal for that).
2. In your terminal, run the following command: `python manage.py test`

## 🤔 How to Submit:
Once all the tests have completed:
1. Stage Changes:
  - View your changes in the Source Control view.
  - Click on the + (plus) sign next to the files you wish to stage.
2. Commit Changes:
  - Enter a descriptive commit message.
  - Press Ctrl + Enter (or Cmd + Enter on macOS) to commit the changes.
3. Push Changes:
  - Click on the ellipsis ... in the Source Control view.
  - Select Push.
4.Verify you code has passed

How the Project will Look Like
![Local Image](project.png)
