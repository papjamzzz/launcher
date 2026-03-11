#!/bin/bash
cd "$(dirname "$0")"
pkill -f "python3 app.py" 2>/dev/null
pip3 install -q -r requirements.txt
python3 app.py &
sleep 2 && open http://localhost:5554
wait
