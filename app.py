from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static/photos'

photos = [
    {"id": 1, "title": "Sunset in the City", "url": "static/photos/sunset.jpg"},
    {"id": 2, "title": "Smart City Skyline", "url": "static/photos/skyline.jpg"},
    {"id": 3, "title": "Traffic Lights at Night", "url": "static/photos/traffic.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)