from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

# Configuração para arquivos estáticos
app.static_folder = 'static'
app.static_url_path = '/static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # Criar pasta static/images se não existir
    os.makedirs('static/images', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)