from urllib.request import urlopen
from urllib.parse import quote
from django.conf import settings

def SendMessage(phone_number, text):
    print('xxxxxxxxxxxxxxx')
    url = "https://login.niazpardaz.ir/SMSInOutBox/SendSms?username={username}&password={password}&from={line_number}&to={phone_number}&text=".format(
    phone_number = phone_number, username = settings.NIAZPARDAZ_USERNAME, password = settings.NIAZPARDAZ_PASSWORD,
    line_number = settings.NIAZPARDAZ_LINENUMBER)
    text = quote(text)
    persian_url = url + text
    print(persian_url)
    page = urlopen(persian_url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
