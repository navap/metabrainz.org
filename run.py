﻿from werkzeug.serving import run_simple
from metabrainz import create_app

application = create_app()

if __name__ == '__main__':
    application.run('0.0.0.0', 8080)
