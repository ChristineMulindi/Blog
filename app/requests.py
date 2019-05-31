import urllib.request, json
from .models import Quote

# Getting the quote base url
base_url = None


def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']


def get_quote(id):
    get_quote_url = base_url.format(id)

    with urllib.request.urlopen(get_quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        quote_object = None
        if quote_response:
            id = quote_response.get('id')
            quote = quote_response.get('quote')
            author = movie_details_response.get('author')
           
            quote_object = Quote(id, quote, author)

    return quote_object