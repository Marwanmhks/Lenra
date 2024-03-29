import json
from http.server import BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.headers.get('Authorization') is None:
            # if there's no query
            if self.path == '/lenra/':
                # Welcome to Counter app
                self.do_HEAD()
                self.wfile.write("Welcome to the counter app".encode('utf-8'))
            else:
                # Extract the query from path
                query = get_content(self.path.replace("/lenra/?", ""))

            pass
        else:
            pass

    def do_POST(self):
        if self.headers.get('Authorization') is None:
            length = int(self.headers.get('Content-Length'))
            data = self.rfile.read(length).decode('utf-8')

            self.do_HEAD()
            self.wfile.write(data.encode('utf-8'))
            pass
        else:
            pass


def get_content(path: str):
    path = path.replace("+", " ")
    result = dict((a.strip(), b.strip())
                  for a, b in (element.split('=')
                               for element in path.split('&')))
    return result
