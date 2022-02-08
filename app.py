from flask import Flask
from flask_cors import CORS
from flask import make_response, jsonify, request
import tempfile
from datetime import datetime
import uuid
import os
from flask_mail import Mail, Message
import matlab.engine
import matplotlib.image as mpimg
import random


eng = matlab.engine.connect_matlab('Engine_1')
# t = eng.sqrt(4.0)
# print(t)

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'martynarutkowska7@gmail.com'
app.config['MAIL_PASSWORD'] = 'jcuwsbmkqnoihesd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



@app.route("/mail", methods=['POST'])
def email():
  msg = Message('Rozpoznanie zmiany skórnej',
                sender='martynarutkowska7@gmail.com',
                recipients=[request.form.get("email")])
  msg.body = "Ten mail został wysłany ze strony xxx. Nie powinien być traktowany jako pewna diagnoza. Aplikacja służy do rozpoznawania łagodnych i złośliwych zmian skórnych." \
             "Aplikacja została oparta na sieci neuronowej o skuteczności 92%. Każdy wynik powinien został potwierdzony przez lekarza." \
             "Twój wynik to: "
  mail.send(msg)
  return "E-mail został wysłany!"

#
@app.route('/')
def start():
    return make_response('Nothing here', 404)


def getNameTemplate():
    return "{}{:=%Y%m%d%H%M%S}".format(str(uuid.uuid4().hex),
                                       datetime.now())



@app.route('/matlab', methods=['POST'])
def receiveFromWebForm():
    if not hasattr(request, 'files'):
        return make_response(jsonify({"response": "no_multiform/data_files_encoded"}), 400)

    receivedFiles = []

    with tempfile.TemporaryDirectory() as tempDir:
        for k in request.files:
            file = request.files[k]
            originalFilename = file.filename
            localFilename = os.path.join(tempDir, getNameTemplate())
            contentType = file.content_type
            file.save(localFilename)
            receivedFiles.append({"received": originalFilename,
                                  "temporary-name": localFilename,
                                  'content-type': contentType})

        id = random.randint(1, 1000)
        image = mpimg.imread(localFilename)
        print('1')
        eng.load(localFilename)
        print('2')
        plik = eng.evalc(r"run C:\Users\marty\Documents\studia\TSwM\projekt\ProjectFlask\kod_matlab.m")
        print('3')
        response = eng.load(r"C:\Users\marty\Documents\studia\TSwM\projekt\ProjectFlask\mat2.mat")
        print('4')
        return response

    #     x = eng.sqrt(4.0)
    #
    # return 'x'

if __name__ == '__main__':
    app.run(debug=True)
