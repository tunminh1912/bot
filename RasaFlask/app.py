from flask import Flask, jsonify, render_template, request
import requests

#  URL nơi server Rasa đang chạy. Flask app sẽ gửi tin nhắn người dùng đến URL này.
RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    #send user message to rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Xin lỗi, tôi không hiểu yêu cầu của bạn.'
    return jsonify({'response': bot_response})


if __name__ == "__main__":
    app.run(debug=True, port=3000)
