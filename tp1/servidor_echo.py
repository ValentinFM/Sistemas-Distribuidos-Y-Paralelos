import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor echo escuchando en {HOST}:{PORT}")
    
    conn, addr = s.accept()
    with conn:
        print(f"Cliente conectado desde: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break # El cliente cerró la conexión
            
            mensaje = data.decode('utf-8')
            
            # Consigna 4: Comando SALIR y cierre ordenado
            if mensaje.strip().upper() == "SALIR":
                confirmacion = "Confirmación: Conexión finalizada."
                conn.sendall(confirmacion.encode('utf-8'))
                print("Comando SALIR recibido. Cerrando socket del cliente.")
                break
            
            # Consigna 2: Servidor Echo (devuelve lo mismo que recibe)
            conn.sendall(data)