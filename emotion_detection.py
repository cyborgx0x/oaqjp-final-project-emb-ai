import requests
import json

def emotion_detector(text_to_analyze) -> str:
    '''
    return the emotion based on given input text
    send the request to emotion watson service 
    '''
    # register neccessary information
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, data=json.dumps(input_data), headers=headers)
    return response.text


# test

emotion_detector("I love this new technology.")