from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if 'Start' in request.form.values():
        subprocess.call('mpv mpv /media/inaki/Data/Music_mess/Mp3/Alex\ Fong.mp3 &', shell=True)
    elif 'Stop' in request.form.values():
        subprocess.call('killall mpv', shell=True)
    return render_template('radio.html')
