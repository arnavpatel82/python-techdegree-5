from flask import render_template, url_for, request
from models import db, Project, app


@app.route('/')
def index():
    # projects = Project.query.all()
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detail')
def project():
    return render_template('detail.html')


@app.route('/add-project')
def add_project():
    return render_template('projectform.html')

# @app.route('/projects/new', methods=['GET', 'POST'])
# def add_project():
#     print(request.form)
#     print(request.form['title'])
#     return render_template('projectform.html')

# @app.route('/projects/<id>')
# def project(id):
#     project = Project.query.get(id)
#     return render_template('detail.html', project=project)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')