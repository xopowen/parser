import asyncio
from bs4 import BeautifulSoup

import paser
from paser import Parser

main_task = []
for i in range(1,6):
   i = Parser('https://www.kinopoisk.ru/lists/movies/top250/?page=' + str(i))
   main_task.append(i.parsingUrl())

async def main():
   await asyncio.gather(*main_task)
asyncio.run(main())