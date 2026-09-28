import socket
import time

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(1.0) # Configuración requerida para limitar la espera de respuesta
    
    # Envío de 10 mensajes sobre la misma conexión
    for i in range(1, 11):
        mensaje_str = f"Mensaje {i}\n"
        
        inicio = time.perf_counter()
        
        try:
            s.sendall(mensaje_str.encode('utf-8'))
            buffer = b""
            while b"\n" not in buffer:
                data = s.recv(1024)
                if not data:
                    break
                buffer += data
                
            rtt_ms = (time.perf_counter() - inicio) * 1000
            respuesta = buffer.decode('utf-8').strip()
            
            # Si data está vacío, el servidor cerró la conexión
            if not data:
                print(f"Error: El servidor cerró la conexión en el Mensaje {i}.")
                break
                
            print(f"Enviado/Recibido: {respuesta} | RTT: {rtt_ms:.3f} ms")
            
        except socket.timeout:
            print(f"Error: Timeout agotado esperando el Mensaje {i}.")
            break # Informar lo ocurrido y terminar la ejecución
        except Exception as e:
            print(f"Error de conexión en Mensaje {i}: {e}")
            break # Informar lo ocurrido y terminar la ejecución
            
        time.sleep(2) # Pausa entre intercambios, fuera de la medición del RTT