import urllib.request
from bs4 import BeautifulSoup
import ssl



# path: relative path of the uri
def crawl_html(uri):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(uri, context=ctx).read()
    return html


# this functions crawls a single page LaTex file.
def crawl_single_page_latex(uri):
    # beautiful soup
    html = crawl_html(uri)

    soup = BeautifulSoup(html, 'html.parser')

    latex = soup.find('div', class_="highlight").text

    return latex

# this function saves a latex string as a .tex file
def save_latex(latex)
    pass


if __name__ == '__main__':
    print(crawl_single_page_latex('http://www.texample.net/tikz/examples/city/'))