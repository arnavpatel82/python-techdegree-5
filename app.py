from flask import render_template, url_for, request, redirect
from models import db, Project, app, datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/project/<id>')
def project(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    skill_list = project.skills.split(', ')
    return render_template('detail.html', project=project, projects=projects, skill_list=skill_list)


@app.route('/add-project', methods=['GET', 'POST'])
def add_project():
    projects = Project.query.all()
    if request.form:
        form_date = request.form['date']
        add_date = datetime.strptime(form_date, '%Y-%m')
        new_project = Project(title=request.form['title'], date=add_date, description=request.form['desc'], skills=request.form['skills'], github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/edit-project/<id>', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    if request.form:
        form_date = request.form['date']
        edit_date = datetime.strptime(form_date, '%Y-%m')

        project.title = request.form['title']
        project.date = edit_date
        project.description = request.form['desc']
        project.skills = request.form['skills']              
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project, projects=projects)


@app.route('/delete/<id>')
def delete_project(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')