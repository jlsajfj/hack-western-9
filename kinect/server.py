import flask, catch_photo, os, time


app = flask.Flask(__name__)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'alive', 200
    
last_time = 0

@app.route('/alert')
def new_alert():
    global last_time
    start = time.time()
    
    if start - last_time < 5:
        return 'too recent', 400
    
    if catch_photo.take_photo():
        last_time = time.time()
        #return flask.redirect('/photo', 302)
        return 'done', 200
    
    return 'failed', 400

@app.route('/photo')
def get_photo():
    if os.path.exists("screenshot.jpg"):
        return flask.send_file('screenshot.jpg')
    
    return 'no image', 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)