from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv
import xml.etree.ElementTree as ET
import requests


TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None


def get_info(info):
    tree = ET.ElementTree(ET.fromstring(info))
    root = tree.getroot()
    event = root[8]
    channel_name = root[9]
    return event, channel_name


def send_message(message):
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    r = requests.get(url, params=params)
    if r.status_code == 200:
        print(message)
    else:
        r.raise_for_status()


class S(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        message = get_info(post_data.decode('utf-8'))
        send_message("התראה מסוג: " + message[0].text + " במצלמה: " + message[1].text)


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Start listening...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stop listening...\n')


if __name__ == '__main__':
    if len(argv):
        TELEGRAM_BOT_TOKEN = argv[1]
        TELEGRAM_CHAT_ID = argv[2]
        run()
