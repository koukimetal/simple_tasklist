from flask import Flask, request

from webapp.model import Task
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(loader=PackageLoader('webapp', 'templates'))


@app.route('/', methods=['GET'])
def show_tasks():
    tasks = Task.objects
    template = env.get_template('tasks.html')
    return template.render(tasks=tasks)


@app.route('/', methods=['POST'])
def edit_tasks():
    name = request.form['name']
    action = request.form['action']
    if action == 'ADD':
        Task(name).save()
    return show_tasks()

if __name__ == '__main__':
    import pydevd
    pydevd.settrace('172.30.254.1', port=5678, stdoutToServer=True, stderrToServer=True)

    app.run(host='0.0.0.0')
