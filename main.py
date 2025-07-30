from flask import Flask, render_template, abort
from src import fn
from typing import List
import os

app = Flask(__name__)
FILE_DIRECTORY = "src/final/"


@app.route("/")
def index():
    directory: List[str] = fn.read_directory(FILE_DIRECTORY)
    directory = [d.split(".")[0] for d in directory]
    return render_template("index.html", listing=directory)


@app.route("/r/<subreddit>")
def listing_redirect(subreddit: str):
    filename = f"{subreddit}.json"
    filepath = os.path.join(FILE_DIRECTORY, filename)
    if os.path.exists(filepath):
        data = fn.read_json_file(filepath)
        return render_template("listing.html", subreddit=subreddit, data=data)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
