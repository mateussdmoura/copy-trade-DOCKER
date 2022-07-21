from flask import Flask

CHAIN_ID=3

def create_app():
    app = Flask(__name__)
    app.config['SECRETE_KEY'] = '12345'
  
    from . import load_vars

    from .views import views
    app.register_blueprint(views,url_prefix='/')
    
    from . import connect
    
    return app
