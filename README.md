# Eventex

Sistem de Eventos 

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtual env com python 3.10+
3. ative o virtual env
4. Instale as denpendências
5. Configure a instância com o .env
6. execute os testes.

```console	
git clone https://github.com/limeira94/wttd-project.git
cd wttd
python -m venv .wttd
.\wttd\scripts\activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
Heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
