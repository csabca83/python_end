import time, urllib, json, threading
from queryxlsx import Readexcel
from bot import Bot
from contextlib import contextmanager
from app import extract_json

#Creating a scheduled job that can run on a specified time, in windows this can be used with task scheduler,
#in linux with crontab or in our case we can do scheduled python execution with heroku scheduler

def check_cron():
    
    #Extracting data from the JSON file
    dicto = {}
    dicto2 = extract_json()
    dicto['ACCESS_TOKEN'] = dicto2['ACCESS_TOKEN']
    dicto['USER_ID_1'] = dicto2['ADRI']
    dicto['USER_ID_2'] = dicto2['CSABI']
    ACCESS_TOKEN = dicto2['ACCESS_TOKEN']

    #Using the same function that we used inside of the class_for_functions module, because here we're just
    #scheduling the word cron under the excel sheet.
    file_name, headers = urllib.request.urlretrieve('https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3gvcyFBbTg1bXlhQXk0dUxzeXBGTmtuejN4TUpndkR3P2U9bTJkMkJK/root/content')
    path = file_name
    x = Readexcel(path=path, ACCESS_TOKEN=ACCESS_TOKEN)
    print('\x1b[1;32;40m' + "~~~~~~~QUERYING THE CRON TEXT NOW~~~~~~~" + '\x1b[0m')
    x.import_excel()
    x.append_items()
    #Trying to find a value for cron inside of the sheet, but if there is no value we automatically set it to False
    try:
        x.append_items_2(text_input='cron')
        x.find_answer(user_id="cron")
        print('\x1b[6;30;42m' + "Cron's value is " + x.random_answers + '\x1b[0m')
    except IndexError:
        x.random_answers = False
        print('\x1b[6;30;42m' + "Cron's value is False" + '\x1b[0m')
    dicto['state'] = bool(x.random_answers)

    #Doesn't matter what kind of text is the value, if there is a text we treat that as True and
    #we return the value to function in a dict format, where we modify the state value depends on the excel value.

    return dicto

#We're setting up the cron based on time + we're passing the values(from the previous function) to the function during the call
def run_functions(state, ACCESS_TOKEN, USER_ID_1, USER_ID_2):
    print('\x1b[1;33;42m' + "~~~~~~~~~~~~CRON INITIATED~~~~~~~~~~~~" '\x1b[0m')
    
    #Here we decide how the function should run, depending on the boolean value.

    if state == True:
        t = time.localtime(time.time() + 7200)
        value = time.strftime("%H" + "%M", t)
        value = int(value)

        #Adding time as an extra value to the class

        s = Messages(value, ACCESS_TOKEN, USER_ID_1, USER_ID_2)

        #Calling the functions inside of the class with a for loop by using exec, if the function name is out of index
        #python generates an attribute error that we're ignoring with a try and except statement.

        for items in range (1, 10):
            try:
                exec(f"s.message{items}()")
            except AttributeError:
                pass
        print('\x1b[6;30;42m' + "~~~~~ CRON FINISHED ~~~~~" + '\x1b[0m')

    else:
        print('\x1b[0;30;41m' + "!!!Cron is turned off!!!" + '\x1b[0m')
        pass

class Messages:
    
    #Storing the variables + we're importing the bot function and we're storing it under a self variable, that can be called
    #later in the functions
    def __init__(self, value, ACCESS_TOKEN, USER_ID_1, USER_ID_2):
        from bot import Bot
        self.value=value
        self.ACCESS_TOKEN=ACCESS_TOKEN
        self.USER_ID_1=USER_ID_1
        self.USER_ID_2=USER_ID_2
        self.bot = Bot(self.ACCESS_TOKEN)
    
    #Every function here is almost the same, it's just a simple text that we're sending back depends on the time value
    #which is an integer, for example: The time was requested with %H + %M (which was the current hour and minute) and if
    #for example the script ran at 8:00 o clock in the morning it would be 800 which would fall between the ~< 810 and 800 > 750
    #statement (it means the message1 would be triggered).

    def message1(self):

        if self.value < 810 and self.value > 750:
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_1}', 'Jóreggelt :), teljen jól a napod :)']).start()
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_2}', 'Jóreggelt :), teljen jól a napod :)']).start()
        else:
            pass

    def message2(self):

        if self.value < 1210 and self.value > 1150:
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_1}', 'Jóétvágyat :)']).start()
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_2}', 'Jóétvágyat :)']).start()
        else:
            pass

    def message3(self):

        if self.value < 1610 and self.value > 1550:
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_1}', 'Remélem jól telik a délutánod :)']).start()
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_2}', 'Remélem jól telik a délutánod :)']).start()
        else:
            pass

    def message4(self):

        if self.value < 2140 and self.value > 2120:
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_1}', 'Jóéjt és Szép álmokat :)']).start()
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_2}', 'Jóéjt és Szép álmokat :)']).start()
        else:
            pass

    def message5(self):

        from bs4 import BeautifulSoup
        import requests

        r = requests.get('https://transferwise.com/hu/currency-converter/huf-to-eur-rate')

        soup = BeautifulSoup(r.content, 'lxml')

        wrap_number_hufeur = soup.find('span', class_="text-success")

        value = wrap_number_hufeur.text

        value = float(value.replace(",", "."))

        if value < 0.0028:
            pass

        else:
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_1}', '0.0028 érték felett van a forint, válthatsz.']).start()
            threading.Thread(target=self.bot.send_text_message, args=[f'{self.USER_ID_2}', '0.0028 érték felett van a forint, válthatsz.']).start()

#Created this if__main__ statement as well for heroku (because it can just execute a file during a specified time) and
#we want also to import the functions without executing them directly during the import.
if __name__ == "__main__":
    print('\x1b[1;34;40m' + "SCHEDULER RUNS THE SCRIPT" + '\x1b[0m')
    dicto = check_cron()
    run_functions(dicto['state'], dicto['ACCESS_TOKEN'], dicto['USER_ID_1'], dicto['USER_ID_2'])