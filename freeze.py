from flask_frozen import Freezer
from app import create_app

# Create flask app
app = create_app()

# Configure freezer with Base URL for GitHub Pages
# Use the repo name "ai-security-portfolio" for now,
# but it's safe to assume standard gh-pages URLs usually have a base path.
# However, if using a custom CNAME, this might change.
# For now, let's use relative URLs which is safer for portability.
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
