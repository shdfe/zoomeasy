from flask import render_template, url_for, flash, redirect, jsonify
from app import app, db
from sqlalchemy import asc
from app.forms import ClassForm #EmptyForm
from app.models import Zoom
from datetime import datetime
from .util import get_closest

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ClassForm()
    if form.validate_on_submit():
        zoom = Zoom(class_link=form.class_link.data, class_name=form.class_name.data, start_time=form.start_time.data)
        db.session.add(zoom)
        db.session.commit()
        flash('Good to go!')
        return redirect(url_for('index'))
    
        #classes = Zoom.query.all() 
            #w = Zoom.query.filter_by(class_time = current_time + 5min)

        #while classes length !=0:
            #w = Zoom.query.filter_by(class_time = current_time + 5min)
            #if w.first() is none:
                #if hour == curr_hour and zoom table.time.desc()[0].minutes % 10 == 0:
                    #set timeout for (curr_min-5)*60 seconds? time sleep
            #else:
                #do the go() function
        
    return render_template('index.html', form=form)

# @app.route('/wait', methods=['GET', 'POST'])
# def wait():
#     classes = Zoom.query.all()
#     if classes:
        
#     flash("No Classes :(")
    
@app.route('/json_class_view', methods=['GET'])
def json_class_view():
    classes = {}
    for one in get_closest(Zoom.query.all()):
        classes[one.class_name] = [
            dict(class_link = one.class_link,
                 start_time = one.start_time
                 )
        ]
    return jsonify(classes)

@app.route('/classes', methods=['GET', 'POST'])
def classes():
    classes = get_closest(Zoom.query.all())
    if bool(classes) == False:
        flash("No classes found :(")
        # return redirect(url_for('index'))
    return render_template('classes.html', classes=classes)


    

# @app.route('/delete/<id>')
# def delete(id):
#     one = Zoom.query.filter_by(id=int(id)).first()
#     db.session.delete(one)
#     db.session.commit()
#     return redirect(url_for('index'))