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

# -------------------------THE ACCOUNT SECTION--------------------------
# If there is already an available logged in session.
@app.route('/')
def index():
    users = mongo.db.users
    return render_template('index.html', users=mongo.db.users.find())

@app.route('/login_user')
def login_user():
    return render_template("login_user.html", users=mongo.db.users.find())

# creating an account
@app.route('/create_account')
def create_account():
    users = mongo.db.users
    return render_template("create_account.html",users=mongo.db.users.find())

# Posting a newly created account and making the sure that the username is not already taken.


@app.route('/signup', methods=['POST'])

def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        # The password is hashed going in and out of mongodb so it is not at risk of being discovered.
        if existing_user is None:
            hashpass = generate_password_hash(request.form['password'],method='pbkdf2:sha256', salt_length=11)
            users.insert({
                'username': request.form['username'],
                'password': hashpass,
                'favourite_food': request.form['favourite_food'],
                'favourite_cooking_utensil': request.form['favourite_cooking_utensil'],
                'favourite_chef': request.form['favourite_chef']
            })
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
        if check_password_hash(login_user['password'],request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('my_recipes'))
        flash('Try again')
        return render_template("login_user.html", users=mongo.db.users.find())
    return render_template("login_user.html", users=mongo.db.users.find())

@app.route('/account_details')
def account_details():
    try:
        return render_template("account_details.html",detail = mongo.db.users.find({'username': session['username']}))
    except:
        return render_template("login_user.html", users=mongo.db.users.find())

# Deleting account details
@app.route('/delete_user/<user_id>', methods=['GET'])
def delete_user(user_id):
    users = mongo.db.users
    mongo.db.users.remove({'_id': ObjectId(user_id)}) 
    return redirect(url_for('create_account'))
# Logging out of the account.
 
@app.route('/logout')
def logout():
    session.clear()
    return render_template("login_user.html", users=mongo.db.users.find())


# Adding a category template, just to make it easier for the admin to add categories
@app.route('/add_category')
def add_category():

    return render_template("add_category.html", categories=mongo.db.categories)

# Posting the category; I do not have a link on the website for this this is for ease of use for admins; So it is hidden for adding caetgories.
@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert({
                'category_name': request.form['category_name'],
                'username' : session.get("username")})
    return redirect(url_for('create_recipe'))

# -------------------------THE RECIPE SECTION--------------------------


# My Recipes page. The only place you can delete or edit recipes which means only the recipe owner can delete or edit based on username in session.

@app.route('/my_recipes')
def my_recipes():
    try:    
        return render_template("my_recipes.html", recipe=mongo.db.recipes.find({'username': session['username']}))
    except:
        return render_template("login_user.html", users=mongo.db.users.find())


# creating a recipe template
@app.route('/create_recipe')
def create_recipe():
    return render_template("create_recipe.html",categories=mongo.db.categories.find(), recipes=mongo.db.recipes.find())

# Posting the recipe details
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    try:
        recipes = mongo.db.recipes
        users = mongo.db.recipes
        categories = mongo.db.categories
        recipes.insert({
                    'recipe_name' : request.form['recipe_name'],
                    'category_select': request.form['category_select'],
                    'recipe_description' : request.form['recipe_description'],
                    'ingredients_list' : request.form['ingredients_list'],
                    'cooking_instructions' : request.form['cooking_instructions'],
                    'picture_url' : request.form['picture_url'],
                    'username' : session.get("username")
                    })
        return redirect(url_for('create_recipe'))
    except:
        return ('Please make sure you choose a category. Go back and add a category.') #This is so all of the information that they type in is not lost.

# Edit the recipe template
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe  = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, category_select=categories)

# Posting the edit details
@app.route('/push_edit/<recipe_id>', methods=['POST'])
def push_edit(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
            'recipe_name':request.form.get('recipe_name'),
            'recipe_description' : request.form.get('recipe_description'),
            'ingredients_list' : request.form.get('ingredients_list'),
            'cooking_instructions' : request.form.get('cooking_instructions'),
            'picture_url' : request.form.get('picture_url'),
            'username' : session.get("username")
    })
    return redirect(url_for('my_recipes'))

# Deleting a recipe details
@app.route('/delete_recipe/<recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    recipes = mongo.db.recipes
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('my_recipes'))

# Dinner template
@app.route('/dinner')
def dinner():
    recipe=mongo.db.recipes
    return render_template("dinner.html",recipe=mongo.db.recipes.find({'category_select':'Dinner'}))

# Lunch template
@app.route('/lunch')
def lunch():
    recipe=mongo.db.recipes

    return render_template("lunch.html",recipes=mongo.db.recipes.find({'category_select':'Lunch'}))

@app.route('/breakfast')
def breakfast():
    recipe=mongo.db.recipes

    return render_template("breakfast.html",recipes=mongo.db.recipes.find({'category_select':'Breakfast'}))

@app.route('/dessert')
def dessert():
    recipe=mongo.db.recipes

    return render_template("dessert.html",recipes=mongo.db.recipes.find({'category_select':'Dessert'}))

#The unique recipe.
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe=mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)})
    return render_template("recipes.html",recipe = recipe)


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) #MAKE SURE TO TURN OFF DEBUG