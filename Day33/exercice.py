import requests
from datetime import datetime
from time import sleep
import smtplib

EMAIL = "elvishenry2402@gmail.com"
PASSWORD = "rpwdynumgwfkjdit"

can_send_email_again = True

LNG = 2.272520
LAT = 48.883629

def is_night():
    parameter = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
    }
    
    sun_request = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    sun_request.raise_for_status()

    data_sun = sun_request.json()["results"]
    sunrise = data_sun["sunrise"]
    sunset = data_sun["sunset"]

    day_hour = (int(sunrise.split("T")[1].split(":")[0]), int(sunset.split("T")[1].split(":")[0]))
    current_hour = datetime.now().hour

    if current_hour >= day_hour[0] and current_hour <= day_hour[1]:
        return False
    
def is_iss_on():
    request = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = request.json()["iss_position"]
    iss_position = (float(data["longitude"]), float(data["latitude"]))
    
    print(iss_position)

    if LAT - 5 <= iss_position[1] <= LAT + 5:
        if LNG - 5 <= iss_position[0] <= LNG + 5:
            return True

def checking_iss_position():
    global can_send_email_again

    if is_iss_on():
        if not is_night():
            if can_send_email_again:
                can_send_email_again = False
                sending_alert_for_iss_position()

    can_send_email_again = True

def sending_alert_for_iss_position():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:ISS\n\nYou can see ISS in the sky !")

while True:
    sleep(60)
    checking_iss_position()