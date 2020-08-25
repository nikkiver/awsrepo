from  app.route import  index



def test_index():
    assert index() ==("Index page rendered" ,200)