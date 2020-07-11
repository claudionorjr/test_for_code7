# Documentação

## Executando o programa em Linux/windows

### LINUX

***OBS***: Com MakeFile:
- No terminal com o diretório do programa setado:

* `help` para mais informações.
* `installvirtualenv` serve para instalar o virtualenv.
* `ambvir`serve para criar um ambiente virtual.
* `start` serve para iniciar seu ambiente virtual. 
* `install` serve para instalar todas as dependências necessárias. 
* `run` executa o arquivo principal.
* `test` executa os testes unitários.

- Depois é só acessar a rota `http://127.0.0.1:5000/`


***OBS***: Direto no terminal:
- No terminal com o diretório do programa setado:

* `sudo apt install virtualenv` (se ainda não tiver instalado)
* `virtualenv .ambvir --python=python3.7` (instalar o virtualenv `.ambvir`)
* `source .ambvir/bin/activate` (iniciar seu ambiente virtual)
* `pip install -r requirements/base.txt` (instalar todas as dependências necessárias)
* `python app.py` (executa o arquivo principal)
* `pytest -v` (executa os testes unitários)

- Depois é só acessar a rota `http://127.0.0.1:5000/`


### WINDOWS

***OBS***: Direto no terminal:
- No terminal com o diretório do programa setado:

* `pip install virtualenv` (se ainda não tiver instalado)
* `virtualenv .ambvir --python=python3.7` (instalar o virtualenv `.ambvir`)
* `.\.ambvir\Scripts\activate` (iniciar seu ambiente virtual)
* `pip install -r requirements\base.txt` (instalar todas as dependências necessárias)
* `python app.py` (executa o arquivo principal)
* `pytest -v` (executa os testes unitários)

- Depois é só acessar a rota `http://127.0.0.1:5000/`


## Rotas 

### Usuário não autenticado
* url `http://127.0.0.1:5000/`

```python
# Login
@app.route("/", methods=["GET","POST"])

# Register
@app.route("/register", methods=["GET","POST"])
```

### Usuário deve estar autenticado
```python
# Home
@app.route("/current_user")

# Formulário para enviar arquivo na página Home
# ID da empresa cujo o formulário fica na mesma linha da tabela!
@app.route('/current_user/uploader/<int:id>', methods = ['GET', 'POST'])

# Sobre a conta do usuário
@app.route("/current_user/account")

# Tela de confirmação antes de deletar o usuário
@app.route("/current_user/delete")

# Deleta o usuário logado
# ID do usuário logado!
@app.route("/current_user/delete/<int:id>")

# Logout do usuário autenticado
@app.route("/logout")
```


## Framework e bibliotecas adicionais

* Flask
* Flask-SQLAlchemy
* python-dotenv
* flask-wtf
* bootstrap-flask
* flask-login
* pytest
