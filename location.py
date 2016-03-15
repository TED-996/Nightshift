import os.path
import json
from astral import Astral

appdata_folder = os.path.join(os.environ["LOCALAPPDATA"], "Nightshift")


def set_location(latitude, longitude):
    print "Setting location to {0}, {1}".format(latitude, longitude)

    try:
        if not os.path.exists(appdata_folder):
            os.mkdir(appdata_folder)

        file_obj = open(os.path.join(appdata_folder, "location.json"), "w")
        json.dump({"longitude": longitude,
                   "latitude": latitude},
                  file_obj)
        file_obj.close()
        return True
    except:
        print "Could not save the location and sunrise/sunset."
        raise


def set_location_city(city):
    print "Trying to set location to", city
    astral_obj = Astral()

    try:
        city_data = astral_obj[city]
    except KeyError:
        print "Sorry, but this city does not exist in the city database."
        print "City names are capitalized and in English (e.g. Rome)"
        return False
    set_location(city_data.latitude, city_data.longitude)
    return True


def get_location():
    print "Getting saved location."
    try:
        file_obj = open(os.path.join(appdata_folder, "location.json"), "r")
        result = json.load(file_obj)
        file_obj.close()
        return {"longitude": result["longitude"],
                "latitude": result["latitude"]}
    except IOError:
        print "Could not read from location file."
        print "Try setting your location with"
        print "Nightshift.exe -s latitude longitude"
        print "or"
        print "Nightshift.exe -s city"
        raise
    except:
        print "Could not get saved location."
        raise
