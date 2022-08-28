from flask import Blueprint, render_template, request, flash, jsonify
from .models import Charactername, Monster
from . import db
import json
import requests
from DnD.character import Character
from DnD.virtuelDice import roll
import numpy as np

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
			newCharacter = Charactername(charid=charid, name=name, initiative=None)
			db.session.add(newCharacter)
			db.session.commit()
			flash("Character added!", category="success")

	chars = Charactername.query.all()

	return render_template('home.html', chars=chars)

@views.route('/dm', methods=["GET", "POST"])
def dm():
	if request.method == "POST":
		monsterIndex = request.form.get("monsterindex")
		if monsterIndex:
			monsterJson = requests.get(f"https://www.dnd5eapi.co/api/monsters/{monsterIndex}/").json()
			if monsterJson.get("error") != "Not found":
				newMonster = Monster(name=monsterJson.get("name"),
									initiative=int(roll(1, 20)[1] + ((int(monsterJson.get("dexterity")) - 10) // 2)),
									HPmax=int(monsterJson.get("hit_points")),
									HPcurrent=int(monsterJson.get("hit_points"))
									)
				db.session.add(newMonster)
				db.session.commit()
				flash("Monster added!", category="success")
			else:
				flash("Invalid monster index", category="error")

		reqHPUp = request.form.get("HPchange")
		if reqHPUp:
			req = request.form["HP"]
			upDown = req[0]
			id = req[1:]
			if upDown == "U":
				mon = Monster.query.filter_by(id=id).first()
				mon.HPcurrent += int(reqHPUp)
				db.session.commit()
			elif upDown == "D":
				mon = Monster.query.filter_by(id=id).first()
				mon.HPcurrent -= int(reqHPUp)
				db.session.commit()

	chars = Charactername.query.all()
	mons = Monster.query.all()

	charsMons = chars + mons
	unsortedInitiatives = []
	for idx, item in enumerate(charsMons):
		if item.initiative is not None:
			unsortedInitiatives.append(item.initiative)
		else:
			unsortedInitiatives.append(-99)
	#print(unsortedInitiatives)
	#if len(unsortedInitiatives) > 0:
	#	unsortedInitiatives[unsortedInitiatives == None] = 0
	sortedInitiatives = np.argsort(unsortedInitiatives)[::-1]
	#print(sortedInitiatives)
	#charsMons = [x for _, x in sorted(zip(sortedInitiatives, charsMons))[::-1]]

	charsMonsSorted = []
	for item in sortedInitiatives:
		charsMonsSorted.append(charsMons[item])

	isMonster = []

	for idx, item in enumerate(charsMonsSorted):
		try:
			item.charid
			isMonster.append(0)
		except:
			isMonster.append(1)
	
	# find all monster - for add monster menu
	allMonsters = requests.get(f"https://www.dnd5eapi.co/api/monsters/").json().get("results")

	return render_template('dm.html', chars=chars, charsMons=charsMonsSorted, isMonster=isMonster, allMonsters=allMonsters)

@views.route('/player/<int:charId>/<state>', methods=['GET', 'POST'])    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def player(charId, state):
	values = (None, None)
	if request.method == "POST":
		if request.form.get("20") is not None:
			values = (roll(1, 20)[1], int(request.form.get("20")))
		elif request.form.get("1d4") is not None:
			values = (roll(1, 4)[1], int(request.form.get("1d4")))
		elif request.form.get("initiative") is not None:
			values = (roll(1, 20)[1], int(request.form.get("initiative")))
			char = Charactername.query.filter_by(charid=charId).first()
			char.initiative = int(sum(values))
			db.session.commit()

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

@views.route('/deleteMonster-id', methods=['POST'])
def deleteMonster_id():
    mon = json.loads(request.data)
    monId = mon['id']
    mon = Monster.query.get(monId)
    if mon:
        db.session.delete(mon)
        db.session.commit()

    return jsonify({})