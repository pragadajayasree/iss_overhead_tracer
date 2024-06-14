import requests
from datetime import datetime
import smtplib

MY_LAT = 20.593683
MY_LONG = 78.962883

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

is_position = "False"
if (((MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)) and
        ((MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5))):
    is_position = "True"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_time = time_now.hour
print(current_time)
print(sunset)
if is_position:
    if sunset <= current_time >= sunrise:
        email = "pragadajayasree@gmail.com"
        password = "psqf nzxg kvui vybv"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="pragadajayasree@yahoo.com", msg="subject:msg\n\nLook up")
