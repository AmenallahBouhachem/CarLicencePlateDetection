from flask import Flask, render_template, request
import os
from Object_Detection import cropped_path
from OCR import extract_text_from_image,save_text_to_file
import pytesseract as pt

pt.pytesseract.tesseract_cmd = '/usr/bin/tesseract'



# webserver gateway interface
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(
    BASE_PATH, 'static/upload/')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH, filename)
        upload_file.save(path_save)
        path_img = cropped_path(path_save, filename)
        text = extract_text_from_image(path_img)
        print(text)
        path_to_save_text = 'static/predict/{}.txt'.format(filename)
        save_text_to_file(text, path_to_save_text)

        return render_template('index.html', upload=True, upload_image=filename, text=text)

    return render_template('index.html', upload=False)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)