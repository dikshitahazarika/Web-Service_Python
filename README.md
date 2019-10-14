## Web-Service_Python
 Building a simple web service that provides information about a preview image from a Pond5 media item.

##Steps to Follow:
1. Install Python3
2. Install Required Dependencies(Lock and track the dependencies of the project)
---Command Prompt
     pip freeze > requirements.txt

## Execute following command to run the application. 
     ---Command Prompt
          python main.py
     

## Access the following urls in the browser:
  
    1. [http://0.0.0.0:8080/ping](http://0.0.0.0:8080/ping)

    2. [http://0.0.0.0:8080/system](http://0.0.0.0:8080/system)
 
    3. [http://0.0.0.0:8080/mediainfo/12192732](http://0.0.0.0:8080/mediainfo/12192732) eg: '12192732' is media id  from “ https://www.pond5.com/photo/12192732/night-city-skyline-and-moon.html ”.

## Unit Tests

## To run simple unit tests run the command:
---Command Prompt
   python test_main.py

##Testing on PostMan


1.postman/System Image(When we enter System request should return JSON object with service version and system information)
2.postman/ping Image (When we enter Ping request should return “pong”)
3.postman/ping_error Image(When we do not enter Ping request eg:http://0.0.0.0:8080/service)
4.postman/media_info Image(When we enter valid media ID which associated with   pond5 website media id)
5.postman/Invalid Image(When we enter invalid media ID)
