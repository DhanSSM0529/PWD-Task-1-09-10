# IMport the flask class form the flask module
from flask import Flask

# Create an instance of the flask class
app = Flask(__name__)

#Define a route for the home page
@app.route('/')
def home():
    return "Hello, Flask app!"

#Run the app
if __name__ == '__main__':
    app.run(debug=True)
    