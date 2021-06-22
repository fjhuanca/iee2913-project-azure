from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ECGConsumer(AsyncWebsocketConsumer):
    
    groupname = 'ecg'
    async def connect(self):
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # await self.disconnect()
        pass

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val = datapoint['value']
        
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'deprocessing',
                'value': val
            }
        )
        # print('>>>', text_data)

    async def deprocessing(self, event):
        valOther = event['value']
        await self.send(text_data=json.dumps({'value': valOther}))

class SignsConsumer(AsyncWebsocketConsumer):
    
    groupname = 'signs'
    async def connect(self):
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # await self.disconnect()
        pass

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        temp = datapoint['temp']
        bf = datapoint['bf']
        spo = datapoint['spo'],        
        bpm = datapoint['bpm']
        
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'deprocessing',
                'temp': temp,
                'bf': bf,
                'spo': spo,
                'bpm': bpm
            }
        )
        # print('>>>', text_data)

    async def deprocessing(self, event):
        # valOther = event['value']
        new_dict = {k : v for k,v in event.items() if k!='type'}
        # print(new_dict)
        await self.send(text_data=json.dumps(new_dict))