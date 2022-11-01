
import pickle
import json
import numpy as np
import pandas as pd
import config


class HousePrice():
    def __init__(self,availability,area_type,size,bath,balcony,site_location):
        self.availability='availability_'+ availability
        self.area_type=area_type
        self.size=size
        self.bath=bath
        self.balcony=balcony
        self.site_location ='site_location_'+ site_location       

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        print(config.MODEL_FILE_PATH)    

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

        print(config.JSON_FILE_PATH)   


    def get_predicted_price(self):

        self.load_model()

        availability_index = self.json_data['columns'].index(self.availability)

        site_location_index = self.json_data['columns'].index(self.site_location)

        array = np.zeros(len(self.json_data['columns']))

        array[0]=self.json_data['area_type'][self.area_type]
        array[1]=self.json_data['size'][self.size]
        array[2]=self.bath
        array[4]=self.balcony
        array[site_location_index]=1
        array[availability_index]=1

        print(array)
        predicted_charges= self.model.predict([array])[0]
        print("predicted_charges",abs(predicted_charges))
        return np.around(predicted_charges, 2)

if __name__ == "__main__":
    availability='Ready To Move'
    area_type='Super built-up Area'
    size='3 BHK'
    bath=2.0
    balcony=1.0
    site_location='Aundh Road'

    house_cost = HousePrice(availability,area_type,size,bath,balcony,site_location)
    charges = house_cost.get_predicted_price()
    print(abs(charges))
