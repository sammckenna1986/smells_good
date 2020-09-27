import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'smells_good'
app.config["MONGO_URI"] = os.getenv("DBPASS")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

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
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('create_recipe'))

#creating an account
@app.route('/create_account')
def create_account():
    return render_template("create_account.html",
    users=mongo.db.users.find())

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            #hashpass = bcrypt.hashpw(request.form['password'], bcrypt.genSalt())
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            users.insert_one(request.form.to_dict())
            session['username'] = request.form['username']
            return redirect(url_for('create_recipe'))
        
        return 'That username already exists. Choose another username.'

    return render_template('create_account.html')

# logging into an account
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        

    return 'Invalid username/password combination'

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'recipe_image' in request.files:
        recipe_image = request.files['recipe_image']
        mongo.save_file(recipe_image.filename, recipe_image)
    return redirect(url_for('create_recipe'))

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)



@app.route('/recipe')
def recipe():
    return render_template("recipe.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

