import flask, catch_photo, os, time
from threading import Barrier
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'alive', 200
    
last_time = 0
approval = 'waiting'
barrier = Barrier(2)

@app.route('/alert')
def new_alert():
    global last_time
    start = time.time()
    
    if start - last_time < 5:
        return 'approve', 200
    
    global approval
    approval = 'waiting'
    
    if catch_photo.take_photo():
        last_time = time.time()
        barrier.wait()
        
        return approval, 200
    
    return 'invalid', 400

@app.route('/approve')
def approve():
    global approval
    
    if approval != 'waiting':
        return 'no request', 200
    
    approval = 'approve'
    barrier.wait()
    
    return 'approved', 200

@app.route('/deny')
def deny():
    global approval
    
    if approval != 'waiting':
        return 'no request', 200
    
    approval = 'deny'
    barrier.wait()
    
    return 'denied', 200

@app.route('/photo')
def get_photo():
    if os.path.exists("screenshot.jpg"):
        return flask.send_file('screenshot.jpg')
    
    return 'no image', 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)