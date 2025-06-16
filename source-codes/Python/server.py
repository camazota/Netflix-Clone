import socket
import threading
import os
import json
import mimetypes

HOST = '127.0.0.1'
PORT = 8080

films = [
    {"image": "/film-images/you.jpg"},
    {"image": "/film-images/mrrobot.jpg"},
    {"image": "/film-images/lacasadepapel.jpg"},
    {"image": "/film-images/strangerthings.webp"},
    {"image": "/film-images/squidgame.jpg"},
    {"image": "/film-images/peakyblinders.webp"},
    {"image": "/film-images/blackmirror.jpg"},
    {"image": "/film-images/queensgambit.jpg"},
    {"image": "/film-images/vikings_0.webp"},
    {"image": "/film-images/wednesday.jpg"},
]

STATIC_DIR = "../../static"
TEMPLATES_DIR = "../../templates"

def get_file_content(file_path):
    try:
        with open(file_path, "rb") as f:
            return f.read()
    except:
        return None

def handle_client(conn, addr):
    try:
        request = conn.recv(4096).decode("utf-8")
        if not request:
            conn.close()
            return

        lines = request.split("\r\n")
        request_line = lines[0]
        method, path, _ = request_line.split()

        print(f"[{addr}] {method} {path}")

        if method == "GET":
            if path == "/":
                file_path = os.path.join(TEMPLATES_DIR, "index.html")
                content = get_file_content(file_path)
                if content:
                    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + content
                else:
                    response = b"HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 - Not Found</h1></body></html>"

            elif path == "/api/films/popular":
                body = json.dumps(films).encode("utf-8")
                headers = b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
                response = headers + body

            else:
                clean_path = path.lstrip("/")
                file_path = os.path.join(STATIC_DIR, clean_path)

                content = get_file_content(file_path)
                if content:
                    mime_type, _ = mimetypes.guess_type(file_path)
                    if not mime_type:
                        mime_type = "application/octet-stream"
                    headers = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n".encode("utf-8")
                    response = headers + content
                else:
                    response = b"HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 - Not Found</h1></body></html>"

        else:
            response = b"HTTP/1.1 405 Method Not Allowed\r\n\r\n"

        conn.sendall(response)
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Sunucu {HOST}:{PORT} adresinde dinleniyor...")
        try:    
            while True:
                conn, addr = server.accept()
                threading.Thread(target=handle_client, args=(conn, addr)).start()
        except KeyboardInterrupt:
            print("\nSunucu kapatıldı.")

if __name__ == "__main__":
    main()
