from flask import Flask
import random

app = Flask(__name__)

dogData = [
    {"dogIMG": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTn4ir7qxd2_RlqMp6l12zjeLI_EE3sO1ulMZYDrHrlN-x2SbHu",
    "Breed": "German Shepherd"},
    {"dogIMG": "https://cdn.outsideonline.com/wp-content/uploads/2023/03/Funny_Dog_S.jpg",
    "Breed": "Chihuahua"},
    {"dogIMG": "https://images.ctfassets.net/u6v061izp9oz/3QZwNflk6BXx6Xl9VhB2Zg/4df3c9f91da5627121f8d9a2be1ab0db/english-bulldog-5422018_1280.jpg",
    "Breed":  "Bulldog"},
    {"dogIMG": "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2023/02/09141023/Diana-the-Poodle-500x485.jpg",
    "Breed": "Poodle"},
    {"dogIMG": "https://www.akc.org/wp-content/uploads/2017/11/Shiba-Inu-puppy-standing-outdoors.jpg",
    "Breed": "Shiba inu"}]

@app.route("/<name>/<day>")
def hello_world(name, day):
    return "Hello" + name + "today is " + day

@app.route("/<number>/")
def number_world(number):
    if int(number) > 10:
        return number + " is greater than 10"
    elif int(number) < 10 : 
        return  number + " is less than 10"

@app.route("/api/<key>")
def api(key):
    for dog in dogData:
        if dog["Breed"] == key:
            return dog 
    return "No dog found"

    #dogIMG = dogData
    #return random.choice(dogIMG("dogIMG"))
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
