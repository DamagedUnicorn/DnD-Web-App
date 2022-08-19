from flask import Blueprint, render_template, request, flash, jsonify
from .models import Charactername
from . import db
import json
import requests
from DnD.character import Character
from DnD.virtuelDice import roll

# https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		charid = request.form.get("charid")

		name = requests.get("https://character-service.dndbeyond.com/character/v3/character/" + str(charid)).json().get("data").get("name")
		chars = Charactername.query.filter_by(charid=charid).first()

		if not name:
			flash("Invalid character ID", category="error")
		elif chars:
			flash("Character already added", category="error")
		else:
			newCharacter = Charactername(charid=charid, name=name)
			db.session.add(newCharacter)
			db.session.commit()
			flash("Character added!", category="success")

	chars = Charactername.query.all()

	return render_template('home.html', chars=chars)

@views.route('/dm')
def dm():
	chars = Charactername.query.all()
	return render_template('dm.html', chars=chars)

#@views.route('/player')
#def player():
#	chars = Charactername.query.all()
#	return render_template('player.html', chars=chars)

@views.route('/player/<int:charId>/<state>', methods=['GET', 'POST'])    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def player(charId, state):
	values = (None, None)
	if request.method == "POST":
		values = (roll(1, 20)[1], int(request.form.get("abilityCheck")))
	character = Character(charId)
	chars = Charactername.query.all()
	return render_template('player.html', character=character, chars=chars, state=state, values=values)


@views.route('/delete-id', methods=['POST'])
def delete_id():
    char = json.loads(request.data)
    charId = char['charId']
    char = Charactername.query.get(charId)
    if char:
        db.session.delete(char)
        db.session.commit()

    return jsonify({})
