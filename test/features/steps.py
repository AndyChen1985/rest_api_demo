# -*- coding: utf-8 -*-
from lettuce import step, world, before
from rest_api_demo.app import app
import json
import requests

# @before.all
# def before_all():
#     requests.



@step(u'When I retrieve data from blog api')
def when_i_retrieve_data_from_blog_api(step):
    world.response = requests.get("http://localhost:8888/api/blog/posts/?per_page=2&page=1")

@step(u'Then I should get a \'([^\']*)\' status code')
def then_i_should_get_a_group1_status_code(step, expectedCode):
    assert world.response.status_code == int(expectedCode), "correct status code" 


@step(u'Then the following info are returned:')
def then_the_following_info_are_returned(step):
    assert world.response.json().items == step.hashes , 'This step must be implemented'