from flask import Flask
from flask import send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the $PORT env variable, default to 5000 for local dev
    app.run(debug=True, host='0.0.0.0', port=port)  # Bind to 0.0.0.0 to make the app accessible
