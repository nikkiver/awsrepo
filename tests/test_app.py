from  app.route import  index
from app import  application
import  pytest



@pytest.fixture(scope='module')
def test_client():
    test_client = application.test_client()
    ctx = application.app_context()
    ctx.push()

    yield test_client

    ctx.pop()


def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
