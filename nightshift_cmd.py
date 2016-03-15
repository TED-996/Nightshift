import sys
from location import set_location, set_location_city
from generator import generate_wallpapers
from nightshift import run_nightshift, test_nightshift


def nightshift_cmd():
    if len(sys.argv) == 4 and (sys.argv[1] == "-s" or sys.argv[1] == "--set-location"):
        try:
            latitude = float(sys.argv[2])
            longitude = float(sys.argv[3])
        except ValueError:
            print "Could not parse arguments."
            print_usage()
            raise
        set_location(latitude, longitude)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-s" or sys.argv[1] == "--set-location"):
        set_location_city(sys.argv[2])
    elif len(sys.argv) == 5 and (sys.argv[1] == "-g" or sys.argv[1] == "--generate"):
        try:
            day_path = sys.argv[2]
            night_path = sys.argv[3]
            step_count = int(sys.argv[4])
        except ValueError:
            print "Could not parse arguments."
            print_usage()
            raise
        generate_wallpapers(day_path, night_path, step_count)
    elif len(sys.argv) == 2 and sys.argv[1] == "-?":
        print_usage()
    elif len(sys.argv) == 2 and sys.argv[1] == "--test":
        test_nightshift()
    elif len(sys.argv) == 1:
        run_nightshift()
    else:
        print "Unrecognized arguments."
        print_usage()


def print_usage():
    print "Usage:"
    print "Nightshift.exe"
    print "Nightshift.exe --test"
    print "Nightshift.exe --generate path_to_day_image path_to_night_image step_count"
    print "Nightshift.exe -g path_to_day_image path_to_night_image step_count"
    print "Nightshift.exe --set-location latitude longitude"
    print "Nightshift.exe -s latitude longitude"
    print "Nightshift.exe --set-location city"
    print "Nightshift.exe -s city"


if __name__ == "__main__":
    nightshift_cmd()
