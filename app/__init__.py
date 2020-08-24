from flask import  Flask


application = Flask(__name__)

from app import  route
if __name__ == "__main__":
    application.run()