import requests as req
import yagmail
import os

client = req.session()

url = os.environ.get("WEBSITE_URL", default="https://www.vbcvjsr.in")
MAX_TIMEOUT = int(os.environ.get("MAX_TIMEOUT", default="30"))
is_working = False

try:
    with client.get(url=url, headers={"REASON": "NEED TO CHECK IF YOUR WEBSITE IS WORKING OR NOT."}, timeout=MAX_TIMEOUT) as response:
        print(response.ok)
        is_working = response.ok
except Exception as e:
    print(e)

# SOME EMAIL CONF
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
RECEIVER = "adityapriyadarshi669@gmail.com"

MESSAGE = f"""
    Hi,
    Your website {url} is {'working ✅' if is_working else 'not working ❌'}

    Thanks,
    Aditya Priyadarshi
    """

yag = yagmail.SMTP(user=EMAIL, password=PASSWORD)

print("SENDING EMAIL 🕑")
yag.send(to=RECEIVER, subject=f"Website Status: {'WORKING ✅' if is_working else 'NOT WORKING ❌'}", contents=MESSAGE)
print("EMAIL SENT ✅")