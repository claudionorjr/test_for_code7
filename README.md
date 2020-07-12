# Documentação

## Executando o programa em Linux ou windows

### LINUX

***OBS***: Com MakeFile:
- No terminal com o diretório do programa setado:

* `help` para mais informações.
* `installvirtualenv` instala o virtualenv.
* `ambvir` cria um ambiente virtual.
* `start` inicia seu ambiente virtual. 
* `install` instala todas as dependências necessárias. 
* `run` executa o arquivo principal.
* `test` executa os testes unitários.

- Depois é só acessar a rota `http://127.0.0.1:5000/`


***OBS***: Direto no terminal:
- No terminal com o diretório do programa setado:

* `sudo apt install virtualenv` (se ainda não tiver instalado)
* `virtualenv .ambvir --python=python3.7` (instalando o virtualenv `.ambvir`)
* `source .ambvir/bin/activate` (iniciando seu ambiente virtual)
* `pip install -r requirements/base.txt` (instalando todas as dependências necessárias)
* `python app.py` (executando o arquivo principal)
* `pytest -v` (executando os testes unitários)

- Depois é só acessar a rota `http://127.0.0.1:5000/`


### WINDOWS

***OBS***: Direto no terminal:
- No terminal com o diretório do programa setado:

* `pip install virtualenv` (se ainda não tiver instalado)
* `virtualenv .ambvir --python=python3.7` (instalando o virtualenv `.ambvir`)
* `.\.ambvir\Scripts\activate` (iniciando seu ambiente virtual)
* `pip install -r requirements\base.txt` (instalando todas as dependências necessárias)
* `python app.py` (executando o arquivo principal)
* `pytest -v` (executando os testes unitários)

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

# Sobre a conta do usuário
@app.route("/current_user/account")

# Tela de confirmação antes de deletar o usuário
@app.route("/current_user/delete")

# Deleta o usuário logado
@app.route("/current_user/delete/<int:id>")

# Logout do usuário autenticado
@app.route("/logout")

# Lista de Devedores
@app.route("/debtors")

# Sobre os débitos de um respectivo cliente
@app.route("/about_debits/<int:id>", methods=["GET","POST"])

# Deletar um débito de um respectivo cliente
@app.route("/about_debits/<int:id>/delete_debit/<int:debit_id>")

# Editar um débito de um respectivo cliente
@app.route("/about_debits/<int:id>/edit_debits/<int:debit_id>", methods=["GET","POST"])

# Deletar todos os débitos de um cliente
@app.route("/debtors/delete_all_debits/<int:id>")
```


## Framework e bibliotecas adicionais

* Flask
* Flask-SQLAlchemy
* python-dotenv
* flask-wtf
* bootstrap-flask
* flask-login
* pytest
