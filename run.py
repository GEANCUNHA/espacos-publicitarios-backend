from app import app, db
from app.models import Espaco, Loja, Marca

# Função para popular o banco de dados com dados fictícios
def popular_banco():
    # Criação das tabelas
    db.create_all()

    # Verifica se o banco já contém dados
    if Espaco.query.count() == 0:
        # Dados fictícios para lojas
        loja1 = Loja(nome="TechHome Store", endereco="Avenida das Tecnologias, 1000")
        loja2 = Loja(nome="Eletrônica Center", endereco="Rua da Inovação, 543")

        # Marcas reais de eletrônicos, linha branca e telefonia
        marca1 = Marca(nome="Samsung")
        marca2 = Marca(nome="LG")
        marca3 = Marca(nome="Sony")
        marca4 = Marca(nome="Philips")
        marca5 = Marca(nome="Electrolux")
        marca6 = Marca(nome="Brastemp")
        marca7 = Marca(nome="Consul")
        marca8 = Marca(nome="Apple")
        marca9 = Marca(nome="Motorola")
        marca10 = Marca(nome="Xiaomi")

        # Adiciona as lojas e marcas ao banco
        db.session.add_all([loja1, loja2, marca1, marca2, marca3, marca4, marca5, marca6, marca7, marca8, marca9, marca10])
        db.session.commit()

        # Populando os espaços publicitários com dados fictícios
        espaco1 = Espaco(nome="Display Entrada", status="ocupado", descricao="Display eletrônico na entrada principal", loja_id=1, marca_id=1)
        espaco2 = Espaco(nome="Banner Central", status="disponível", descricao="Banner central de promoções de smartphones", loja_id=1, marca_id=8)
        espaco3 = Espaco(nome="Display Lateral", status="ocupado", descricao="Display lateral de TVs e eletrônicos", loja_id=1, marca_id=2)
        espaco4 = Espaco(nome="Totem Interativo", status="disponível", descricao="Totem de autosserviço para celulares", loja_id=2, marca_id=9)
        espaco5 = Espaco(nome="Display Linha Branca", status="ocupado", descricao="Display de eletrodomésticos", loja_id=2, marca_id=5)
        espaco6 = Espaco(nome="Expositor de Celulares", status="disponível", descricao="Expositor de celulares da marca Xiaomi", loja_id=1, marca_id=10)
        espaco7 = Espaco(nome="Display Geladeiras", status="ocupado", descricao="Display de geladeiras Samsung", loja_id=2, marca_id=1)
        espaco8 = Espaco(nome="Expositor de Smartphones", status="disponível", descricao="Expositor de smartphones Motorola", loja_id=1, marca_id=9)
        espaco9 = Espaco(nome="Display Televisores", status="ocupado", descricao="Display de televisores LG", loja_id=1, marca_id=2)
        espaco10 = Espaco(nome="Expositor de Lavadoras", status="disponível", descricao="Expositor de lavadoras Consul", loja_id=2, marca_id=7)

        # Adiciona os espaços ao banco
        db.session.add_all([espaco1, espaco2, espaco3, espaco4, espaco5, espaco6, espaco7, espaco8, espaco9, espaco10])
        db.session.commit()

        print("Banco de dados populado com dados fictícios!")

# Rodar a aplicação e popular o banco
with app.app_context():
    popular_banco()

from app import app

# Rodar a aplicação com a interface 127.0.0.1
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)