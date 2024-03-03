from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    env_vars = '<br>'.join([f'{key}: {value}' for key, value in os.environ.items()])
    return f'<h1>Environment Variables</h1><p>{env_vars}</p>'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)