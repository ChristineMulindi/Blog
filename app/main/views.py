from flask import render_template, request, redirect, url_for,abort
from . import main
from ..request import get_quote






@main.route('/blog/<int:id>')
def blog(id):

    quote = get_quote(id)
    author = f'{blog.author}'
    return render_template('blog.html', author=author, quote = quote)