import os

from flask import Flask, request, jsonify

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType

app = Flask(__name__)

PUBLIC_KEY = os.getenv('PUBLIC_KEY')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(PUBLIC_KEY)
def interactions():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        return jsonify({
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': 'Hello world'
            }
        })
