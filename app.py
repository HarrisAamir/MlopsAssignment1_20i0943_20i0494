from model import getLabel
from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    custom_text = data['text']
    return getLabel(custom_text)


# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
