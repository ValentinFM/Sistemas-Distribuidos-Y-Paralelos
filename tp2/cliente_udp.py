import socket
import time

HOST = '127.0.0.1'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(1.0) # Configuración requerida para UDP[cite: 2]
    
    # Envío de 10 mensajes, uno por datagrama
    for i in range(1, 11):
        mensaje_str = f"Mensaje {i}"
        inicio = time.perf_counter()
        
        try:
            s.sendto(mensaje_str.encode('utf-8'), (HOST, PORT))
            data, addr = s.recvfrom(1024)
            rtt_ms = (time.perf_counter() - inicio) * 1000
            print(f"Enviado/Recibido: {data.decode('utf-8')} | RTT: {rtt_ms:.3f} ms")
        except socket.timeout:
            print(f"Enviado: Mensaje {i} | RTT: sin datos (Timeout)")
            # En UDP se registra la ausencia de respuesta y se continúa[cite: 2]
            
        time.sleep(2) # Pausa entre intercambios, fuera de la medición del RTT[cite: 2]