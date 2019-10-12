from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import platform
import requests
import re

main = Flask(__name__)


if __name__ == "__main__":
      # http://127.0.0.1
    main.run(host="0.0.0.0", debug=True, port=8080)
