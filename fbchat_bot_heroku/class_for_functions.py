class Functions:
    def __init__(self, ACCESS_TOKEN):
        self.ACCESS_TOKEN = ACCESS_TOKEN



    def function1(self, user_id):
        import time
        t = time.localtime(time.time() + 7200)
        self.value = time.strftime("%H:%M:%S", t)

    def function2(self, user_id):
        
        from bot import Bot
        import time
        import threading

        #RICK ASTLEEEEY#
        bot = Bot(self.ACCESS_TOKEN)
        threading.Thread(target=bot.send_text_message, args=[f'{user_id}', "We're no strangers to love\nYou know the rules and so do I\n \
                                                                            A full commitment's what I'm thinking of\nYou wouldn't get this from \
                                                                            any other guy\nI just wanna tell you how I'm feeling\nGotta make you understand\n\
                                                                            Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert \
                                                                            you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you"]).start()
        threading.Thread(target=bot.send_image_by_id, args=[f'{user_id}', '320946389156236']).start()

    
    def function3(self, user_id):
        #RACOOOON

        from bot import Bot
        import threading
        from random import choice

        bot = Bot(self.ACCESS_TOKEN)
        random_racoon = choice(['372593837093422', '344456233269789', '702376980356371', '947112995783361'])
        threading.Thread(target=bot.send_image_by_id, args=[f'{user_id}', f'{random_racoon}']).start()

    def function4(self, user_id):
        from bs4 import BeautifulSoup
        import requests

        r = requests.get('https://www.idokep.hu/30napos/Budapest')


        soup = BeautifulSoup(r.content, 'lxml')

        wrap_kilatasok = soup.find_all('div', class_='kilatasok-szoveg')
        wrap_buborek_fejlec = soup.find_all('div', class_="buborek-fejlec")
        wrap_buborek_oszlop = soup.find_all('div', class_="oszlop")

        kozos = []

        kozos.append(wrap_kilatasok[0].h3.text)
        kozos.append(wrap_kilatasok[0].find_all('p')[0].text)
        kozos.append(wrap_kilatasok[0].find_all('p')[1].text)

        while_loop = 0

        while int(while_loop) <= 7:
            kozos.append('~~~~~~~~~~~~~~')
            kozos.append(wrap_buborek_fejlec[while_loop].text)
            wrap_felhos_text = wrap_buborek_oszlop[while_loop].find_all('div', class_='buborek-text')
            for items in wrap_felhos_text:
                kozos.append(items.find('strong', class_='felhos-text').text)
            while_loop  = while_loop + 1


        self.value = ('\n'.join(map(str, kozos)))

    def function5(self, user_id):
        from bs4 import BeautifulSoup
        import requests

        r = requests.get('https://index.hu/24ora')

        soup = BeautifulSoup(r.content, 'lxml')

        wrap_text = soup.find_all('div', class_="article-container")

        kozos = []
        while_loop = 0

        while int(while_loop) <= 4:
            kozos.append(wrap_text[while_loop].a.img.get('alt'))
            kozos.append(wrap_text[while_loop].a.get('href'))
            kozos.append('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            while_loop  = while_loop + 1
        self.value = ('\n'.join(map(str, kozos)))

    def function6(self, user_id):
        from bs4 import BeautifulSoup
        import requests

        kozos = []

        r = requests.get('https://transferwise.com/hu/currency-converter/huf-to-eur-rate')
        s = requests.get('https://transferwise.com/hu/currency-converter/eur-to-huf-rate')

        soup = BeautifulSoup(r.content, 'lxml')
        soups = BeautifulSoup(s.content, 'lxml')

        wrap_title_hufeur = soup.find('h3', class_="colored-dot")
        wrap_text_hufeur = soup.find('h3', class_="cc__source-to-target hidden-xs")
        wrap_title_eurhuf = soups.find('h3', class_="colored-dot")
        wrap_text_eurhuf = soups.find('h3', class_="cc__source-to-target hidden-xs")

        while_loop = 1

        kozos.append(wrap_title_hufeur.text)

        while int(while_loop) <= 3:
            kozos.append(wrap_text_hufeur.find_all('span')[while_loop].text)
            while_loop  = while_loop + 1

        kozos.append('~~~~~~~~~~~~~~~~~~~~~~~~')

        kozos.append(wrap_title_eurhuf.text)

        while int(while_loop) <= 6:
            kozos.append(wrap_text_eurhuf.find_all('span')[while_loop - 3].text)
            while_loop  = while_loop + 1

        self.value = ('\n'.join(map(str, kozos)))
