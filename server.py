"""
Emotion Detection Server

This module implements a Flask server for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formatted_response = emotion_predictor(response)
    if formatted_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formatted_response['anger']} "
        f"'disgust': {formatted_response['disgust']}, 'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']} and 'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()
