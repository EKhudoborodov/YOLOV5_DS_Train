import requests
from flask import Flask, render_template, request
import track
from pathlib import Path
import tempfile
#import psycopg2

app = Flask(__name__)

#conn = psycopg2.connect(database="service_db",
#                        user="user1e",
#                        password="huut7364",
#                        host="localhost",
#                        port="5432")
#cursor = conn.cursor()

@app.route('/', methods=['GET'])
def index():
    return render_template('start.html')

@app.route('/result', methods=['POST'])
def login():
    #if request.method == 'POST':
    video = request.files['file']
    video.save("/home/scripter/testing-2/YOLOV5_DS_Train/videos/VvID.mp4")
    track.tracking(video)
    return render_template('result.html')
    #return render_template('result.html', video = track.tracking(f))
#        cursor.execute(f"SELECT * FROM service.users WHERE login='{username}' AND password='{password}'", (str(username), str(password)))
#        records = list(cursor.fetchall())
#        if records != []:
#            return render_template('account.html', full_name=f"Hello, {records[0][1]}!", login=f"Your login:{username}", passw=f"Your password:{password}")
#        else:
#            return render_template('login2.html')
if __name__ == '__main__':
    app.run()
