from app import app, db
from flask import jsonify, request
from app.models import Espaco, Loja, Marca
from sqlalchemy.orm import joinedload

# Rota GET - Listar todos os espaços com nomes de Loja e Marca
@app.route('/espacos', methods=['GET'])
def listar_espacos():
    espacos = Espaco.query.options(
        joinedload(Espaco.loja), joinedload(Espaco.marca)
    ).all()
    espacos_list = [
        {
            'id': espaco.id,
            'nome': espaco.nome,
            'status': espaco.status,
            'descricao': espaco.descricao,
            'loja': espaco.loja.nome,
            'loja_id': espaco.loja.id,
            'marca': espaco.marca.nome,
            'marca_id': espaco.marca.id
        }
        for espaco in espacos
    ]
    return jsonify(espacos_list)

# Rota PUT - Atualizar marca de um espaço
@app.route('/espacos/<int:id>', methods=['PUT'])
def atualizar_marca_espaco(id):
    espaco = Espaco.query.get_or_404(id)
    dados = request.get_json()

    nova_marca_id = dados.get('marca_id')
    if not nova_marca_id:
        return jsonify({'erro': 'Campo marca_id é obrigatório'}), 400

    nova_marca = Marca.query.get(nova_marca_id)
    if not nova_marca:
        return jsonify({'erro': 'Marca não encontrada'}), 404

    espaco.marca_id = nova_marca_id
    db.session.commit()

    # Recarrega os dados do espaço para refletir a nova marca
    db.session.refresh(espaco)

    return jsonify({
        'mensagem': 'Marca atualizada com sucesso',
        'espaco': {
            'id': espaco.id,
            'nome': espaco.nome,
            'status': espaco.status,
            'descricao': espaco.descricao,
            'loja': espaco.loja.nome,
            'marca': espaco.marca.nome
        }
    }), 200

# Rota GET - Listar marcas disponíveis
@app.route('/marcas', methods=['GET'])
def listar_marcas():
    marcas = Marca.query.all()
    return jsonify([
        {'id': marca.id, 'nome': marca.nome}
        for marca in marcas
    ])


@app.route('/espacos/<int:id>', methods=['DELETE'])
def deletar_espaco(id):
    espaco = Espaco.query.get_or_404(id)
    db.session.delete(espaco)
    db.session.commit()
    return jsonify({'mensagem': f'Espaço com ID {id} foi deletado com sucesso.'}), 200

@app.route('/espacos', methods=['POST'])
def criar_espaco():
    dados = request.get_json()

    nome = dados.get('nome')
    status = dados.get('status')
    descricao = dados.get('descricao')
    loja_id = dados.get('loja_id')
    marca_id = dados.get('marca_id')

    # Validações básicas
    if not nome or not status or not loja_id or not marca_id:
        return jsonify({'erro': 'Campos obrigatórios ausentes'}), 400

    loja = Loja.query.get(loja_id)
    marca = Marca.query.get(marca_id)
    if not loja or not marca:
        return jsonify({'erro': 'Loja ou Marca inválida'}), 400

    novo_espaco = Espaco(
        nome=nome,
        status=status,
        descricao=descricao,
        loja_id=loja_id,
        marca_id=marca_id
    )

    db.session.add(novo_espaco)
    db.session.commit()

    return jsonify({
        'mensagem': 'Espaço criado com sucesso',
        'espaco': {
            'id': novo_espaco.id,
            'nome': novo_espaco.nome,
            'status': novo_espaco.status,
            'descricao': novo_espaco.descricao,
            'loja': loja.nome,
            'marca': marca.nome
        }
    }), 201
