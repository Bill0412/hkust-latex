import urllib.request
from bs4 import BeautifulSoup
import ssl

# TODO
# 1. funciton self._save_tags
class Crawler:
    def __init__(self, uri):
        self.uri = uri

    def crawl_html(self, uri=None):
        if uri == None:
            uri = self.uri

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        html = urllib.request.urlopen(uri, context=ctx).read()
        return html

    # this function saves a latex string as a .latex file
    def _save_latex(self, latex_doc, filename):
        with open('data/{0}.latex'.format(filename), 'w') as out:
            out.write(latex_doc)

    def _save_tags(self, tags, filename):
        pass

    # this functions crawls a single page LaTex file.
    # uri: the uri of the page that contains latex
    # filename: the name of the file to be saved
    # if not specified, it is extracted from the uri
    def crawl_single_page_latex(self, uri, filename=None):
        # beautiful soup
        html = self.crawl_html(uri)

        soup = BeautifulSoup(html, 'html.parser')

        # get the plain latex
        latex_doc = soup.find('div', class_="highlight").text

        # get the category tags
        lis = soup.find('div', class_='tag-list').find_all('li')
        tags = list()
        for li in lis:
            li.span.decompose()
            tags.append(li.text)
        # print(tags)

        self._save_latex(latex_doc, filename)
        self._save_tags()

    def block_test(self):
        # crawler.crawl_single_page_latex('http://www.texample.net/tikz/examples/city/', 'city')
        crawler.crawl_single_page_latex('http://www.texample.net/tikz/examples/parallelepiped/', 'parallelepiped')

if __name__ == '__main__':
   crawler = Crawler()
   crawler.block_test()
