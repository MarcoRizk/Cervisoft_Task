#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Marco Rizk'
__email__ = 'marco.r.eissa@gmail.com'
__version__ = '1.3'

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from CervisoftTask.controllers.main import main
from CervisoftTask import assets
from CervisoftTask.models import db

from CervisoftTask.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. CervisoftTask.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    return app
