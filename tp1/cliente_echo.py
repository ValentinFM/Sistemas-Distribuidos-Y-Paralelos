import socket
import time

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Consigna 3: Bucle para cinco mensajes en la misma conexión
    for i in range(5):
        mensaje = input(f"Mensaje {i+1} de 5 (escriba SALIR para terminar): ")
        
        # Consigna 5: Medición del RTT
        inicio = time.perf_counter()
        
        # Codificación a bytes antes de enviar
        s.sendall(mensaje.encode('utf-8')) 
        
        # Recepción de hasta 1024 bytes
        respuesta_bytes = s.recv(1024)
        if not respuesta_bytes:
            print("El servidor cerró la conexión de manera abrupta.")
            break
            
        # Decodificación y cálculo de RTT
        respuesta = respuesta_bytes.decode('utf-8')
        rtt_ms = (time.perf_counter() - inicio) * 1000
        
        print(f"Respuesta del servidor: {respuesta}")
        print(f"RTT: {rtt_ms:.3f} ms\n")
        
        # Cierre local si se envió SALIR
        if mensaje.strip().upper() == "SALIR":
            break