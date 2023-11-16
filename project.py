from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


mesas = {
    'mesa1': {'convidados': ['Ozeni', 'Sergio', 'Nicolly', 'Natasha', 'Vinicius', 'Bruna', 'Marcos', 'Diogo'], 'numero': 1},
    'mesa2': {'convidados': ['Ana', 'Jair', 'Carol', 'Guilherme', 'Amanda', 'Alan', 'Paula', 'Diogo'], 'numero': 2},
    'mesa3': {'convidados': ['Luciana', 'Fernando', 'Jessica', 'Guilherme', 'Dona Vera', 'Matheus', 'Luciano', 'Rose'], 'numero': 3},
    'mesa4': {'convidados': ['Valquiria', 'Gilberto', 'Heloisa', 'Kaique', 'Ricardo', 'Jessica Melo', 'Ryan'], 'numero': 4},
    'mesa5': {'convidados': ['Maria', 'José', 'Selma', 'Adriano', 'Leandro', 'Sonia'], 'numero': 5},
    'mesa6': {'convidados': ['Rosana', 'Claudi', 'Camila', 'Vinicius', 'Rosangela', 'Marcos'], 'numero': 6},
    'mesa7': {'convidados': ['Adriana', 'Moises', 'Gabriela', 'Samara', 'Danilo', 'David', 'Pedro'], 'numero': 7},
    'mesa8': {'convidados': ['Jessica', 'Gusthavo', 'Rose', 'Pastor Alberto', 'Eduardo'], 'numero': 8},
    'mesa9': {'convidados': ['Juliana', 'Kelly', 'Jeremias', 'Matheus', 'Julia', 'Alice', 'Tchunay', 'Cintia'], 'numero': 9},
    'mesa10': {'convidados': ['Maria de Carmo', 'Julia', 'Heton', 'Giovana', 'Cleyton', 'Emilyn', 'Vanderley'], 'numero': 10},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obter_informacoes', methods=['POST'])
def obter_informacoes():
    nome = request.form.get('nome')

    for mesa, info_mesa in mesas.items():
        if nome in info_mesa['convidados']:
            resposta = f"Olá, {nome}! Você está na mesa {info_mesa['numero']} com os seguintes convidados: {', '.join(info_mesa['convidados'])}."
            return jsonify(resposta)


    resposta = f"Desculpe, {nome}, não encontramos informações sobre a sua mesa."
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
