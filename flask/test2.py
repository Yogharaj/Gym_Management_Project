from pymongo import MongoClient
from flask import *
cluster = "mongodb+srv://yogharaj025:5SdfbqKSkn1ntWK9@cluster0.ljgjax4.mongodb.net/test"

client = MongoClient(cluster)

print(client.list_database_names())

db = client.Assignment_2

print(db.list_collection_names())
app=Flask(__name__)
@app.route('/',methods=['POST'])
def fun():
    name=request.form['Name']
    return "Hello from flask %s"%name
if __name__=="__main__":
    app.run(debug=True)
