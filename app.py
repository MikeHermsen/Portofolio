from flask import ( # - Importing all neccesery libarys
    Flask,          # Flask is the main framework i'll be using 
    render_template,# Makes it possible to render an html file to the client
    request,        # Reading input from clients
    escape          # Secure user input
)                   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# The main framework
app = Flask(__name__)


# Pages of the site
# URL OF IMG | TITLE OF PAGE | CONTENT ABOUT PAGE | PAGE URL
pages = [
    
    ('/static/media/background-home.jpg', 'Home', 'Home', '/home'),
    ('/static/media/about-me.jpg', 'About me', 'Learn more about me', '/about-me'),
    ('/static/media/projects.jpg', 'Projects', 'A showcase of my recent projects.', '/projects'),
    ('/static/media/skills.jpeg', 'Skills', 'Check out my experience', '/skills'),
    ('/static/media/contact.jpg', 'Contact', 'Want to get in touch?', '/contact')
]


#-gif returner for loading screen
def getGif():
    return ['Orb electronic'         , 'https://i.gifer.com/yy3.gif']


#-Landig page for all clients
@app.route('/')         # The page that is asked
@app.route('/home')     # ^
def index(): 
    # - Returning the base.html to the client
    return render_template(
                'base.html',            # - The file to return to the client
                title="Home",           # - The title of the page
                gif=getGif(),           # - Calls the function that wil return an random gif to use in the program
                pages=pages)            # - Sending page configs for the links 

#-About me page for all clients
@app.route('/about-me') # The page that is asked to return
def aboutMe():
    #- Returning the about-me.html to the client
    return render_template(
                'base.html',            # - The file to return 
                title="About me",       # The title of the page
                gif=getGif(),           # Calls the function that will return an random gif
                pages=pages)            # - Sending page configs for the links 

@app.route('/projects') # The page that is asked to return
def projects():
    #- Returning the about-me.html to the client
    #-TODO 
    #   * Change the base.html to about-me.html
    #   * Creating the about-me.html
    return render_template(
                'base.html',            # - The file to return 
                title="Projects",       # The title of the page
                gif=getGif(),           # Calls the function that will return an random gif
                pages=pages)            # - Sending page configs for the links 

@app.route('/skills') # The page that is asked to return
def skills():
    #- Returning the about-me.html to the client
    #-TODO 
    #   * Change the base.html to about-me.html
    #   * Creating the about-me.html
    return render_template(
                'base.html',            # - The file to return 
                title="Skills",         # - The title of the page
                gif=getGif(),           # - Calls the function that will return an random gif
                pages=pages)            # - Sending page configs for the links 



@app.route('/contact', methods=['GET', 'POST']) # The page that is asked to return
def contact():
    #- Returning the about-me.html to the client
    #-TODO 
    #   * Change the base.html to about-me.html
    #   * Creating the about-me.html
    if ( request.method == "POST" ):
        user_profile = {
            'email' : escape(request.form['email']),
            'name' : escape(request.form['name']),
            'message'  : escape(request.form['message'])
        }
        if ( len(user_profile["email"]) > 4 ) and ( user_profile["name"] > 2 ) and ( user_profile["message"] > 3 ):

            with open('static/data/emails.txt', 'a+') as f:
                f.write('============================\n')
                f.write(f'Email :     {user_profile["email"]}\n')
                f.write(f'Naam  :     {user_profile["name"]}\n')
                f.write(f'Meessage :     {user_profile["message"]}\n')

        print(user_profile['email'], user_profile['name'], user_profile['message'])

    return render_template(
                'base.html',             # - The file to return 
                title="Contact",         # The title of the page
                gif=getGif(),            # Calls the function that will return an random gif
                pages=pages)             # - Sending page configs for the links 

