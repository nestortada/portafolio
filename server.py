from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)

# Habilitar CORS
CORS(app)

@app.route('/execute', methods=['POST'])
def execute_script():
    try:
        # Ruta del script de Python que deseas ejecutar
        script_path = 'D:\portafolio\Documentos\AdmonCentroAdultos\Principall.py'
        
        # Ejecutar el script usando subprocess
        result = subprocess.run(
            ['python', script_path],  # Revisa si necesitas 'python3' en lugar de 'python'
            capture_output=True,
            text=True
        )
        
        # Comprobar si la ejecución fue exitosa
        if result.returncode == 0:
            return jsonify({
                'status': 'success',
                'output': result.stdout.strip()  # Elimina espacios extra
            })
        else:
            return jsonify({
                'status': 'error',
                'error': result.stderr.strip()
            }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
