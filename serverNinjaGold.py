from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key ="secret"

#def winGold(gold, location):
	#time = time.time()
	#message = "You earned %d at the %s"(gold, location)
	#session["message"].append(message)
	

@app.route('/')
def index():
	if 'gold' not in session:
		session["gold"] = 0
	if 'message' not in session:
		session["message"] = []

	return render_template("index.html")

@app.route('/process', methods=['post'])

def process():
	if request.form["building"] =="farm":
		randnum = random.randint(10, 20)
		session['gold']+=randnum
		session["message"].append('You earned ' + str(randnum) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))

	if request.form["building"] =="cave":
		randnum = random.randint(5, 10)
		session['gold']+=randnum
		session["message"].append('You earned ' + str(randnum) + ' gold from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))

	if request.form["building"] =="house":
		randnum = random.randint(2, 5)
		session['gold']+=randnum
		session["message"].append('You earned ' + str(randnum) + ' gold from the house!(' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))

	if request.form["building"] =="casino":
		winLose = random.randint(0, 1)
		if winLose == 0:
			winGold = random.randint(0, 50)
			session['gold'] += winGold
			session["message"].append('You earned ' + str(randnum) + ' gold from the casino! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
		elif winLose == 1:
			loseGold = random.randint(-50, 0)
			session['gold']+= loseGold
			session["message"].append('You lost ' + str(randnum) + ' gold from the casino! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
	
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)