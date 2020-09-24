#The idea behind the script is to have a flask app that can receive GET and make POST requests by using an access token for a facebook page
#The app can only receive authenticated message with a verify token
#The other modules, classes and functions will be imported from other locations, like the Readexcel class

from flask import Flask, request
import json, urllib
from bot import Bot
from contextlib import contextmanager
from queryxlsx import Readexcel
import os, threading, sys

#Creating a function for JSON data extracting, so it can be used in other modules as well.
def extract_json():

    #Using contextmanager as a decorator for our function to safely open the file that contains the credentials
    @contextmanager
    def file(filename, method):
        file = open(filename, method)
        yield file
        file.close()

    with file("tokens.json", "r") as f:
        json_data = json.load(f)
    
    dicto = {}
    dicto['ACCESS_TOKEN'] = json_data['ACCESS_TOKEN']; dicto['VERIFY_TOKEN'] = json_data['VERIFY_TOKEN']
    dicto['ADRI'] = json_data['ADRI']; dicto['CSABI'] = json_data['CSABI']
    #Returning the data as a dictionary, it's easier to manage the data and we don't have to call the function
    #every time when we need some key-value
    return dicto

#Adding the function to a variable so it will be called just once, then the data is being stored under a variable
dicto = extract_json()
ACCESS_TOKEN = dicto['ACCESS_TOKEN']
VERIFY_TOKEN = dicto['VERIFY_TOKEN']

#Assigning the name contributor to our app variable

app = Flask(__name__)

#Creating a route for Flask to enable only GET and POST requests
#Creating a function for the webhook(GET requests) where the webhook can be verified by facebook
#If the request is not a verification from facebook then we use the else statement for POST requests

@app.route('/', methods=['GET', 'POST'])

def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return str(challenge)
        return '400'


    else:
        #Storing the GET or POST request into a data and loading it up with json, since the request is in json format
        #Triggering the bot function that we can use to send data back + passing the access token parameter to it
        data = json.loads(request.data)
        bot = Bot(ACCESS_TOKEN)
        print(data)

        #Extracting the data from the data variable for user_id
        user_id = data['entry'][0]['messaging'][0]['sender']['id']
        
        #Using try and except statements, because the received data can be image or other type of data
        #For now under the except we do not have any values, so nothing will happen if we receive a different kind of data
        #Applying the other module (Readexcel) where the answers are being stored under an excel file called answers.xlsx

        try:
            text_input = str.lower(data['entry'][0]['messaging'][0]['message']['text'])
            print ("Message from user ID {} - {}".format(user_id, text_input))


            #Accessing raw content of the answers.xlsx in onedrive

            file_name, headers = urllib.request.urlretrieve('https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3gvcyFBbTg1bXlhQXk0dUxzeXBGTmtuejN4TUpndkR3P2U9bTJkMkJK/root/content')
            path = file_name
            r = Readexcel(path=path, ACCESS_TOKEN=ACCESS_TOKEN)
            r.import_excel()
            r.append_items()
            #Using the text message that we just received to decide what answer needs to be picked up from the answers.xlsx file
            r.append_items_2(text_input=text_input)
            r.find_answer(user_id)
            #Picking the random answers from the Readexcel module and sending it back to the sender with an access token by using the Bot class
            #This is the first threading that we can see, so if we receive multiple requests at the time all of them will be processed in a
            #different thread. (Threading is also being used in other places)
            if r.random_answers == "":

                print('\x1b[6;30;42m' + "~~~~~ Value had no text, skipping the text delivery ~~~~~" + '\x1b[0m')

            else:

                threading.Thread(target=bot.send_text_message, args=[f'{user_id}', f'{r.random_answers}']).start()
                print('\x1b[6;30;42m' + "~~~~~ Successful text delivery ~~~~~" + '\x1b[0m')
        
        #Error handling around the script and sending the error back through a message
        except:
            print('\x1b[0;30;41m' + "!!! Something went wrong !!!" + '\x1b[0m')
            error_list = []
            for items in sys.exc_info():
                error_list.append(items)
            error = ('\n'.join(map(str, error_list)))
            threading.Thread(target=bot.send_text_message, args=[f'{user_id}', '🤖!!ERROR!!🤖']).start()
            threading.Thread(target=bot.send_text_message, args=[f'{user_id}', f'{error}']).start()
            pass


        return '200'
#Running the flask app on 0.0.0.0 host with the Port that was being assigned by heroku
#The port 5000 will be replaced once heroku assigns a port to our server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)