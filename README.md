<img src="/static/branding/logo.png" >


<b>Problem Statement</b><br>
If you look at any other recipe sharing websites they are always really busy and their are always elements getting in the way of
actually seeing the instructional steps in the recipe or the ingredients.

<br>
<b>Proposed Solution</b><br>
<i>Smells Good</i> is a website for sharing your favourite websites, when you log in all of your recipes are saved in one place, but you still get to see what recipes
other community members are posting that inspire you. The website is very clean and easily viewable on any device that you might have with you while you are cooking your favourite dish.

## UX
<b>The Smells Good design concept</b> is that it might look like the facebook of food where people can look at each other's recipes and have their own recipe location as well. 
The design is really clean and very functional and does not distract the user from the actual recipe instructions or ingredients which a lot of recipe websites do.<br>

The idea behind the simplicity is that it is easy to cook, that it is simple to read, and that there is nothing that is distracting about the website visually; Suggesting good, simple, clean food.

<b>The user experience for the website</b> The user might have gotten attracted to the website by one of the recipes but they might be enticed to create and account, and interact with the website more
as it is so cleanly designed that it is useful to keep their own recipes on it, and to refer back to it. The website is simply structured into the simplest types of meal categories: breakfast, lunch, dinner, dessert; This means when a user arrives to the website
they know exactly where to go for what overarching food scenario they are trying to find a recipe for. 

<i>Log in with the demo account credentials:</i><br>
<b>Username:</b> Samuel<br>
<b>Password:</b> smellsgood2020<br>

<b>User Story 1: Be Inspired</b><br>
- A new user comes across the <b>Smells Good</b> website and is inspired by the simplicity of the design, the ease of which they can see the information, and high-resolution pictures of the food and chooses a recipe for the occasion that they want to cook for.


<img src="/static/assets/images/index.png">

<b>User Story 2: Selecting a Recipe by Category</b><br>
- The user is able to go to the website and choose a simple recipe category that interests them and chooses the correct recipe for the occasion at speed.  

<img src="/static/assets/images/categories.png">

<b>User Story 3: The user creates an account with Smells Good</b><br>
- After the user has visited the website a few times and is really enjoying the whitespace and the ease of being able to see the recipe information, they decide to create an account with Smells Good. 
They are really happy that Smells Good has made the sensible choice and is hashing all of the passwords and is not asking for their email address on login which makes the site a closed circuit and protects the users data and identity.
<br><br>

<img src="/static/assets/images/create_account.png">

<b>User Story 4: The user creates recipes and manages their 'my recipes' section of the website</b><br>
- The user creates an account and is also asked to state their favourite chef, favourite cooking-utensil and favourite food.
<br><br>
Once they have created an account they are able to visit their own recipes, that they created, in their 'my recipes' section. They are able to manage this 
part of the website to fit their needs by editing recipes as their recipes develop and improve over time,
and they also can delete the recipes that they are no longer interested in.

<img src="/static/assets/images/my_recipes.png">
<img src="/static/assets/images/create_account.png">

## Features
1) <b>Food Categories</b><br><br> 
A user is quickly and easily able to navigate to the food category that they want to find the recipe in: breakfast, lunch, dinner , and dessert. It is that simple.

2) <b>Create an Account Safely</b><br><br> 
A user is able to create an account with a hashed password system and they do not need to user their email address which keeps their identity extremely safe.


3) <b>My Recipes (Edit and Delete) </b><br><br> 
Users are able to manage their own 'my recipes' section of the website where they can edit their existing recipes and also delete the recipes that they are not interested in any longer.

3) <b>Sharing the page link on Facebook </b><br><br> 
Users are able to share the recipe page that they are on onto their Facebook page.

## Future Feature Ideas
1) I really enjoyed thinking-up a contrarian cooking-recipes website because if you look at some of the actual cooking recipes websites, they are so bad actually being functional and the information is really hard to find.
I would love to have a focus group with a lot of people that use these websites and really figure out what they hate about them as most of them seem half a decade behind most modern websites in terms of clean design.

2) Create a shopping list part of the website that just grabs the ingredients from the selected recipe and then populates another part of the website.

3) It would be nice to create a rating of recipes system between the user.

4) Build comments section under the recipes that is hideable so it does not distract from the cleanness of the pages so people can still use it easily for cooking instructions and ingredients.

## Technologies Used

- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to speed up the HTML and CSS work.

- [Google Fonts](https://fonts.google.com/)
        - I used archivo as this website is a little bit like an archive of recipes. It looks very strong and clean as well as a font.

- [Python](https://docs.python.org/3/)

- [Flask] (https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja] (https://jinja.palletsprojects.com/en/2.10.x/templates/)
        - Both Flask and Jinja were used to create the templating around the recipes populating to the website. 

- [CSS](https://cssreference.io/)

- [MongoDb] (https://www.mongodb.com/)
        - MongoDb was used for managing the databases of users, categories and recipes.

- [Werkzeug.Security] (https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
        - I used this for hashing the user passwords and also the hashcomparison for retrieving the passwords.
    
- [bson.objectid] (https://docs.mongodb.com/manual/reference/method/ObjectId/)
        - This was used for pointing at the particular recipes or users within the database.   

- [dotenv] (https://pypi.org/project/python-dotenv/)
        - For protecting the secret keys.

- [flask_pymongo](https://flask-pymongo.readthedocs.io/en/latest/)
        - To be able to interact with mongodb easily.


## Testing
<b>Testing Summary</b><br>
<b>Responsinator:</b> [Link](https://www.responsinator.com/?url=https%3A%2F%2F8080-aa5ae074-9803-49bd-805e-afa25ed5fdf4.ws-eu01.gitpod.io%2F) 

1. <b>User Story 1 & 2:</b> Be inspired and browse the recipe categories.
    1. Try to read all of the text on the index page and make sure that the text looks strong. - Success
    2. The image loads. - Success
    3. Try the 'My Recipes' button and it leads to both the 'My Recipes' section, as well as to the login/account creation part of the website. - Success
    4. Try the 'Great Food' - dropdown menu and try the 'Add Recipe', 'Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Create New Account'  and 'Account details' buttons. The correct information is populated to the page. - Success
    5. Try the login button. - Success
    6. Try the logout button. - Success
    7. Check the index.html page in responsinator(https://www.responsinator.com/?url=https%3A%2F%2Fsammckenna1986.github.io%2FBeenThere-GoogleMapsApi%2F)
        - Success

2. <b>User Story 3:</b> Create a new account.
    1. All of the form is present. - Success
    2. The create account 'submit button' is operational. - Success
    3. The data is added to mongodb. - Success
    4. The logged in user is able to go to the 'account details' page and their information is populated. - Success 
    5. On the 'account details' page the user is able to press the 'delete account' button and the user is removed from the mongodb collection. - Success


1. <b>User Story 4:</b> The user creates recipes and manages their 'my recipes' section of the website.
    1. The recipes that the user created appear correctly on the page. - Success
    2. The 'edit' button works correctly and the information changes correctly in the mongodb recipe collection. - Success
    3. The 'delete' button works correctly and the recipe is deleted from the collection. - Success 
    4. The 'Facebook share' button works correctly and shares the page to a users Facebook.

## Deployment
- I deployed the website on [Heroku](https://smells-good.herokuapp.com/)
    1. Created a Heroku account.
    2. Link Heroku to my github account.
    3. Chose which project to connect the Heroku application to on Github:sammckenna1986/smells_good 
    4. Picked to deplouy the master branch.
    5. Used the 'manual deploy' option and then pressed the 'deploy branch' button.
    6. Waited for the deployment to finish successfully.
    7. Checked the url to make sure that the website deployed successfully.    
## Credits
- Thank you to Antonio Rodriguez, my mentor, who is always a fountain of knowledge and really fun to learn from.
- Thank you to Claire Roberts who asked a great question about her project in the slack channel which between the codeinstitute instructional videos and the answer to her question
made me understand how the process works.
- Thank you to all the teachers on the course; The videos and excercises were excellent.

### Content and Media
- I created the smells good logo myself.
- All of the recipes were taken from the great https://www.bbc.co.uk/food/recipes website.
- The general stock pictures were taken from the pixabay.com website as they are royalty free.

### Acknowledgements

I received a lot of inspiration and instruction from youtube this project and it really help drive a lot of concepts home for me:
- Account Creation System:
            - [Creating a User Login System Using Python, Flask and MongoDB](https://www.youtube.com/watch?v=vVx1737auSE&t=3s)
- Environment variable to hide the secret key:
            - [Python (Flask) - How to set up Environment Variables ( And What are they)](https://www.youtube.com/watch?v=3EuB7J5BnjE)
- Login Functionality and password hashing:
            - [Password Hashing in Flask Using Werkzeug](https://www.youtube.com/watch?v=jJ4awOToB6k)
- Authentication and Authorization With Flask-Login:
            - [Authentication and Authorization With Flask-Login](https://www.youtube.com/watch?v=K0vSCCAM2ss)
- Build a Python CRUD REST API in Flask and MongoDB Using Flask-PyMongo Library:
            -[ Link](https://www.youtube.com/watch?v=HyDACIfdPs0&t=1690s)

The following were some of the recipes websites that I was looking at while creating this website:
- https://www.bbcgoodfood.com/recipes
- https://www.delish.com/cooking/recipe-ideas/g3166/cheap-easy-recipes/
- https://www.seriouseats.com/
- https://www.theguardian.com/tone/recipes
- https://www.jamieoliver.com/recipes/
- https://www.nigelslater.com/Home
- https://www.nigella.com/recipes
- https://myfoodbook.com.au/recipes/categories 