import os.path
import json
import win32ui
import subprocess
import location
import generator

appdata_folder = os.path.join(os.environ["LOCALAPPDATA"], "Nightshift")


def nightshift_setup():
    print "Welcome to the Nightshift Setup."

    close_nightshift()

    location_json_path = os.path.join(appdata_folder, "location.json")

    print
    while (not os.path.exists(location_json_path) or not location_ok() or ask_set_location()) and not set_location():
        pass

    images_json_path = os.path.join(appdata_folder, "images.json")

    print
    while (not os.path.exists(images_json_path) or not images_ok() or ask_set_images()) and not set_images():
        pass

    print
    print "Configuration complete."

    if ask("Would you like to start Nighshift? (Y/N)"):
        start_nightshift()

    os.system("pause")


def location_ok():
    location_json_path = os.path.join(appdata_folder, "location.json")
    file_obj = open(location_json_path, "r")
    result = json.load(file_obj)
    file_obj.close()

    if "longitude" in result and isinstance(result["longitude"], float) and \
                    "latitude" in result and isinstance(result["latitude"], float):
        return True

    print "The location information file is invalid."
    return False


def ask_set_location():
    print "The location seems to be correctly set."
    return ask("Would you like to set it again? (Y/N)")


def ask(question):
    print question
    response = raw_input().lower()

    if response in ["y", "yes"]:
        return True

    if response not in ["n", "not"]:
        print "That's a no then."
    return False


def set_location():
    print
    try:
        print "You can set your location to a city (if it's in the database) or from latitude & longitude."
        city = raw_input("Enter city to set location to (or leave blank to skip): ")
        while city != "" and not city.isspace():
            if location.set_location_city(city):
                return True
            city = raw_input("Enter city to set location to (or leave blank to skip): ")

        while True:
            try:
                print "Enter your coordinates (you can find them on Wikipedia):"
                latitude = float(raw_input("Enter your latitude (as a decimal number): "))
                longitude = float(raw_input("Enter your longitude (as a decimal number): "))

                location.set_location(latitude, longitude)
                return True
            except ValueError:
                print "Please enter a number (example: 45.60)"
                pass
            except IOError:
                return False

    except IOError:
        return False


def images_ok():
    images_json_path = os.path.join(appdata_folder, "images.json")
    file_obj = open(images_json_path, "r")
    result = json.load(file_obj)
    file_obj.close()

    if "step_count" in result and isinstance(result["step_count"], int) and \
                    "format" in result and (isinstance(result["format"], str) or isinstance(result["format"], unicode)):
        return True

    print "The image information file is invalid."
    return False


def ask_set_images():
    print "The image information seems to be correctly set."
    return ask("Would you like to set it again? (Y/N)")


def set_images():
    print
    try:
        print "You need 2 wallpapers the same size to set as wallpapers."

        day_image_path = None
        while day_image_path is None:
            print "Choose the daytime wallpaper:"
            dialog = win32ui.CreateFileDialog(1, None, None, 0,
                                              "Image files (.jpg, .png, .bmp) |*.jpg;*.jpeg;*.png;*.bmp|"
                                              "All files (*.*)|*.*")
            dialog.SetOFNTitle("Choose the daytime wallpaper")
            dialog_result = dialog.DoModal()
            if dialog_result == 1:
                day_image_path = dialog.GetPathName()
            elif dialog_result == 2:
                return False

        night_image_path = None
        while night_image_path is None:
            print "Choose the nighttime wallpaper:"
            dialog = win32ui.CreateFileDialog(1, None, None, 0,
                                              "Image files (.jpg, .png, .bmp) |*.jpg;*.jpeg;*.png;*.bmp|"
                                              "All files (*.*)|*.*")
            dialog.SetOFNTitle("Choose the nighttime wallpaper")
            dialog_result = dialog.DoModal()
            if dialog_result == 1:
                night_image_path = dialog.GetPathName()
            elif dialog_result == 2:
                return False

        print "You can also create intermediate images (blends of the 2 images) to set as wallpapers around " \
              "sunrise and sunset."
        print "You can choose how many images to create, and they will be at equal blending intervals."

        while True:
            try:
                step_count = int(raw_input("Enter the image count: "))
                if step_count >= 0:
                    break
                print "Please enter a positive number."
            except ValueError:
                print "Please enter a number."
                pass

        # noinspection PyBroadException
        try:
            # noinspection PyUnboundLocalVariable
            generator.generate_wallpapers(day_image_path, night_image_path, step_count + 1)
        except:
            return False
        return True

    except IOError:
        raise


def close_nightshift():
    print
    print "Closing Nightshift (if it is running)"
    # os.system("tskill nightshift")
    subprocess.Popen("tskill nightshift", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()


def start_nightshift():
    subprocess.Popen("nightshift.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    nightshift_setup()
