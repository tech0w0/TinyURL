from flask import Flask, url_for, render_template, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__,  static_url_path='', template_folder="templates")

from app import routes
