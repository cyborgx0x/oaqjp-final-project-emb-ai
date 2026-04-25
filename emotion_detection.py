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
    formatted_data = json.loads(response.text)
    # get the emotion value
    emotion = formatted_data.get("emotionPredictions")[0].get("emotion")
    # get the score
    anger_score = emotion.get("anger")
    disgust_score = emotion.get("disgust")
    fear_score = emotion.get("fear")
    joy_score = emotion.get("joy")
    sadness_score = emotion.get("sadness")
    # get the dominant_emotion by using max filter
    emotion_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
    }
    max_value = max(emotion_dict.values())
    dominant_emotion = ""
    for key in emotion_dict.keys():
        if emotion_dict[key] == max_value:
            dominant_emotion = key
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }


# test

emotion_detector("I love this new technology.")