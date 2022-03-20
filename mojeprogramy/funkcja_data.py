from datetime import datetime
import pytz

def date_now():
    now = datetime.now(pytz.timezone('Poland'))
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    content = "It's " + formatted_now 
    return content