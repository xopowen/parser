class DataMovie():
    def __init__(self,itemListROMdata):
        self.data = itemListROMdata
        self.dataMovie = {}

        self._formatDataONexit = ['rating','views','namaMovie','countrie','genre','year','duration','director','rol_1','rol_2']

    def updateDataMovie(self):
        # имя
            self.dataMovie.update({'namaMovie': self.data.find('span', 'styles_mainTitle__3Bgao').string})
    
            yearDuration = self.data.find('span', 'desktop-list-main-info_secondaryText__1ov2X').string.split(',')
            # год
            try:
                self.dataMovie.update({'year': yearDuration[1]})
                # длительность
                self.dataMovie.update({'duration': [int(x) for x in yearDuration[2].split() if x.isdigit()][0] })
            except IndexError as e:
                self.dataMovie.update({'year': 'None'})
                # длительность
                self.dataMovie.update({'duration':  'None' })



            desktop_list_main_info = self.data.find_all('span', 'desktop-list-main-info_truncatedText__2Q88H')
            # страна
            self.dataMovie.update({'countrie': desktop_list_main_info[0].string.split('•')[0]})
            # жанр

            genre_Director = desktop_list_main_info[0].string.split('•')[1].split('  ')[0].split('Режиссёр:')

            self.dataMovie.update({'genre': genre_Director[0]})
    
            # Режисёр
            self.dataMovie.update({ 'director': genre_Director[1]})
    
            rol = desktop_list_main_info[1].string.split(':')[1].split(',')
            print(rol)
            self.dataMovie.update({'rol_1': rol[0] })
            self.dataMovie.update({'rol_2': rol[1]})
    
            # просмотров
            self.dataMovie.update({'views': self.data.find('span', 'styles_kinopoiskCount__1DPG7').string})
            # рейтинг
            self.dataMovie.update({'rating':  self.data.find('span', 'styles_kinopoiskValuePositive__1G4F6 styles_kinopoiskValue__2oNdS').string,})

    @property
    def formatDataONexit(self):
        self.updateDataMovie()
        strintDataMovie = ''
        for i in range(0, len(self._formatDataONexit)):
            if i == len(self._formatDataONexit)-1:
                strintDataMovie += str(self.dataMovie[self._formatDataONexit[i]])
            else :
                strintDataMovie += str(self.dataMovie[self._formatDataONexit[i]])+"/"
        return strintDataMovie

    def __str__(self):
        return self.formatDataONexit