# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify#, render_template, 
#from web_app.services.twitter_service import twitter_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    print(screen_name)
    return f"Fetched {screen_name} OK"