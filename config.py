# instalar pip install python-dotenv
# en la raiz del proyecto crear el archivo .env
# en la raiz del proyecto crear el archivo config.py
# y en este config.py  recuperar las variables con: user = os.environ['MYSQL_USER']
# puedo concatenar como: DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
# despues en el archivo app importar la variable con: from config  import DATABASE_CONNECTION_URI
# y ya puedo usar esa variables.
# en el archivo .gitignore incluir el .env.


from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(os.environ['HELLO'])
