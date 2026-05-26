from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def show_headers():
    x_forwarded_for = request.headers.get('X-Forwarded-For', 'Not set')
    x_real_ip = request.headers.get('X-Real-IP', 'Not set')
    remote_addr = request.remote_addr
    
    # Формируем текстовый список заголовков
    headers_text = '\n'.join([f'{key}: {value}' for key, value in request.headers.items()])

    return f'''
Client IP Information
=====================
X-Forwarded-For (chain): {x_forwarded_for}
X-Real-IP: {x_real_ip}
request.remote_addr (container view): {remote_addr}

Full headers:
{headers_text}
    ''', 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)