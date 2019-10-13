from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import platform
import requests
import re

main = Flask(__name__)

# Check if Flask has run successfully and service should return the following request.

@main.route("/")
def descp():
    html = "<h1><center>Pond5 Test</center></h1>\
        <P><center><em>GET /PING - REQUEST RETURNS “PONG”</em></center></P>\
        <P><center><em>GET /SYSTEM - REQUEST RETURNS A SYSTEM INFORMATION AND SERVICE VERSION.</em></center></P>\
        <P><center><em>GET /MEDIAINFO/ID - REQUEST RETURNS TITLE, FILENAME, SIZE, DIMENSIONS AND PRICE.</em></center></P>"
    return html

# if we request Ping  then return "PONG", else  return "ERROR!!PLEASE TRY WITH PING".
@main.route("/<request>", methods=["GET"])
def ping(request):
    if request == "ping":
        return "Pong"
    else:
        return "ERROR!! PLEASE TRY WITH PING"
    
# platform import provided show all the information system & return JSON format.
@main.route("/system")
def system():
    systeminfo = {"platform": platform.architecture(),
                  "processor": platform.processor(),
                  # "S_version": "0.0.1",
                  "system": platform.system(),
                  "version": platform.version(),}
    return jsonify(systeminfo)

# Get all media information using media_id it is the numbered code of the specific photo resource
# eg: '12192732' is media id  from “ https://www.pond5.com/photo/12192732/night-city-skyline-and-moon.html ”.
@main.route("/mediainfo/<media_id>", methods=["GET"])
def media(media_id):
    page = requests.get("https://www.pond5.com/photo/" + str(media_id))
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    filename = soup.find("meta", property="og:image")
    filename = filename["content"]
    height = soup.find("meta", property="og:image:height")
    height = height["content"]
    regex = re.compile(r'(\D)+')
    price = soup.find(id="itemDetail-totalPrice").text.strip()
    price = regex.sub('', price)
    size = soup.find_all("dd")[12].text
    title = soup.find("meta", property="twitter:title")
    title = title["content"]
    width = soup.find("meta", property="og:image:width")
    width = width["content"]
    # dim = soup.find("{} x {}".format(height, width))

    # all media information
    imageinfo = {
        "filename": filename,
        "height": height,
        "price": price,
        "size": size,
        "title": title,
        "width": width,
       # "dim": dim,
    }
    return jsonify(imageinfo)


def invalidId():
    html = "<h1>Pond descp</h1>\
        <p>Id is not available</p>\
        <p>Please enter a valid id</p>"
    return html

@main.errorhandler(Exception)
def idnotfound(e):
    return invalidId()


if __name__ == "__main__":
      # http://127.0.0.1
    main.run(host="0.0.0.0", debug=True, port=8080)
