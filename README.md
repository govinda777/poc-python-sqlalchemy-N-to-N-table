# poc-python-sqlalchemy-N-to-N-table

API básica usando a stack especificada, que gerencia dois recursos: `User` e `Group`. Um usuário pode pertencer a vários grupos e um grupo pode ter vários usuários (relacionamento N para N).

Aqui está um plano para a POC:

1. Crie uma estrutura de pastas.
2. Configure o ambiente virtual e instale as dependências.
3. Defina os modelos de banco de dados.
4. Crie as rotas para o CRUD.
5. Inicie o servidor.

## Comandos

poetry init
poetry env use python3.9

poetry add fastapi uvicorn gunicorn sqlalchemy python-dotenv pymysql



**1. Estrutura de Pastas**

```plaintext
/poc_fastapi
|-- /app
|   |-- __init__.py
|   |-- main.py
|   |-- models.py
|   |-- database.py
|   |-- routers
|       |-- users.py
|       |-- groups.py
|-- .env
|-- requirements.txt
```

**2. Ambiente Virtual e Dependências**

Navegue até a pasta `poc_fastapi` e configure o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

`requirements.txt`:

```plaintext
fastapi==0.95.1
uvicorn==0.22.0
gunicorn==20.1.0
sqlalchemy==2.0.14
python-dotenv==1.0.0
pymysql==1.0.3
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

**3. Modelos de Banco de Dados**

`.env`:

```plaintext
DATABASE_URL=mysql+pymysql://[username]:[password]@[host]/[database_name]
```

`app/database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
```

`app/models.py`:

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

association_table = Table(
    'association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    groups = relationship("Group", secondary=association_table, back_populates="users")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship("User", secondary=association_table, back_populates="groups")
```

**4. Rotas CRUD**

Por motivos de brevidade, vou apenas mostrar um esboço da criação das rotas CRUD em `app/routers/users.py`:

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database

router = APIRouter()

@router.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    # lógica para criar um usuário
    pass

# Adicione rotas para Read, Update e Delete, bem como para gerenciar associações de grupo.
```

**5. Iniciar o Servidor**

`app/main.py`:

```python
from fastapi import FastAPI
from app.routers import users, groups

app = FastAPI()

app.include_router(users.router)
app.include_router(groups.router)
```

Execute:

```bash
uvicorn app.main:app --reload
```

Agora você pode acessar a documentação da API em `http://127.0.0.1:8000/docs` e testar as rotas.

Esse é um esboço muito básico e há muitos aspectos, como tratamento de erros e segurança, que precisariam ser abordados em uma aplicação real.
