from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')
    emotion = emotion_detector(text)
    anger_score = emotion.get("anger")
    disgust_score = emotion.get("disgust")
    fear_score = emotion.get("fear")
    joy_score = emotion.get("joy")
    sadness_score = emotion.get("sadness")
    dominant_emotion = emotion.get("dominant_emotion")
    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)