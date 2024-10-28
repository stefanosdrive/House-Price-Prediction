import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_price(location, surface, rooms, baths, balconies, lvl):
 
    loc_index = __data_columns.index(location.lower())
    
    x = np.zeros(len(__data_columns))
    x[0] = rooms
    x[1] = surface
    x[2] = lvl
    x[3] = baths
    x[4] = balconies
    if loc_index >= 0:
        x[loc_index] = 1
        
    return round(__model.predict([x])[0], 2)
    
def get_location_name():
    return __locations

def load_saved_artifacts():
    print("Starting loading saved artifacts...")
    global __data_columns
    global __locations
        
    with open ("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]
    
    global __model
    with open("./artifacts/bucharest_apartments_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Stopped loading saved artifacts...")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_price('Herastrau', 65, 3, 1, 1, 3))
    print(get_location_name())