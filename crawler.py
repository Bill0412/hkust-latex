import urllib.request
from bs4 import BeautifulSoup
import ssl

class Crawler:
    def _crawl_html(self, uri):
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

    # this functions crawls a single page LaTex file.
    # uri: the uri of the page that contains latex
    # filename: the name of the file to be saved
    def crawl_single_page_latex(self, uri, filename):
        # beautiful soup
        html = self._crawl_html(uri)

        soup = BeautifulSoup(html, 'html.parser')

        # get the plain latex
        latex = soup.find('div', class_="highlight").text

        self._save_latex(latex, filename)

    def block_test(self):
        crawler.crawl_single_page_latex('http://www.texample.net/tikz/examples/city/', 'city')

if __name__ == '__main__':
   crawler = Crawler()
   crawler.block_test()
