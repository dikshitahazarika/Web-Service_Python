from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import platform
import requests
import re

main = Flask(__name__)

# Check if Flask has run successfully and service should return the following request.
@main.route("/")
def test():
    html = "<h1><center>Pond Test</center></h1>\
        <P><center><em>GET /PING - REQUEST RETURNS “PONG”</em></center></P>\
        <P><center><em>GET /SYSTEM - REQUEST RETURNS A SYSTEM INFORMATION AND SERVICE VERSION.</em></center></P>\
        <P><center><em>GET /MEDIAINFO/ID - REQUEST RETURNS TITLE, FILENAME, SIZE, DIMENSIONS AND PRICE.</em></center></P>"
    return html


if __name__ == "__main__":
      # http://127.0.0.1
    main.run(host="0.0.0.0", debug=True, port=8080)



