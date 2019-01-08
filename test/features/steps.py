# -*- coding: utf-8 -*-
from lettuce import step, world, before
from rest_api_demo.app import app
import json

@before.all
def before_all():
    world.app = app.test_client()



@step(u'When I retrieve data from blog api')
def when_i_retrieve_data_from_blog_api(step):
    assert hasattr(world.app, 'get')
    world.response = world.app.get("/")
    print "dafds" 

@step(u'Then I should get a \'([^\']*)\' status code')
def then_i_should_get_a_group1_status_code(step, expectedCode):
    print world.response.status_code
    print expectedCode
    assert(int(expectedCode) == 200)
    assert(hasattr(world, 'response'))
    assert world.response.status_code == int(200), "correct status code" 


@step(u'Then the following info are returned:')
def then_the_following_info_are_returned(step):
    assert world.response.data == "Hello, World!" , 'This step must be implemented'