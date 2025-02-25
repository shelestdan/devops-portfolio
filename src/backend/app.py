from flask import Flask # type: ignore
import os

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return f"Hello from backend! ENV: {os.getenv('ENVIRONMENT', 'dev')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)