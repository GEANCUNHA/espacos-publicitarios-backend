from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

# Inicializando o app e o banco de dados
app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///espacos.db'  # Banco local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilitar notificações de alterações no banco

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Configuração do Swagger
SWAGGER_URL = '/swagger'  # A URL onde a documentação do Swagger será acessada
API_URL = '/static/swagger.json'  # Caminho para o arquivo swagger.json

swagger_ui = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Espacos Publicitarios API"
    }
)

# Registra o Swagger UI
app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

# Importa as rotas do projeto
from app import routes
