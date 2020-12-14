#TSP Service Example

#Prerequites
1. docker

#Commands
1. docker-compose up

#Use application
Docker compose will run 3 containers 
1. rabbitmq
2. publisher
3. consumer
4. example.py

##1. rabbitmq
It's a message broker used for pub/sub implementation of this project
to view the rabbitmq dashboard use following credentials
 - url: http://localhost:15672
 - username: guest
 - password: guest

##2. publisher
The publisher is flask restful service which takes request to find out vehical shortest path. 
All the received request will published to rabbitmq broker 
url: http://localhost:5000

##3. consumer
It will consume request coming from rabbitmq and find run TSP algorithm using google-or toolkit
Solution will be printed on console

##4. example.py
automated script example.py file is available to post request to publisher. 
