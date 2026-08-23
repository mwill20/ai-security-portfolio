from datetime import datetime

from flask import Flask, render_template

try:
    from projects_data import projects as projects_list
except ImportError:
    projects_list = {}


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.context_processor
    def inject_now():
        return {'now': datetime.now()}

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/projects/')
    def projects():
        return render_template('projects.html', projects=projects_list)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
