from . import db


class Charactername(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charid = db.Column(db.Integer)
    name = db.Column(db.String(50))
    initiative = db.Column(db.Integer)
    passivePerception = db.Column(db.Integer)
    passiveInvestigation = db.Column(db.Integer)
    passiveInsight = db.Column(db.Integer)


class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    initiative = db.Column(db.Integer)
    HPmax = db.Column(db.Integer)
    HPcurrent = db.Column(db.Integer)
