import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'smells_good'
app.config["MONGO_URI"] = 'mongodb+srv://sam_mckenna:YnNPIkpu2VIdHiqT@cluster0.wptnw.mongodb.net/smells_good?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello World'

@app.route('/home')
def home():
    categories=mongo.db.categories.find()

    return render_template("home.html", categories=categories)

@app.route('/add_category')
def add_category():
    return render_template("add_category.html",
    categories=mongo.db.categories.find())

@app.route('/create_recipe')
def create_recipe():
    return render_template("create_recipe.html",
    categories=mongo.db.categories.find(), recipes=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('create_recipe'))

@app.route('/recipe')
def recipe():
    return render_template("recipe.html", recipes=mongo.db.recipes.find())
"""
@app.route('/recipe/<dish>')
def about_recipe(dish):
    recipe = {}
    data = mongo.db.recipes.find()
    for obj in data:
        if obj["recipe_name"] == dish:
            recipe = obj
    return render_template("recipe.html", recipe=recipe)
"""

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

