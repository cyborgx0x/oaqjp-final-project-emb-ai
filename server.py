'''
this is the server to detect emotion
'''

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home():
    '''
    Home route
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    '''
    this function get the value from param agument and then sen to emotion detector, return a text
    '''
    text = request.args.get('textToAnalyze')
    emotion = emotion_detector(text)
    anger_score = emotion.get("anger")
    disgust_score = emotion.get("disgust")
    fear_score = emotion.get("fear")
    joy_score = emotion.get("joy")
    sadness_score = emotion.get("sadness")
    dominant_emotion = emotion.get("dominant_emotion")
    if not dominant_emotion:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response "
        f"is 'anger': {anger_score},"
        f"'disgust': {disgust_score},"
        f"'fear': {fear_score},"
        f"'joy': {joy_score} "
        f"and 'sadness': {sadness_score}."
        f"The dominant emotion is {dominant_emotion}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
