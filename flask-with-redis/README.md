README
======

This is an example docker-compose project: a Flask web application with Redis storage. The application
has a (single) frontend of a HAProxy container. 

Setup:

    docker-compose up

If needed, we can setup by scaling the web application to a number of instances:

    docker-compose up --scale webapp=2


