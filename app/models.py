from app import db

# Modelo de Loja
class Loja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    
    # Relacionamento com espaços publicitários
    espacos = db.relationship('Espaco', backref='loja', lazy=True)

    def __repr__(self):
        return f'<Loja {self.nome}>'

# Modelo de Marca
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
    # Relacionamento com espaços publicitários
    espacos = db.relationship('Espaco', backref='marca', lazy=True)

    def __repr__(self):
        return f'<Marca {self.nome}>'

# Modelo de Espacos Publicitarios
class Espaco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    
    # Relacionamento com loja e marca
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)

    def __repr__(self):
        return f'<Espaco {self.nome}>'
