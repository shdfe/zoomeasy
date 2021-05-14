from flask import render_template, url_for, flash, redirect, jsonify, request
from app import app, db
from sqlalchemy import asc
from app.forms import ClassForm #EmptyForm
from app.models import Zoom
from datetime import datetime
from .util import get_closest, add_time, sort_by_oldest

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ClassForm()
    if form.validate_on_submit():
        zoom = Zoom(class_link=form.class_link.data, class_name=form.class_name.data, start_time=form.start_time.data, done=False)
        db.session.add(zoom)
        db.session.commit()
        flash('Good to go!')
        return redirect(url_for('index'))

        
    return render_template('index.html', form=form)


    
@app.route('/json_class_view', methods=['GET'])
def json_class_view():
    classes = {}
    for one in get_closest(Zoom.query.all()):
        classes[one.class_name] = [
            dict(class_link = one.class_link,
                 start_time = add_time(one.start_time),
                 done=one.done
                 )
        ]
    return jsonify(classes)

@app.route('/done', methods=["GET","POST"])
def done():
    class_name = request.args.get('className', None)
    if class_name:
        the_class = Zoom.query.filter_by(class_name=class_name).first()
        the_class.done = True
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/classes', methods=['GET', 'POST'])
def classes():
    classes = sort_by_oldest(Zoom.query.all())
    if bool(classes) == False:
        flash("No classes found :(")
        # return redirect(url_for('index'))
    return render_template('classes.html', classes=classes)

