from flask import Flask
from api_services.news_api.latest_news_api import latest_news
from api_services.news_api.category_api import category_news
from api_services.news_api.summary_api import summarize_news

app = Flask(__name__)


@app.route("/")
def home():
    return "AI News Intelligence System Running"


@app.route("/api/news/latest")
def latest():
    return latest_news()


@app.route("/api/news/category/<category>")
def category(category):
    return category_news(category)


@app.route("/api/news/summarize", methods=["POST"])
def summarize():
    return summarize_news()


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )