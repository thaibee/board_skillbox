from datetime import datetime, timedelta
import csv

from django.core.exceptions import PermissionDenied


class FilterIP:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, list_acc=None):
        allowed_ips = ['127.0.0.2']
        ip = request.META.get('REMOTE_ADDR')
        time_now = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        if ip in allowed_ips:
            raise PermissionDenied
        with open('log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time_now, ip, request.method])
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            a = sum([1 for i in reader if
                     datetime.strptime(i[0], '%d/%m/%y %H:%M:%S') > datetime.now() - timedelta(minutes=2)])
            # print(a)
        response = self.get_response(request)
        return response
