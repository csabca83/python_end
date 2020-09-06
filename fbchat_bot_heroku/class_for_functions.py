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
        threading.Thread(target=bot.send_image_by_id, args=[f'{user_id}', '329441454964466']).start()

    
    def function3(self, user_id):
        #RACOOOON

        from bot import Bot
        import threading

        bot = Bot(self.ACCESS_TOKEN)
        threading.Thread(target=bot.send_image_by_id, args=[f'{user_id}', '4252880948086447']).start()

    def function4(self, user_id):
        from bs4 import BeautifulSoup
        import requests

        r = requests.get('https://www.idokep.hu/30napos/Budapest')


        soup = BeautifulSoup(r.content, 'lxml')

        wrap_homerseklet = soup.find_all('p', class_="zivatar-text")
        wrap_honap = soup.find_all('p', class_="atlag-info")

        kozos = []
        while_loop = 0

        while int(while_loop) <= 10:
            kozos.append(wrap_homerseklet[while_loop].text + "-------")
            kozos.append(wrap_honap[while_loop].text)
            while_loop  = while_loop + 1
        kozos.remove(kozos[0])
        self.value = ('\n'.join(map(str, kozos)))

    def function5(self, user_id):
        from bs4 import BeautifulSoup
        import requests

        r = requests.get('https://index.hu/24ora')

        soup = BeautifulSoup(r.content, 'lxml')

        soup.prettify()

        wrap_text = soup.find_all('div', class_="article-container")

        kozos = []
        while_loop = 0

        while int(while_loop) <= 4:
            kozos.append(wrap_text[while_loop].a.img.get('alt'))
            kozos.append(wrap_text[while_loop].a.get('href'))
            kozos.append('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            while_loop  = while_loop + 1
        self.value = ('\n'.join(map(str, kozos)))
