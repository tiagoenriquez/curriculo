# Currículo

Esta aplicação permite cadastro de algumas informações importantes para constar em um currículo. Foi baseada no currículo disponibilizado pelo Linkedin. Permite incluir informações sobre:
<li>Meios de contato</li>
<li>Competências</li>
<li>Experiências</li>
<li>Resumo</li>
<br>
Permite também gerar o currículo tanto em português como em inglês, e com a quantidade de competências definida pelo usuário.
<br>
Esta aplicação foi desenvolvida em Python com o framework Django. Os dados são persistidos em arquivo do SQLite. O cadastro das informações é feita em telas geradas pelo próprio framework. E os currículos são acessados em telas desenvolvidas com Django Templates, um template engine que já vem instalado com o Django. Não foi utilizada nenhuma biblioteca ou framework em javascript nesta aplicação.
<br>
Para fazer esta aplicação funcionar, primeiro é necessário criar o ambiente virtual, digitando em linha de comando:


```
python -m venv venv
```

Depois, é preciso entrar no ambiente virtual, digitando o comando que varia a depender do sistema operacional. No Linux, o comando é:

```
source venv/bin/activate
```

Em seguida, é preciso instalar as dependências, com o comando:

```
pip install -r requirements.txt
```

Então, é necessário rodar as migrações, com:

```
python manage.py migrate
```

Depois, é possível fazer o sistema funcionar, com o comando:

```
python manage.py runserver
```

Com este comando, a aplicação ficará disponível no navegador de internet na URL http://localhost:8000.
<br>
Para cadastrar os dados que alimentarão o currículo, primeiro é necessário criar um super usuário com o seguinte comando:

```
python manage.py createsuperuser
```

Este comando vai abrir um programa em linha de comando que vai perguntar os dados de usuário. Depois de cadastrar o usuário, é possível cadastrar os dados na URL http://localhost:8000/admin, depois de informar os dados do usuário.
