# This module crawls, compiles, categorises all the latex files
# at http://www.texample.net/tikz/examples/all/list/
from crawler import Crawler
from bs4 import BeautifulSoup
import os

class TikzCrawler(Crawler):
    def __init__(self):
        super().__init__()
        self.source_uri = 'http://www.texample.net/tikz/examples/all/list/'
        self.base_uri = 'http://www.texample.net/'
        # self.id = 0
        self.tags = dict()

    def _get_links(self):
        html = self.crawl_html(self.source_uri)

        soup = BeautifulSoup(html, 'html.parser')

        lis = soup.find('div', class_='grid_9').find('ul').find_all('li')

        return [self.base_uri + li.a['href'] for li in lis]


    def crawl_all(self):
        # get all the download links
        links = self._get_links()

        # crawl all the pages
        for link in links:
            slug = link.rsplit('/')[-2]
            if not os.path.exists('data/latex/' + slug):
                self.crawl_single_page_latex(link, self.tags)

    def block_test(self):
        ## Test get_links
        # print(self._get_links())

        # test crawl all
        self.crawl_all()


if __name__ == '__main__':
    tikz = TikzCrawler()
    tikz.block_test()
