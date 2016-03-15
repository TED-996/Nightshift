import datetime
import time
import sys
import os.path
from location import get_location
from generator import get_wallpaper_params
from sunset import get_sunrise_sunset
import ctypes
import unicodedata


appdata_folder = os.path.join(os.environ["LOCALAPPDATA"], "Nightshift")


def run_nightshift():
    print "Trying to run nightshift"
    location_params = get_location()
    wallpaper_params = get_wallpaper_params()
    sunrise, sunset = get_sunrise_sunset(location_params["latitude"], location_params["longitude"])
    step_count = wallpaper_params["step_count"]
    img_format = wallpaper_params["format"]

    last_id = -1
    while True:
        current_time = datetime.datetime.now().time()
        last_id = update_nightshift(current_time, sunrise, sunset, step_count, img_format, last_id)
        time.sleep(15)


def test_nightshift():
    print "Testing nightshift: "
    location_params = get_location()
    wallpaper_params = get_wallpaper_params()
    sunrise, sunset = get_sunrise_sunset(location_params["latitude"], location_params["longitude"])
    step_count = wallpaper_params["step_count"]
    img_format = wallpaper_params["format"]

    print "Sunrise is at {0} and sunset at {1}".format(sunrise, sunset)

    current_time = datetime.time(minute=2)
    start_time = datetime.time()
    last_id = -1
    while current_time != start_time:
        current_time = (datetime.datetime.combine(datetime.datetime.today(), current_time) +
                        datetime.timedelta(seconds=15)).time()

        last_id = update_nightshift(current_time, sunrise, sunset, step_count, img_format, last_id)
        # print "Updated for time = {0}; id = {1}".format(current_time, last_id)
        # time.sleep(0.1)


def update_nightshift(time_obj, sunrise, sunset, step_count, img_format, last_id):
    night_index = get_night_index(time_obj, sunrise, sunset)
    if step_count != 0:
        step = int(night_index * step_count)
        wallpaper_id = int(step / float(step_count) * 255)
    else:
        wallpaper_id = 0 if (night_index <= 0.5) else 255

    if wallpaper_id != last_id:
        set_wallpaper(wallpaper_id, img_format)

    return wallpaper_id


def get_night_index(time_obj, sunrise, sunset):
    # interval in hours around the sunrise/sunset times
    interval = 1.0
    time_hours = to_hours_float(time_obj)
    sunrise_hours = to_hours_float(sunrise)
    sunset_hours = to_hours_float(sunset)

    # deltas: + => night; - => day
    sunrise_delta = sunrise_hours - time_hours
    sunset_delta = time_hours - sunset_hours
    min_abs_delta = min(abs(sunrise_delta), abs(sunset_delta))

    # normal day: sunrise, then sunset
    if sunrise_hours < sunset_hours:
        if sunrise_delta >= 0 or sunset_delta >= 0:
            min_delta = min_abs_delta
            if min_delta >= interval / 2.0:
                return 1
            return (min_delta + interval / 2.0) / interval
        else:
            max_delta = -min_abs_delta
            if max_delta <= -interval / 2.0:
                return 0

            return (interval / 2.0 + max_delta) / interval
    else:
        if sunrise_delta >= 0 and sunset_delta >= 0:
            min_delta = min_abs_delta
            if min_delta >= interval / 2.0:
                return 1
            return (min_delta + interval / 2.0) / interval
        else:
            max_delta = -min_abs_delta
            if max_delta <= -interval / 2.0:
                return 0
            return (interval / 2.0 + max_delta) / interval


def to_hours_float(time_obj):
    return time_obj.hour + time_obj.minute / 60.0 + time_obj.second / 3600.0


def set_wallpaper(index, img_format):
    img_path = os.path.abspath(os.path.join(appdata_folder, format(index, "03d") + img_format))
    print "Setting wallpaper to path", img_path
    if not os.path.exists(img_path):
        raise Exception("Image file not found!")
    # noinspection PyPep8Naming
    SPI_SETDESKWALLPAPER = 0x0014
    ascii_path = unicodedata.normalize("NFKD", img_path).encode("ascii", "ignore")
    if not ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, ascii_path, 3):
        raise Exception("Could not set wallpaper!")


def run_nightshift_standalone():
    sys.stdout = open(os.path.join(appdata_folder, "stdout.log"), "w", buffering=1)
    sys.stderr = open(os.path.join(appdata_folder, "stderr.log"), "w", buffering=1)
    run_nightshift()


if __name__ == "__main__":
    run_nightshift_standalone()
