# Given the provided cars dictionary:
#
# Get all Jeeps
# Get the first car of every manufacturer.
# Get all vehicles containing the string Trail in their names (should work for other grep too)
# Sort the models (values) alphabetically
# See the docstrings and tests for more details. Have fun!
# URL = https://codechalleng.es/bites/21/


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    jeeps = cars['Jeep']
    return ", ".join(str(x) for x in jeeps)


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    m = []
    for i in cars.values():
        m.append(i[0])
    return m


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    n = []
    for i in cars.values():
        for b in i:
            if grep.lower() in b.lower():
                n.append(b)
    return sorted(n)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    new_dict = {}
    p = sorted(list(cars.keys()))
    for i in p:
        new_dict[i] = sorted(cars[i])
    return new_dict