import requests
import json

FACEBOOK_URL = 'https://graph.facebook.com/v8.0/me/'


class Bot(object):
    def __init__(self, access_token, api_url=FACEBOOK_URL):
        self.access_token = access_token
        self.api_url = api_url


    def send_text_message(self, psid, message, messaging_type="RESPONSE"):

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'messaging_type': messaging_type,
            'recipient': {'id': psid},
            'message': {'text': message}
        }

        params = {'access_token': self.access_token}
        api_url = self.api_url + 'messages'
        response = requests.post(api_url, headers=headers, params=params, data=json.dumps(data))

        print(response.content)
        print(data)

    def upload_image_url(self, image_url, messaging_type="RESPONSE"):

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'message': {'attachment':
                                {'type': 'image', 'payload':
                                                        {'is_reusable': True,'url': image_url
                                                        }
                                }
                        }
                }

        params = {'access_token': self.access_token}
        api_url = self.api_url + 'message_attachments'
        response = requests.post(api_url, headers=headers, params=params, data=json.dumps(data))

        print(response.content)
        print(data)        

    def send_image_by_id(self, psid, attachment_id, messaging_type="RESPONSE"):

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
                'recipient':{
                    'id': psid
                },
                'message':{
                    'attachment':{
                        'type':'image',
                        'payload':{
                            'attachment_id': attachment_id
                        }
                    }
                }
        }

        params = {'access_token': self.access_token}
        self.api_url = self.api_url + 'messages'
        response = requests.post(self.api_url, headers=headers, params=params, data=json.dumps(data))

        print(response.content)
        print(data)        

#-----------------Send message API-------------------
#curl -X POST -H "Content-Type: application/json" -d '{
#  "messaging_type": "<MESSAGING_TYPE>",
#  "recipient": {
#    "id": "<PSID>"
#  },
#  "message": {
#    "text": "hello, world!"
#  }
#}' "https://graph.facebook.com/v8.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"

#-------------Upload image API------------
#curl -X POST -H "Content-Type: application/json" -d '{
  #"message":{
    #"attachment":{
      #"type":"image", 
      #"payload":{
        #"is_reusable": true,
        #"url":"http://www.messenger-rocks.com/image.jpg"
      #}
    #}
  #}
#}' "https://graph.facebook.com/v8.0/me/message_attachments?access_token=<PAGE_ACCESS_TOKEN>"

#-----------------SEND image API------------- 
#curl -X POST -H "Content-Type: application/json" -d '{
  #"recipient":{
    #"id":"1254459154682919"
  #},
  #"message":{
    #"attachment":{
      #"type":"image", 
      #"payload":{
        #"attachment_id": "1745504518999123"
      #}
    #}
  #}
#}' "https://graph.facebook.com/v8.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
