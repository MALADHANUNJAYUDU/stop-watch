from flask import Flask, render_template, jsonify, request
import time

app = Flask(_name_)

start_time = 0
elapsed_time = 0
running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global start_time, running
    if not running:
        start_time = time.time()
        running = True
    return jsonify({'status': 'started'})

@app.route('/stop', methods=['POST'])
def stop():
    global elapsed_time, running
    if running:
        elapsed_time += time.time() - start_time
        running = False
    return jsonify({'status': 'stopped'})

@app.route('/reset', methods=['POST'])
def reset():
    global start_time, elapsed_time, running
    start_time = 0
    elapsed_time = 0
    running = False
    return jsonify({'status': 'reset'})

@app.route('/time')
def get_time():
    global start_time, elapsed_time, running
    current_time = elapsed_time
    if running:
        current_time += time.time() - start_time
    return jsonify({'time': round(current_time, 2)})

if _name_ == '_main_':
    app.run(debug=True)
