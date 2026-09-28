import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor TCP escuchando en {HOST}:{PORT}")
    
    conn, addr = s.accept()
    with conn:
        buffer = b""
        while True:
            data = conn.recv(1024)
            if not data:
                break # El cliente se desconectó
            
            buffer += data
            # Extraer y responder mensajes completos delimitados por \n
            while b"\n" in buffer:
                mensaje, buffer = buffer.split(b"\n", 1)
                conn.sendall(mensaje + b"\n")