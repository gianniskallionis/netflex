from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_pymongo import PyMongo
from flask_cors import CORS
import numpy as np
from bson.objectid import ObjectId

app=Flask(__name__)
CORS(app)

 # connecting database with flask 
app.config["MONGO_URI"]="mongodb://localhost:27017/netflex"
mongo= PyMongo(app)

@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/items')
def items():
   return render_template('items.html')

@app.route ('/like',methods=['POST'])
def like():
   data = request.get_json()
   id = data["id"]
   mongo.db.athletes.update_one({"_id": ObjectId(id)},{"$inc": {"likes": 1}})
   return jsonify({"message": "Liked!"})

@app.route('/search')    
def search():
   nameSearched=request.args.get("name","")  #an den valei name, epistrefei empty string, dld to ""
   query={"name": {"$regex":nameSearched,"$options":"i"}}
   results=mongo.db.athletes.find(query).sort("price",-1)
   clean_results=[]
   for athlete in results:
      athlete['_id']=str(athlete['_id'])
      clean_results.append(athlete)
   return jsonify(clean_results)

# to $regex psaxnei na vrei an mia akolouthia p exei grapsei o allos yparxei se kapoio name
# an grapseis gi sou vriskei to giannis ( gi is in giannis)
#to "$options": "i" . to option shmainei rythmiseis kai to i shmainei case Insensitive
# ara mikra kai kefalaia ola sto idio saki 
# to id tou athlete to kanume string gt to _id ths mongodb einai special object pou den to diavazei h py3
#shoutout thano an to diavazeis auto 


 # /popular: Αναπτύξτε ένα GET request που θα επιστρέφει μία λίστα με τα top-5 πιο
#δημοφιλή προϊόντα με βάση των αριθμό των Likes.
@app.route('/popular') 
def get5MostPopular():
   results = mongo.db.athletes.find().sort("likes", -1).limit(5)
   clean_results = []
   for athlete in results:
      athlete['_id'] = str(athlete['_id'])  #kanw to object id string gia na borei na to diavasei h python
      clean_results.append(athlete)
   return jsonify(clean_results)
   # to find ta fernei ola, to sort likes-1 krataei ta top me likes apo max pros min
   #to limit 5 krataei ta 5 max likes, to list ta kanei lista kai to jsonify ta kanei json
   
if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)