from flask import Flask, render_template, request
import cv2
import os
import random

img_path = r"static/images/"

def get_pic_array(path):
    """ collects the pictures from the folder into an array """
    pictures = []
    for filename in os.listdir(path):
        if filename.endswith('.png'):
            pictures.append(cv2.imread(os.path.join(path, filename), cv2.IMREAD_GRAYSCALE))
    return pictures

def generate_phrase(pictures, number, name):
    """ horizontal image concatenation  """

    if number % 2:
        pass
    else:
        result = cv2.hconcat(random.sample(pictures, number))
        cv2.imwrite(img_path + f"result/{name}.png", result)



app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def start():
    if request.method == "POST" and request.form["button"] in "123456789" :
        number = int(request.form["button"])
        if number < 3:
            pictures = get_pic_array(img_path)
            generate_phrase(pictures, number, "result")
            return render_template("start.html", the_title="Here your rhythm",
                                   flag=True)
        else:
            if int(number) == 3:
                pictures = get_pic_array(img_path)
                generate_phrase(pictures, int(number)-1, "result")
                generate_phrase(pictures, int(number)-2, "result_2")
                return render_template("start.html", the_title="Here your rhythm",
                                       flag=True, flag_3=True)
            else:
                pictures = get_pic_array(img_path)
                generate_phrase(pictures, int(number) - 2, "result")
                generate_phrase(pictures, int(number) - 2, "result_2")
                return render_template("start.html", the_title="Here your rhythm",
                                       flag=True, flag_3=True)
    else:
        return render_template("start.html", the_title="Hello")


if __name__ == "__main__":
    app.run(debug=True)