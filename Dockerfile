# Usando uma imagem base com Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt
COPY requirements.txt .

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o conteúdo da aplicação
COPY . .

# Expor a porta 5000 (porta padrão do Flask)
EXPOSE 5000

# Rodar o app
CMD ["python", "run.py"]
