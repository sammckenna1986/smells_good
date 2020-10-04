import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'smells_good'
app.config["MONGO_URI"] = os.getenv("DBPASS")

mongo = PyMongo(app)

# Index route and checking if logged in.
@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

# Adding a category
@app.route('/home')
def home():
    categories=mongo.db.categories.find()

    return render_template("home.html", categories=categories)

@app.route('/add_category')
def add_category():
    return render_template("add_category.html",
    categories=mongo.db.categories.find())


# creating a recipe
@app.route('/create_recipe')
def create_recipe():
    return render_template("create_recipe.html",
    categories=mongo.db.categories.find(), recipes=mongo.db.categories.find())
    



@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert({
                'recipe_name' : request.form['recipe_name'],
                'category_select': request.form['category_select'],
                'recipe_description' : request.form['recipe_description'],
                'ingredients_list' : request.form['ingredients_list'],
                'cooking_instructions' : request.form['cooking_instructions'],
                'picture_url' : request.form['picture_url'],
                'username' : session.get("username")})
    return redirect(url_for('create_recipe'))

#creating an account
@app.route('/create_account')
def create_account():
    return render_template("create_account.html",
    users=mongo.db.users.find())

#MY RECIPES PAGE ------------
@app.route('/my_recipes')
def my_recipes():
    #recipes=mongo.db.recipes.find_one({'username': session['username']})
    return render_template("my_recipes.html", recipe = recipe)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = generate_password_hash(request.form['password'],method='pbkdf2:sha256', salt_length=11)
            users.insert({
                'username' : request.form['username'],
                'password': hashpass,
                'favourite_food' : request.form['favourite_food'],
                'favourite_cooking_utensil' : request.form['favourite_cooking_utensil'],
                'favourite_chef' : request.form['favourite_chef']})
            session['username'] = request.form['username']
            return redirect(url_for('create_recipe'))
        
        return 'That username already exists. Choose another username.'

    return render_template('create_account.html')

# logging into an account
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        #if check_password_hash(generate_password_hash(login_user['password'],method='pbkdf2:sha256', salt_length=11),request.form['password']):
        if check_password_hash(login_user['password'],request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('my_recipes'))

        return 'NO'

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'recipe_image' in request.files:
        recipe_image = request.files['recipe_image']
        mongo.save_file(recipe_image.filename, recipe_image)
    return redirect(url_for('create_recipe'))

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/dinner')
def dinner():
    recipe=mongo.db.recipes

    return render_template("dinner.html",recipes=mongo.db.recipes.find())


@app.route('/recipe/<unique_id>')
def recipe(unique_id):
    recipe=mongo.db.recipes.find_one({'_id':ObjectId(unique_id)})

    return render_template("recipes.html",recipe = recipe)

@app.route('/recipes')
def recipes():
    #recipe =mongo.db.recipes.find()
    recipe = mongo.db.users
    return render_template("recipes.html",recipe = mongo.db.recipes.find())

@app.route('/account_details/<user_id>')
def account_details(user_id):
    detail=mongo.db.users.find_one({'_id':ObjectId(user_id)})

    return render_template("account_details.html",detail = detail)


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

