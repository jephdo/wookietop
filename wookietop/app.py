import time
import threading

from flask import Flask, jsonify, send_file

from .processes import poll_processes, processes_to_dict

app = Flask(__name__)
app.config['DEBUG'] = True

def track_system_resources(meters, interval=1):
    """
    d
    """

    def track():
        while True:
            for meter in meters:
                meter.read()
            time.sleep(interval)

    t = threading.Thread(target=track)
    t.daemon = True
    t.start()

@app.route('/')
@app.route('/overview/')
def overview():
    return send_file('templates/base.html')

@app.route('/logs/')
def f():
    if request.GET:
        return send_file()

    if request.POST:
        return jsonify()

@app.route('/api/')
def return_stats():
    stats = {'1': 2}

    return jsonify(stats)

@app.route('/api/processes/')
def show_processes():
    processes, statuses = poll_processes()

    return jsonify({
        'processes': processes_to_dict(processes),
        'statuses':  statuses
    })



# @app.route('/')
# def directory_list():

if __name__ == '__main__':
    # from .meter import meters
    # track_system_resources(meters)
    app.run()