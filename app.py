from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'mensagem': 'Bem-vindo à API!',
        'endpoints': {
            'saudacao': '/saudacao?nome=SeuNome',
            'soma': '/soma?numero1=10&numero2=5'
        }
    })

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    return jsonify({
        'mensagem': f' Ola, {nome}! Bem-vindo a API! ',
        'status': 'sucesso',
        'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    })

@app.route('/soma', methods=['GET', 'POST'])
def soma():
    if request.method == 'GET':
        numero1 = request.args.get('numero1', type=float)
        numero2 = request.args.get('numero2', type=float)
    else:
        dados = request.get_json()
        if not dados:
            return jsonify({'erro': 'Dados JSON não fornecidos'}), 400
        numero1 = dados.get('numero1')
        numero2 = dados.get('numero2')
    
    if numero1 is None or numero2 is None:
        return jsonify({'erro': 'Por favor, forneça dois números (numero1 e numero2)'}), 400
    
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        resultado = numero1 + numero2
        return jsonify({
            'numero1': numero1,
            'numero2': numero2,
            'soma': resultado,
            'mensagem': f'A soma de {numero1} + {numero2} = {resultado}',
            'status': 'sucesso',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })
    except ValueError:
        return jsonify({'erro': 'Os valores fornecidos devem ser números'}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) 