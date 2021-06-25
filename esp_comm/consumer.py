from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio

class ECGConsumerSender(AsyncWebsocketConsumer):
    
    groupname = 'ecg_sender'
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
        pass

    async def deprocessing(self, event):
        valOther = event['value']
        await self.send(text_data=json.dumps({'value': valOther}))


class ECGConsumerReceiver(AsyncWebsocketConsumer):
    
    groupname = 'ecg_receiver'
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
            "ecg_sender",
            {
                'type': 'deprocessing',
                'value': val
            }
        )
        # print('>>>', text_data)

    async def deprocessing(self, event):
        pass


class SignsConsumerSender(AsyncWebsocketConsumer):
    
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
        pass

    async def deprocessing(self, event):
        # valOther = event['value']
        new_dict = {k : v for k,v in event.items() if k!='type'}
        # print(new_dict)
        await self.send(text_data=json.dumps(new_dict))


class SignsConsumerReceiver(AsyncWebsocketConsumer):
    
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
            "ecg_sender",
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
        pass



class CamConsumerReceiver(AsyncWebsocketConsumer):
    
    groupname = 'cam'
    async def connect(self):
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # await self.disconnect()
        pass

    async def receive(self, bytes_data):
        
        await self.channel_layer.group_send(
            "cam2",
            {
                'type': 'deprocessing',
                'bytes': bytes_data
            }
        )
        # print('>>>', text_data)
        

    async def deprocessing(self, event):
        pass


class CamConsumerSender(AsyncWebsocketConsumer):
    
    groupname = 'cam2'
    async def connect(self):
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # await self.disconnect()
        pass

    async def receive(self, bytes_data):
        pass
        
    async def deprocessing(self, event):
        # valOther = event['value']
        # print(new_dict)
        await self.send(bytes_data=event["bytes"])