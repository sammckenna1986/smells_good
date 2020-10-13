<img src="../static/branding/logo.png" >

# Smells Good

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


<img src="../static/assets/images/md/index.png" style="height:20%;width:20%;margin-left:33%;">

<b>User Story 2: Selecting a Recipe by Category</b><br>
- The user is able to go to the website and choose a simple recipe category that interests them and chooses the correct recipe for the occasion at speed.  

<img src="../static/assets/images/md/categories.png" style="height:20%;width:20%;margin-left:33%;">

<b>User Story 3: The user creates an account with Smells Good</b><br>
- After the user has visited the website a few times and is really enjoying the whitespace and the ease of being able to see the recipe information, they decide to create an account with Smells Good. 
They are really happy that Smells Good has made the sensible choice and is hashing all of the passwords and is not asking for their email address on login which makes the site a closed circuit and protects the users data and identity.
<br><br>

<img src="../static/assets/images/md/create_account.png" style="height:20%;width:20%;margin-left:33%;">

<b>User Story 4: The user creates recipes and manages their 'my recipes' section of the website</b><br>
- The user creates an account and is also asked to state their favourite chef, favourite cooking-utensil and favourite food.
<br><br>
Once they have created an account they are able to visit their own recipes, that they created, in their 'my recipes' section. They are able to manage this 
part of the website to fit their needs by editing recipes as their recipes develop and improve over time,
and they also can delete the recipes that they are no longer interested in.

<img src="../static/assets/images/md/my_recipes.png" style="height:20%;width:20%;margin-left:33%;">
<img src="../static/assets/images/md/create_account.png" style="height:20%;width:20%;margin-left:33%;">

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
    12. Check the page in [responsinator](https://www.responsinator.com/?url=https%3A%2F%2Fsammckenna1986.github.io%2FBeenThere-GoogleMapsApi%2Fibiza.html) - Success


## Deployment
- I deployed the website on [github pages](https://sammckenna1986.github.io/BeenThere-GoogleMapsApi/index.html)
    1. Made sure that my github repository was up to date by 'git push' command in terminal.
    2. Went to settings of that particular gihub repository.
    3. Navigated to the github pages part of the settings and published the master branch.
    4. Refreshed the page and then tried the blue hyperlink where the website was published at to make sure that it works.
    5. Then I tested the deployment in responsinator to make sure that it looks good on all devices and that it is truly, phone-first, responsive.
    
## Credits
- Thank you to Antonio Rodriguez, my mentor, who's three meetings on this project were excellent and helped me understand a few concepts that I was missing.
- Thank you to Claire Lally for clarifying a few concepts on the phone and for providing some extra motivation.
- Thank you to all the teachers on the course; The videos and excercises were excellent.

### Content and Media
- The blurbs for the cutomised google maps markers I got from the places' own websites.
- The social media icons were from fontawesome.
- All the pictures were copyright free and were downloaded from https://pixabay.com/.
- The bean logo image I got from google images.


### Acknowledgements

I received a lot of inspiration and instruction from the following links:
- https://developers.google.com/maps/documentation/javascript/cloud-based-map-styling
- https://stackoverflow.com/questions/40064293/add-second-marker-on-google-maps-javascript-code
- https://www.exberliner.com/whats-on/food-drink/nanum/
- https://www.standard.co.uk/go/london/restaurants/jimi-famurewa-restaurant-review-la-chingada-surrey-quays-a4366261.html
- https://www.france-voyage.com/restaurants-guide/restaurant-nice-120949.htm
- https://bigseventravel.com/2019/10/best-bars-in-nice/
- https://www.girafeparis.com/en
- https://www.booking.com/hotel/fr/la-nouvelle-republique.html?aid=356980&label=gog235jc-1DCAMoTTjjAkgzWANoaYgBAZgBMbgBB8gBDNgBA-gBAfgBAogCAagCA7gC0aO-9wXAAgHSAiRlYWMzMTQ1Zi05MTkyLTQ3NWYtOGM1NS0yYmQ4YjVhMDJhZjjYAgTgAgE&sid=c0209fec1728bf25488978eb82c8b64b&lp_sr_snippet=1
- https://www.tripadvisor.ie/Restaurant_Review-g652116-d10446195-Reviews-Es_Tragon-Sant_Antoni_de_Portmany_Ibiza_Balearic_Islands.html
- https://www.tripadvisor.ie/Attraction_Review-g642208-d4355606-Reviews-Liquido_Cocktail_Bar-Santa_Eulalia_del_Rio_Ibiza_Balearic_Islands.html
- https://www.inspirock.com/spain/santa-eulalia-del-rio/liquido-cocktail-bar-a3165514397
- https://www.tripadvisor.ie/ShowUserReviews-g642208-d4355606-r487945949-Liquido_Cocktail_Bar-Santa_Eulalia_del_Rio_Ibiza_Balearic_Islands.html
- https://www.hrhibiza.com/amenities.htm
- https://www.w3schools.com/jsref/met_element_addeventlistener.asp
- https://www.partners.skyscanner.net/affiliates/widgets-quick-start
- https://blog.hubspot.com/marketing/html-form-email
- https://www.youtube.com/watch?v=GMXFMVg5E4U
- https://developers.google.com/maps/documentation/javascript/examples/places-searchbox#maps_places_searchbox-javascript
- https://www.geeksforgeeks.org/hide-or-show-elements-in-html-using-display-property/#:~:text=Style%20display%20property%20is%20used,getElementById(%22element%22).
- https://developers.google.com/places/
- https://getbootstrap.com/docs/4.5/getting-started/introduction/