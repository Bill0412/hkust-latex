import urllib.request
from bs4 import BeautifulSoup
import ssl
import os
import json
from compiler import Compiler


class Crawler:
    def __init__(self, base_path='data/', uri=None):
        self.uri = uri
        self.base_path = base_path
        self.compiler = Compiler()

    def crawl_html(self, uri=None):
        if uri == None:
            uri = self.uri

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            html = urllib.request.urlopen(uri, context=ctx).read()
        except Exception as e:
            print(e)
        return html

    # this function saves a latex string as a .latex file
    def _save_latex(self, latex_doc, tags, filename, tags_dict=None):
        slugname = filename.rsplit('/')[-1]

        # save latex doc
        with open(filename + '/' + slugname + '.latex', 'w') as out:
            out.write(latex_doc)
            out.close()

        # save latex tags
        try:
            for tag in tags:
                if tag not in tags_dict:
                    tags_dict[tag] = list()
                tags_dict[tag].append(slugname)
            with open('data/tags.json', 'w') as out:
                json.dump(tags_dict, out)
                out.close()
        except Exception as e:
            print(e)

    # this functions crawls a single page LaTex file.
    # uri: the uri of the page that contains latex
    # filename: the name of the file to be saved
    # if not specified, it is extracted from the uri
    def crawl_single_page_latex(self, uri, tags_dict=None):
        # beautiful soup
        html = self.crawl_html(uri)

        soup = BeautifulSoup(html, 'html.parser')

        # get the plain latex
        latex_doc = soup.find('div', class_="highlight").text

        # get the category tags
        lis = soup.find('div', class_='tag-list').find_all('li')
        latex_tags = list()
        for li in lis:
            li.span.decompose()
            latex_tags.append(li.text)

        # get file name from the uri
        print(uri)
        fileslug = uri.rsplit('/')[-2]
        print(fileslug)
        target_path = self.base_path + 'latex/{0}'.format(fileslug)
        if not os.path.exists(target_path):
            os.mkdir(target_path)

        self._save_latex(latex_doc, latex_tags, target_path, tags_dict)
        try:
            self.compiler.compile(fileslug)
        except Exception as e:
            print(e)





    def block_test(self):
        # crawler.crawl_single_page_latex('http://www.texample.net/tikz/examples/city/', 'city')
        crawler.crawl_single_page_latex('http://www.texample.net/tikz/examples/parallelepiped/', 'parallelepiped')

if __name__ == '__main__':
   crawler = Crawler()
   crawler.block_test()
