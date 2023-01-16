from flask import Flask, request, session, g, url_for, Blueprint, render_template
from flask_login import login_required, current_user

import json
import requests


views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    video_url = "http://35.197.224.224/myflix/videos"
    vid = requests.get(video_url)
    vid_json = vid.json()
    return render_template("home.html", gallery = vid_json, user=current_user)

@views.route('/<category>')
@login_required
def category(category):
    video_url = 'http://35.197.224.224/myflix/videos?filter={"video.category":"'+category+'"}'
    vid = requests.get(video_url)
    vid_json = vid.json()
    return render_template("home.html", gallery = vid_json, user=current_user)

@views.route('/play/<uuid>')
@login_required
def video(uuid):
    video_url =  'http://35.197.224.224/myflix/videos?filter={"video.uuid":"'+uuid+'"}'
    vid = requests.get(video_url)
    vid_json = vid.json()
    return render_template("video.html", gallery = vid_json, user=current_user)