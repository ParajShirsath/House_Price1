
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import HousePrice
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to House Price Prediction")
    return render_template("index.html")

@app.route('/predict_charges', methods = ["POST", "GET"])
def get_insurance_charges():

    if request.method == "GET":
        print("We are using GET Method")  

        # age = int(request.args.get("age"))
        # sex = request.args.get("sex")
        # bmi = float(request.args.get("bmi"))
        # children = int(request.args.get("children"))
        # smoker = request.args.get("smoker")
        # region = request.args.get("region")

        availability=request.args.get("availability")
        area_type=request.args.get("area_type")
        size=request.args.get("size")
        bath=float(request.args.get("bath"))
        balcony=float(request.args.get("balcony"))
        site_location=request.args.get("site_location")
    

        print("availability,area_type,size,bath,balcony,site_location \n",availability,area_type,size,bath,balcony,site_location)

        house_cost = HousePrice(availability,area_type,size,bath,balcony,site_location)
        charges = house_cost.get_predicted_price()
        return render_template("index.html", prediction = charges)

    else:
        print("We are using POST Method")

        # age = int(request.form.get("age"))
        # sex = request.form.get("sex")
        # bmi = float(request.form.get("bmi"))
        # children = int(request.form.get("children"))
        # smoker = request.form.get("smoker")
        # region = request.form.get("region")

        availability=request.form.get("availability")
        area_type=request.form.get("area_type")
        size=request.form.get("size")
        bath=float(request.form.get("bath"))
        balcony=float(request.form.get("balcony"))
        site_location=request.form.get("site_location")

        print("availability,area_type,size,bath,balcony,site_location \n",availability,area_type,size,bath,balcony,site_location)

        house_cost = HousePrice(availability,area_type,size,bath,balcony,site_location)
        charges = house_cost.get_predicted_price()

        return render_template("index.html", prediction = charges)


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=config.PORT_NUMBER, debug=True)




        
