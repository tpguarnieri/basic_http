import socket

class HttpServer:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port 
    
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Sets up server socket to listen and accept incoming connections
            server_socket.bind((self.addr, self.port))
            server_socket.listen(5)
            while True:
                # Accept connection, create connection socket, and read data
                client_socket, addr = server_socket.accept()
                data = client_socket.recv(1024)
                print("Client data", data.decode()) 

                # Send HTTP Response to client
                response = 'HTTP/1.0 200 OK\n\n<h1>Hello, world!</h1>'
                client_socket.sendall(response.encode())
                client_socket.close()

if __name__ == "__main__":
    server = HttpServer('localhost', 8000)
    server.run()