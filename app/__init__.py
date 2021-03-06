from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.cadastro.cadastro_controller import api as home_ns
from app.main.produtocel.produto_controller import api as cel_ns
from app.main.produtopc.produtopc_controller import api as pc_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

authorizations = {
    'bearer': {
        'name': "Authorization",
        'in': "header",
        'type': "apiKey",
        'description': "Insira o seu Token JWT aqui!"
    }
}
api = Api(app, title='Api Flask HanaH', version='1.0', description='Api de experimentos com python flask',prefix='/api', authorizations=authorizations)


api.add_namespace(home_ns, path='/cadastro')
api.add_namespace(cel_ns, path='/celular')
api.add_namespace(pc_ns, path='/pc')