from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequesthandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequesthandler)
httpd.serve_forever()