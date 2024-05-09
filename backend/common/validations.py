from django.utils import timezone

format = "%Y-%m-%d"


def date_validation(date):
    try:
        return timezone.now().strptime(date, format).astimezone()
    except:
        raise Exception("Please pass the date in YYYY-mm-dd format")
