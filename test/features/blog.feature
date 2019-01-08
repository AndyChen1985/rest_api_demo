Feature: blogs CRUD operation

       Scenario: Retrieve blog list
            When I retrieve data from blog api
            Then I should get a '200' status code
            Then the following info are returned:
            |   id      |                title                     |
            |    1      |  The New RThe Road to Extinction         |
            |    2      |  The New Rock                            |