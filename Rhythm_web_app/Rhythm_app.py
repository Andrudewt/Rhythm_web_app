from flask import Flask, render_template, request
import cv2
import os
import random


def get_pic_array(path) -> list:
    """ collects the pictures from the folder into an array """
    pictures = []
    for filename in os.listdir(path):
        if filename.endswith('.png'):
            pictures.append(cv2.imread(os.path.join(path, filename)))  # , cv2.IMREAD_GRAYSCALE
    return pictures


def generate_phrase(pictures, number, name) -> "png file":
    """ horizontal image concatenation randomly
    chosen according to desired quantity """
    result = cv2.hconcat(random.sample(pictures, number))
    if number % 2:
        result = cv2.hconcat((result, extend_pic))
    cv2.imwrite(img_path + f"result/{name}.png", result)


img_path = r"static/images/"
extend_pic = cv2.imread(r"static/images/result/extend.png")
phrase_1 = "Melodic rhythm practicing"
phrase_2 = "Here your rhythm phrase"

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def start() -> "html":
    """ depending on the POST shows one or several pictures  """
    pictures = get_pic_array(img_path)
    if request.method != "POST":
        return render_template("start.html", the_title=phrase_1,
                               phrase_3="Get rhythm a phrases from 22 jazz cliché")
    number = int(request.form["button"])
    if number < 3:
        generate_phrase(pictures, number, "result")
        return render_template("start.html", the_title=phrase_2,
                               flag=True)
    elif number == 3:
        generate_phrase(pictures, number - 1, "result")
        generate_phrase(pictures, number - 2, "result_2")
        return render_template("start.html", the_title=phrase_2,
                               flag=True, flag_3=True)
    else:
        generate_phrase(pictures, number - 2, "result")
        generate_phrase(pictures, number - 2, "result_2")
        return render_template("start.html", the_title=phrase_2,
                               flag=True, flag_3=True)


if __name__ == "__main__":
    app.run(debug=True)