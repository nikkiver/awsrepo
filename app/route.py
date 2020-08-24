from app import  application


@application.route('/' , methods=['GET'])
def index():
    return "Index page rendered" , 200
