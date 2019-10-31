from flask import Flask
from play import play_audio

app = Flask(__name__)

@app.route('/')
def hello():
    play_audio('utils/chewie.mp3')
    return 'Hello world!'

@app.route('/commit', methods = ['POST'])
def commit():
    play_audio('utils/chewie.mp3')
    return 'You\'ve commited a new file!'

if __name__ == '__main__':
    app.run(debug=True)
