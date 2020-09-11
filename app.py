import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'smells_good'
app.config["MONGO_URI"] = 'mongodb+srv://sam_mckenna:YnNPIkpu2VIdHiqT@cluster0.wptnw.mongodb.net/smells_good?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')

@app.route('/recipe')
def recipe():
    data = mongo.db.recipes.find()
    return render_template("recipe.html", page_title="Recipe", company=data)

@app.route('/recipe/<dish>')
def about_recipe(dish):
    recipe = {}
    data = mongo.db.recipes.find()
    for obj in data:
        if obj["recipe_name"] == dish:
            recipe = obj
    return render_template("recipe.html", recipe=recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)