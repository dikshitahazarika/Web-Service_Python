## Web-Service_Python
 Building a simple web service that provides information about a preview image from a Pond5 media item <br/>

## Steps to Follow:<br/>
 *1. Install Python3<br/>
 *2. Install Required Dependencies(Lock and track the dependencies of the project)<br/>
---Command Prompt<br/><br/>
     pip freeze > requirements.txt<br/>

## Execute following command to run the application.<br/>
     ---Command Prompt<br/>
          python main.py<br/>
     

## Access the following urls in the browser:<br/>
  
     1. [http://0.0.0.0:8080/ping](http://0.0.0.0:8080/ping) <br/>

     2. [http://0.0.0.0:8080/system](http://0.0.0.0:8080/system) <br/>
 
     3. [http://0.0.0.0:8080/mediainfo/12192732](http://0.0.0.0:8080/mediainfo/12192732) eg: '12192732' is media id  from “           https://www.pond5.com/photo/12192732/night-city-skyline-and-moon.html ”<br/>

## Unit Tests <br/>

## To run simple unit tests run the command: <br/>
* ---Command Prompt <br/>
  * python test_main.py <br/>

##Testing on PostMan <br/>


1.postman/System Image(When we enter System request should return JSON object with service version and system information)<br/>
![](/postman/invalid media.png)<br/>
2.postman/ping Image (When we enter Ping request should return “pong”)<br/>
![](/postman/invalid ping.png)<br/>
3.postman/ping_error Image(When we do not enter Ping request eg:http://0.0.0.0:8080/service)<br/>
![](/postman/invalid ping_error.png)<br/>
4.postman/media_info Image(When we enter valid media ID which associated with   pond5 website media id)<br/>
![](/postman/media_info.png)<br/>
5.postman/Invalid Image(When we enter invalid media ID)<br/>
![](/postman/system.png)<br/>
