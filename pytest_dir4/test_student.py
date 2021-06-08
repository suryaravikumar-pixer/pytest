from student import StudentDB
import pytest

"""with this fixture we can return db to the test cases but it calls setupmodule for each test, we want setupmodule begining of the test """
# @pytest.fixture 
"""yeah, this worked well interms of our requirement"""
@pytest.fixture(scope='module')
def db():
    print('-----------setupmodule---------------')
    db = StudentDB()
    db.connect('data.json')
    yield db #return replaced by yield, at end of the test close connection will executed 

    """teardown_module is closes the db connection """
    print('-----------teardown ---------------')
    db.close()
    


def test_jhon_data(db):
    Jhon_data = db.get_data('Jhon')
    assert Jhon_data['id'] == 1
    assert Jhon_data['name'] == 'Jhon'
    assert Jhon_data['result'] == 'pass'

def test_mark_data(db):
    Mark_data = db.get_data('Mark')
    assert Mark_data['id'] == 2
    assert Mark_data['name'] == 'Mark'
    assert Mark_data['result'] == 'fail'