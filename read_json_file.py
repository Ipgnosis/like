# read a json data file

import json


# reads a json file and returns json or False
def read_json_data(fname):

    try:
        with open(fname) as json_file:
            data = json.load(json_file)
        return data
    except OSError as error:
        print(error)
        print("File {} cannot be read".format(fname))
        return False
