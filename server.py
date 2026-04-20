"""Flask server for the EmotionDetection application."""
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyse the emotion of the provided text and return a formatted response."""
    text_to_analyse = request.args.get('textToAnalyse')

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
