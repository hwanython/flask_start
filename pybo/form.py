from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('뭐라도 쓰십시오.')])

class Answerform(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired("내용은 필수라고요,,")])