from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)
app.config["DEBUG"] = True
apiURL = "http://www.omdbapi.com/?"

@app.route("/")
def start():
    return render_template('hello.html')

@app.route("/movie/<title>")
def get_movie(title):
    parameters = {'t':title}
    r = requests.get(apiURL,params=parameters)
    results = json.loads(r.text)
    print results
    plot = results['Plot']
    poster = results['Poster']
    return render_template('movie.html',movie=title,plot=plot,poster=poster)

if __name__ == "__main__":
    app.run()


# parameters = {'access_token': token,"message":"I sent this using the Facebook API, I hope it works!!!"}
#
# r = requests.get('https://graph.facebook.com/v2.5/me/inbox', params=parameters)
# result = json.loads(r.text)
# print result
