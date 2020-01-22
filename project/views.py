from flask import render_template
from project.app import app, pages

@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=False,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@app.route('/<path:path>/')
def page(path):
    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'page.html')
    return render_template('page.html', page=page)
