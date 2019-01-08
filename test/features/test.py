# -*- coding: utf-8 -*-
from lettuce import step, world, before
from rest_api_demo.app import app

from rest_api_demo.api.restplus import api

if __name__ == "__main__":
    client = app.test_client()
    # response = client.get("/blog/categories/")
    doc(api)