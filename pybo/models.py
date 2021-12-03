from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=True)

class Answer(db.Model):
    # insert id in column at db
    id = db.Column(db.Integer, primary_key=True)
    # for linking to question_id, CASCADE = delete question following delete answer
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
