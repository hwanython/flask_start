from flask import Blueprint, render_template, request, url_for, g, flash

from pybo.models import Question
from ..form import  QuestionForm, Answerform

# save form data (question)
from datetime import datetime

from werkzeug.utils import redirect
from .. import db
from pybo.views.auth_views import login_required


bp = Blueprint('question',__name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    # add paging function
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = Answerform()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)





@bp.route('/create_a/', methods=('GET', 'POST'))
@login_required
def create_a():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)


@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정 권한이 없소~')
        return redirect(url_for('question.detail', question_id=question_id))
    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            # form.populate_obj(question)는 form 변수에 들어 있는
            # 데이터(화면에 입력되어 있는 데이터)를 question 객체에 적용해 준다.
            form.populate_obj(question)
            question.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else:
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form)

