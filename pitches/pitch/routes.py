from flask import (render_template, url_for, flash,
                    redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from pitches import db
from pitches.models import Pitch
from pitches.pitch.forms import PitchForm, ReviewsForm

pitchess = Blueprint('pitchess', __name__)


@pitchess.route("/pitch/new", methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_pitch.html', title='New Pitch',
                           form=form, legend='New Pitch')


@pitchess.route('/pitch/review', methods = ['GET', 'POST'])
@login_required
def review():    
    form = ReviewsForm() 
    # reviews = Reviews.query.all()    
    if form.validate_on_submit():       
        new_review = Review(review = form.review.data)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been submitted!', 'success')
        return redirect(url_for('main.review'))
    return render_template('reviews.html', form = form, title = "New Review")

@pitchess.route("/pitch/<int:pitch_id>")
def pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    return render_template('pitch.html', category=pitch.category, pitch=pitch)


@pitchess.route("/pitch/<int:pitch_id>/update", methods=['GET', 'POST'])
@login_required
def update_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if pitch.author != current_user:
        abort(403)
    form = PitchForm()
    if form.validate_on_submit():
        pitch.category = form.category.data
        pitch.content = form.content.data
        db.session.commit()
        flash('Your pitch has been updated!', 'success')
        return redirect(url_for('pitchess.pitch', pitch_id=pitch.id))
    elif request.method == 'GET':
        form.category.data = pitch.category
        form.content.data = pitch.content
    return render_template('create_pitch.html', title='Update Pitch',
                           form=form, legend='Update Pitch')


@pitchess.route("/pitch/<int:pitch_id>/delete", methods=['POST'])
@login_required
def delete_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if pitch.author != current_user:
        abort(403)
    db.session.delete(pitch)
    db.session.commit()
    flash('Your pitch has been deleted!', 'success')
    return redirect(url_for('main.home'))