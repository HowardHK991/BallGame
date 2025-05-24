import http.server
import socketserver
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='启动游戏服务器')
    parser.add_argument('-p', '--port', type=int, default=8000,
                      help='服务器端口号 (默认: 8000)')
    return parser.parse_args()

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 如果访问根路径，重定向到 index.html
        if self.path == '/':
            self.path = '/index.html'
        # 如果访问 mindmap.html，重定向到 GAME0525.html
        elif self.path == '/mindmap.html':
            self.path = '/GAME0525.html'
        return super().do_GET()

    def end_headers(self):
        # 添加更严格的缓存控制
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        return super().end_headers()

def main():
    args = parse_args()
    Handler = MyHttpRequestHandler

    with socketserver.TCPServer(("", args.port), Handler) as httpd:
        print(f"服务器运行在 http://localhost:{args.port}")
        print("按 Ctrl+C 停止服务器")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")

if __name__ == '__main__':
    main() 