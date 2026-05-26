from flask import Flask
from flask_cors import CORS
from datetime import datetime
from zoneinfo import ZoneInfo # Імпортуємо роботу з часовими поясами

app = Flask(__name__)  
CORS(app)

@app.route('/api/time', methods=['GET'])
def get_time():
    # Беремо поточний час строго за київським часом
    now = datetime.now(ZoneInfo("Europe/Kyiv"))
    responseBody = now.strftime("%H:%M:%S")
    return responseBody

if __name__ == '__main__':
    # We work on port 8080, listening to all interfaces inside the future container
    app.run(debug=True, port=8080, host="0.0.0.0")
