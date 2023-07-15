import asyncio
from urllib.parse import urljoin
import aiohttp
import json
from bs4 import BeautifulSoup
import os


async def get_html(session, url):
    async with session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}) as response:
        return await response.text()


async def parse_marks(html):
    soup = BeautifulSoup(html, 'html.parser')
    marks_div = soup.find('div', id='all-marks')
    marks = []
    for link in marks_div.find_all('a'):
        mark_text = link.text
        mark_href = link['href']
        marks.append({'text': mark_text, 'href': mark_href})
    return marks


async def parse_models(session, base_url, marks):
    all_models = []
    for mark in marks:
        url = urljoin(base_url, mark['href'])
        html = await get_html(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        models_div = soup.find('div', id='all-models')
        models = [h3.text for h3 in models_div.find_all('h3')]
        all_models.append({'mark': mark['text'], 'models': models})
    return all_models


async def save_to_json(data, filename):
    os.makedirs('datasets', exist_ok=True)
    filepath = os.path.join('datasets', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


async def main():
    base_url = 'http://www.motorpage.ru/select-auto/by-mark.html'

    async with aiohttp.ClientSession() as session:
        html = await get_html(session, base_url)
        marks = await parse_marks(html)
        models = await parse_models(session, base_url, marks)
        await save_to_json(models, 'models.json')

if __name__ == '__main__':
    asyncio.run(main())
