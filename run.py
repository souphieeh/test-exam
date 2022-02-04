#import necessary modules
from flask import Flask, render_template


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# webscraping function
def my_scraper():
    # YOUR CODE GOES HERE


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


# starts the webserver
if __name__ == "__main__":
    app.run()
