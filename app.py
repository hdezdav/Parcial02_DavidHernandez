from flask import Flask, jsonify
import math

app = Flask(__name__)

def calcular_factorial(n):
    # Calcula el factorial 
    if n < 0:
        return None
    return math.factorial(n)

def es_par(n):
    # Ver si es numero es par
    return n % 2 == 0

@app.route('/factorial/<int:numero>', methods=['GET'])
def obtener_factorial(numero):
    # Endpoint que recibe un numero y devuelve su factorial y si es par o impar
    factorial = calcular_factorial(numero)
    
    if factorial is None:
        return jsonify({
            'error': 'no puede ser negativo'
        }), 400
    
    etiqueta = 'par' if es_par(numero) else 'impar'
    
    respuesta = {
        'numero': numero,
        'factorial': factorial,
        'paridad-input': etiqueta
    }
    
    return jsonify(respuesta), 200

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({
        'Modo de uso': '/factorial/<numero>'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
