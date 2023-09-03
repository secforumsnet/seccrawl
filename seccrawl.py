import logging
import requests
from pystyle import Colors, Colorate
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import csv

R = '\033[3m'  
G = '\033[32m'  
W = '\033[0m'   
C = '\033[96m'

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)


class Crawler:
    def __init__(self, url, max_depth=3):
        self.visited_urls = []
        self.urls_to_visit = [(url, 0)]
        self.max_depth = max_depth

    def download_url(self, url):
        response = requests.get(url)
        response.raise_for_status()  
        return response.text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url, depth):
        if url not in self.visited_urls and (url, depth) not in self.urls_to_visit and depth <= self.max_depth:
            self.urls_to_visit.append((url, depth))

    def crawl(self, url, depth):
        html = self.download_url(url)
        for linked_url in self.get_linked_urls(url, html):
            self.add_url_to_visit(linked_url, depth + 1)
            


    def export_results(self, output_file):
        # Export visited URLs and depths to a CSV file
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            # Write header row
            writer.writerow([""])
            # Write data rows
            for item in self.visited_urls:
                writer.writerow([item['url']])

    def run(self):
        while self.urls_to_visit:
            url, depth = self.urls_to_visit.pop(0)
            logging.info(f'{C}Crawling: {url} (Depth: {depth}){W}')
            try:
                self.crawl(url, depth)
            except requests.exceptions.RequestException as e:
                logging.error(f'{R}Failed to crawl: {url} - {e}{W}')
            except KeyboardInterrupt:
                print('\n'f'{R}[!] Keyboard Interrupt!{R}')
                break
            except Exception as e:
                logging.exception(f'{R}Failed to crawl: {url} - {e}{W}')
            finally:
                self.visited_urls.append({'url': url, 'depth': depth})
            


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, W + """
    
░██╗░░░░░░░██╗███████╗██████╗░  ░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝  ██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗  ██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝  ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝
𝖻𝗒 𝖲𝖤𝖢𝖥𝖮𝖱𝖴𝖬𝖲.𝖭𝖤𝖳

    """ + W))
    url = input(f"{R} TARGET:")
    max_depth = int(input(f"{R}Max Depth: "))
    output_file = input('Output File (e.g., results.json): ')
    crawler = Crawler(url, max_depth=max_depth)
    crawler.run()
    crawler.export_results(output_file)
