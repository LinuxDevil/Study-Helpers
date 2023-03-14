import argparse
import requests
from bs4 import BeautifulSoup
from lighthouse import lighthouse

class Test:
    def __init__(self, url):
        self.url = url
    
    def run(self):
        self._run_seo_tests()
        self._run_performance_tests()
        self._run_best_practices_tests()
        self._run_accessibility_tests()

    def _run_seo_tests(self):
        response = requests.get(self.url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        title = soup.title.text
        if len(title) < 50:
            print('Title tag is too short: {}'.format(title))

        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if not meta_desc or len(meta_desc.get('content', '')) < 120:
            print('Meta description is too short or missing')

        h1_tags = soup.find_all('h1')
        if len(h1_tags) == 0:
            print('No H1 tags found')

        img_tags = soup.find_all('img')
        if len(img_tags) == 0:
            print('No images found')

    def _run_performance_tests(self):
        results = lighthouse(self.url, config_path={'extends': 'lighthouse:default', 'settings': {'emulatedFormFactor': 'desktop'}},
                              flags={'onlyCategories': ['performance']})
        print('Performance score:', results['categories']['performance']['score'])

    def _run_best_practices_tests(self):
        results = lighthouse(self.url, config_path={'extends': 'lighthouse:default', 'settings': {'emulatedFormFactor': 'desktop'}},
                              flags={'onlyCategories': ['best-practices']})
        print('Best practices score:', results['categories']['best-practices']['score'])

    def _run_accessibility_tests(self):
        results = lighthouse(self.url, config_path={'extends': 'lighthouse:default', 'settings': {'emulatedFormFactor': 'desktop'}},
                              flags={'onlyCategories': ['accessibility']})
        print('Accessibility score:', results['categories']['accessibility']['score'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run SEO, performance, best practices, and accessibility tests on a website.')
    parser.add_argument('url', help='URL of website to test')
    args = parser.parse_args()

    test = Test(args.url)
    test.run()
