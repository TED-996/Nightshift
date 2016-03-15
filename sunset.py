import datetime
import astral
import tzlocal


def get_sunrise_sunset(latitude, longitude):
    print "Trying to get the sunrise and sunset times"
    astral_obj = astral.Astral()
    astral_obj.solar_depression = "civil"
    sunrise_utc = astral_obj.sunrise_utc(datetime.datetime.utcnow(), latitude, longitude)
    sunset_utc = astral_obj.sunset_utc(datetime.datetime.utcnow(), latitude, longitude)
    timezone = tzlocal.get_localzone()

    return sunrise_utc.astimezone(timezone).time(), sunset_utc.astimezone(timezone).time()
