import os, socket, subprocess, signal
from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

APPS = {
    'kalshi': {
        'name': 'kalshi konnektor',
        'desc': 'Prediction market edge detector',
        'port': 5555,
        'url': 'http://localhost:5555',
        'cwd': os.path.expanduser('~/kalshi-edge'),
        'cmd': ['python3', 'app.py'],
        'type': 'web',
        'match': 'kalshi-edge/app.py',
    },
    'streamfader': {
        'name': 'StreamFader',
        'desc': 'Streaming content ranker with DJ fader',
        'port': 5556,
        'url': 'http://localhost:5556',
        'cwd': os.path.expanduser('~/streamfader'),
        'cmd': ['python3', 'app.py'],
        'type': 'web',
        'match': 'streamfader/app.py',
    },
    'tracktracks': {
        'name': 'TrackTracks',
        'desc': 'Per-track CPU monitor for Ableton Live',
        'port': None,
        'url': None,
        'cwd': os.path.expanduser('~/track_cpu_monitor'),
        'cmd': ['arch', '-arm64', 'python3', 'viewer/main.py'],
        'type': 'gui',
        'match': 'track_cpu_monitor/viewer/main.py',
    },
    'dawdoctor': {
        'name': 'DAW Doctor',
        'desc': 'Ableton diagnostics — CPU, latency, dropouts',
        'port': None,
        'url': None,
        'cwd': os.path.expanduser('~/ableton-diagnostics'),
        'cmd': ['open', '-a', 'Terminal', os.path.expanduser('~/ableton-diagnostics/launch.command')],
        'type': 'cli',
        'match': 'ableton-diagnostics/diagnose.py',
    },
}

_procs = {}  # app_key → Popen


def port_open(port):
    try:
        s = socket.socket()
        s.settimeout(0.3)
        result = s.connect_ex(('127.0.0.1', port))
        s.close()
        return result == 0
    except Exception:
        return False


def proc_running(match):
    for p in psutil.process_iter(['cmdline']):
        try:
            cmd = ' '.join(p.info['cmdline'] or [])
            if match in cmd:
                return True
        except Exception:
            pass
    return False


def is_running(key):
    cfg = APPS[key]
    if cfg['type'] == 'web':
        return port_open(cfg['port'])
    return proc_running(cfg['match'])


@app.route('/')
def index():
    return render_template('index.html', apps=APPS)


@app.route('/api/status')
def status():
    return jsonify({k: is_running(k) for k in APPS})


@app.route('/launch/<key>', methods=['POST'])
def launch(key):
    if key not in APPS:
        return jsonify({'ok': False, 'error': 'unknown app'}), 404
    cfg = APPS[key]
    if is_running(key):
        return jsonify({'ok': True, 'already': True})
    try:
        env = {**os.environ, 'PYTHONPATH': ''}
        p = subprocess.Popen(cfg['cmd'], cwd=cfg['cwd'], env=env,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        _procs[key] = p
        if cfg['type'] == 'web' and cfg['url']:
            subprocess.Popen(['bash', '-c', f'sleep 3 && open "{cfg["url"]}"'])
        return jsonify({'ok': True})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/stop/<key>', methods=['POST'])
def stop(key):
    if key not in APPS:
        return jsonify({'ok': False, 'error': 'unknown app'}), 404
    cfg = APPS[key]
    # Kill by process match
    killed = False
    match = cfg['match']
    for p in psutil.process_iter(['cmdline', 'pid']):
        try:
            cmd = ' '.join(p.info['cmdline'] or [])
            if match in cmd:
                os.kill(p.info['pid'], signal.SIGTERM)
                killed = True
        except Exception:
            pass
    if key in _procs:
        try:
            _procs[key].terminate()
        except Exception:
            pass
        del _procs[key]
    return jsonify({'ok': True, 'killed': killed})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5554, debug=False)
