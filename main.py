from flask import Flask, render_template, request
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

EVENTS = []

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/create")
def create():
  return render_template("create.html")
  
@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/add", methods=["GET","POST"])
def add():
    # get the data from the form.
  if request.method == "POST":
    name = request.form.get('name')
    email = request.form.get('email')
    ename = request.form.get('event_name')
    where = request.form.get('where')
    date = request.form.get('date')
    oinfo = request.form.get('notes')
    EVENTS.append({'name':name, 'email':email, 'ename':ename, 'where':where, 'date':date, 'date':date, 'oinfo':oinfo})
  return render_template("calender.html",event_list=EVENTS)
  


#---------------------------
if __name__ == "__main__":
  app.run("0.0.0.0")
