from abc import ABCMeta, abstractmethod
import win32api
import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
from DataMovie import DataMovie

class Parser():
    def __init__(self,url):
        self.url = url
        print(self.url)
        self.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Cookie':'_csrf = 9h4LMeGUDgoJqAFqt - HGcS9Y;_yasc = l9pK9jLgGTILiAeKydbeCCJXUM1qc2 / 3U3mxzOstNj4CcLOZ;i = jn1L / y9vCYRwjSQYQMWyHgDwRCY2p47RVngKeuEGDVZ2WIa / O1WUCdWOspBa2bRWPzbxszfLJ3 + vJJG8ySp3h0mfscc =;desktop_session_key = e048fe0c457672b4f1a48b083ac12afd44ce6d71e803daefbc3bcc2ad3b023f27a64e3d7358ce5d369b2a6abb4a51804d9a51785e02b6660aa68329b1c64031faa02ec5a919d1f103b0246cd81bd364b844fe1a373b48975d2437fba5209dc31;desktop_session_key.sig = ixrElFIqgvSZ4Vu4CBdonfvqL40;gdpr = 0;_ym_uid = 1649850983581838880;_ym_d = 1649914691;yandex_login =;ys = c_chck.567485842;yandexuid = 1753880571642154811;mda2_beacon = 1649913076622;crookie = VGLO8fS / ZaLH / OxbcUP + fGJdVxqqV9jSU // 1XhwefPoG8jSB6cvlkLKJ85IIi1BgUxMO0m8tWcj6Oczeaxw9n7pgL0g =;cmtchd = MTY0OTg1MDk4NDk5Mg ==;_ym_isad = 1;location = 1;ya_sess_id = noauth:1649913076;sso_status = sso.passport.yandex.ru:synchronized',
                                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}
    async def parsingUrl(self):
        async with aiohttp.ClientSession(headers = self.headers) as session:
                async with session.get(self.url) as resp:
                    #print(await resp.text())
                    try:
                        if resp.status != 200:
                            raise ValueError
                    except ValueError as e:
                        print(e)
                        pass

                    request =  BeautifulSoup(await resp.text(), 'lxml')
                    list_ROM_div = request.find_all('div','styles_root__3a8vf')
                    for i in range(0,len(list_ROM_div)-1):
                        await self.saveTxt(list_ROM_div[i])


    async def saveTxt(self,itemListROMdata):
        dataOnWrite = DataMovie(itemListROMdata)

        with open('parsingInfo.txt','a',encoding="utf-8") as f:
            try:
                await f.write('\n'+str(dataOnWrite),)
            except TypeError as e:
                str(e)
                #print(dataOnWrite)

