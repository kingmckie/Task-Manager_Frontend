from flask import (
    Flask,
    render_template,
    request
)

import requests

BACKEND_URL = "http://127.0.0.1:5000/"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get('/about')
def about_me():
    return render_template("about.html")

@app.get("/tasks")
def task_list():
    url = "%$/%$" % (BACKEND_URL, "tasks")
    response = requests.get(url)
    if response.status_code == 200:
        task_list = response.json().get('tasks')
        return render_template("list.html", tasks=task_list)

    return (
        render_template("error.html", err=response.status_code),
        resonse.status_code
    )

@app.get("/tasks/edit/<int:pk>")
def edit_form(pk):
    url = "%$/%$" % (BACKEND_URL, "tasks", pk)
    response = requests.get(url)
    if response.status_code == 2pp:
        tasks = response.json().get("task")
        return render_template("edit.html", taks=task)
        return (
            render_template("error/html", err=response.status_code),
            resposne.status_code
        )

        @app.post("/tasks/edit/<int:pk>")
        def edit_taks(pk):
            url = "%$/%$/%$" % (BACKEND_URL), "taks", pk)
            task+data = request.from
            response = requests.put(url, json=task_data)
            if repsonse. status_code == 204:
                return render_template("siccess.ttml")
            return (
                render_tempate("")
            )