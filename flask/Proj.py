from flask import *
from pymongo import MongoClient
cluster = "mongodb+srv://yogharaj025:l4YBDoBsV0GfO3Ok@cluster0.ljgjax4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster,connect=False)
db = client.Assignment
col = db.Login
col1=db.User_info
col2=db.Fitness_track
col3=db.Trainer_Login
col4=db.Sessions
v=dict()
app = Flask(__name__,template_folder='Frontend-api')


@app.route('/call',methods=['POST'])
def fun3():
    return render_template("New.html")

@app.route('/train',methods=['POST'])
def fun4():
    name = request.form['Name']
    pass1 = request.form['Pass']
    g1=list(col3.find_one({"Username":name,"Password":pass1}))
    if len(g1)==0:
        return "Invalid Username"
    else:
        return render_template("Int8.html")

@app.route('/session',methods=['POST'])
def fun5():
    return render_template("Int9.html")

@app.route('/sesscreate',methods=['POST'])
def fun6():
    Tn=request.form['tn']
    date=request.form['date']
    time=request.form['time']
    v={"Trainee Name":Tn,"Date":date,"Time":time}
    col4.insert_one(v)
    return "<h1>SESSION SUCCESSFULLY CREATED</h1>"

@app.route('/call1/<name>',methods=['POST'])
def fun7(name):
    g=dict(col4.find_one({"Trainee Name":name}))
    if g is None:
        return "<h1>NO SESSIONS</h1>"
    else:
        return render_template("Int10.html",obj=g)


@app.route('/data',methods=['POST'])
def fun2():
    Name=request.form['Name']
    date1=request.form['date']
    push=request.form['push']
    pull=request.form['pull']
    v={"Name":Name,"Date":date1,"Pushups":push,"Pullups":pull}
    col2.insert_one(v)
    return "Done"

@app.route('/', methods=['POST'])
def fun():
    name = request.form['Name']
    pass1 = request.form['Pass']
    g1=list(col.find_one({"Username":name,"Password":pass1}))
    if len(g1)==0:
        return "Invalid Username"
    else:
        g=dict(col1.find_one({"Name":name},{"_id":0,"Password":0}))
        return render_template("Int5.html",obj=g,name1=name)
    

@app.route('/signup',methods=['POST'])
def fun1():
    name=request.form['Name']
    age=request.form['Age']
    gender=request.form['G']
    address=request.form['Add']
    height=request.form['hei']
    weight=request.form['wei']
    level=request.form.get('sel')
    pass1=request.form['pass']
    v1={"Username":name,"Password":pass1}
    v={"Name":name,"Age":age,"Gender":gender,"Address":address,"Height":height,"Weight":weight,"Level":level,"Password":pass1}
    col1.insert_one(v)
    col.insert_one(v1)
    return render_template("Int.html")
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
