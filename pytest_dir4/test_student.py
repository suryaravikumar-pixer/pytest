from student import StudentDB
import pytest


db = None
"""setup_module is initiate's the dabase connection for each test module"""
def setup_module(module):
    print('-----------setupmodule---------------')
    global db
    db = StudentDB()
    db.connect('data.json')

"""teardown_module is closes the db connection """
def teardown_module(module):
    print('-----------teardown ---------------')
    db.close()

def test_jhon_data():
    Jhon_data = db.get_data('Jhon')
    assert Jhon_data['id'] == 1
    assert Jhon_data['name'] == 'Jhon'
    assert Jhon_data['result'] == 'pass'

def test_mark_data():
    Mark_data = db.get_data('Mark')
    assert Mark_data['id'] == 2
    assert Mark_data['name'] == 'Mark'
    assert Mark_data['result'] == 'fail'