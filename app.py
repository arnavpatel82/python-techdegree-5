from flask import render_template, url_for, request, redirect
from models import db, Project, app, datetime


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


@app.route('/add-project', methods=['GET', 'POST'])
def add_project():
    if request.form:
        form_date = request.form['date']
        add_date = datetime.strptime(form_date, '%Y-%m')
        new_project = Project(title=request.form['title'], date=add_date, description=request.form['desc'], skills=request.form['skills'], github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('projectform.html')


# @app.route('/projects/<id>')
# def project(id):
#     project = Project.query.get(id)
#     return render_template('detail.html', project=project)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')