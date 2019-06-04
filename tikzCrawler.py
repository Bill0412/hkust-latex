# It crawls all the latex files at http://www.texample.net/tikz/examples/all/list/ and categorises it
from crawler import Crawler

class TikzCrawler(Crawler):
    def __init__(self):
        self.source_uri = 'http://www.texample.net/tikz/examples/all/list/'

    def _get_links(self):
        pass

    def crawl_all(self):
        # get all the download links
        links = self._get_links()

        # crawl all the pages
        for link in links:
            self.crawl_single_page_latex(link)

