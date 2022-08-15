from flask import Blueprint, render_template, request, flash, jsonify
from .models import Charactername
from . import db
import json
import requests

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		charid = request.form.get("charid")

		name = requests.get("https://character-service.dndbeyond.com/character/v3/character/" + str(charid)).json().get("data").get("name")

		newCharacter = Charactername(charid=charid, name=name)
		db.session.add(newCharacter)
		db.session.commit()
		flash("Character added!")

	chars = Charactername.query.all()

	return render_template('home.html', chars=chars)

@views.route('/dm')
def dm():
	return render_template('dm.html')

@views.route('/player')
def player():
	return render_template('player.html')

@views.route('/delete-id', methods=['POST'])
def delete_id():
    char = json.loads(request.data)
    charId = char['charId']
    char = Charactername.query.get(charId)
    if char:
        db.session.delete(char)
        db.session.commit()

    return jsonify({})
