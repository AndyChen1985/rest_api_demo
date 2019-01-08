# -*- coding: utf-8 -*-
from lettuce import step, world, before
from rest_api_demo.app import app

from rest_api_demo.api.restplus import api
import requests

if __name__ == "__main__":
     response = requests.get("http://localhost:8888/api/blog/posts/?per_page=2&page=1")
     print response.json().items()