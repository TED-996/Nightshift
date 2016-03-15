import os.path
from PIL import Image
import json

appdata_folder = os.path.join(os.environ["LOCALAPPDATA"], "Nightshift")


def generate_wallpapers(day_img_path, night_img_path, step_count):
    print "Generating {0} images from {1} and {2} to {3}"\
        .format(step_count, day_img_path, night_img_path, appdata_folder)
    if not os.path.exists(day_img_path) or not os.path.exists(night_img_path) \
            or os.path.isdir(day_img_path) or os.path.isdir(night_img_path):
        raise IOError("Day image or night image not found.")
    _, day_ext = os.path.splitext(day_img_path)
    _, night_ext = os.path.splitext(night_img_path)
    if day_ext not in [".jpeg", ".jpg"] or night_ext not in [".jpeg", ".jpg"]:
        print "Images will be converted to .jpg."

    try:
        day_image = Image.open(day_img_path)
        night_image = Image.open(night_img_path)
    except IOError:
        print "Could not read image files."
        raise

    if day_image.size != night_image.size:
        print "The two wallpapers must be the same size."
        raise Exception("The two wallpapers must be the same size.")

    try:
        if not os.path.exists(appdata_folder):
            os.mkdir(appdata_folder)
        else:
            cleanup_old_wallpapers()

        blend_save_image(day_image, night_image, 0)

        for step in range(1, step_count + 1):
            opacity = step / float(step_count)
            blend_save_image(day_image, night_image, opacity)
    except:
        print "Could not generate wallpapers."
        raise

    try:
        output_file = open(os.path.join(appdata_folder, "images.json"), "w")
        json.dump({"step_count": step_count,
                   "format": ".jpg"},
                  output_file)
        output_file.close()
    except IOError:
        print "Could not write image settings."
        raise

    print "Images generated correctly."


def cleanup_old_wallpapers():
    print "Cleaning up wallpaper directory."
    for item in os.listdir(appdata_folder):
        if item.endswith(".jpg"):
            os.remove(os.path.join(appdata_folder, item))


def blend_save_image(day_image, night_image, opacity):
    blended_image = Image.blend(day_image, night_image, opacity)
    blended_image.save(os.path.join(appdata_folder, format(int(opacity * 255), "03d") + ".jpg"), quality=95)
    blended_image.close()


def get_wallpaper_params():
    print "Getting saved wallpaper params."
    try:
        file_obj = open(os.path.join(appdata_folder, "images.json"), "r")
        result = json.load(file_obj)
        file_obj.close()
        return result
    except IOError:
        print "Could not read from wallpaper params file."
        print "Try generating the wallpaper images with"
        print "Nightshift.exe -g path_to_day_image path_to_night_image step_count"
        raise
    except:
        print "Could not get saved location."
        raise
