#Sistemas Distribuidos y Paralelos - Trabajo Práctico N° 2
Repositorio con la resolución del TP 2 de la materia Sistemas Distribuidos y Paralelos (Universidad Nacional de Villa Mercedes).

Sockets TCP vs UDP
Este proyecto implementa y compara un servicio de eco (echo server) utilizando los protocolos TCP y UDP para analizar su comportamiento en condiciones normales y ante la interrupción del servidor

Características implementadas:

Cliente/Servidor TCP (Puerto 5000): Comunicación orientada a conexión. Manejo de un flujo continuo de bytes utilizando saltos de línea (\n) como delimitadores de mensaje
Cliente/Servidor UDP (Puerto 5001): Comunicación orientada a datagramas sin conexión previa. Implementación de timeouts (settimeout) para gestionar la ausencia de respuesta
Medición de rendimiento: Cálculo del tiempo de ida y vuelta (RTT) de cada mensaje utilizando time.perf_counter()
Simulación de fallos: Pruebas de interrupción del servidor para observar el quiebre de la conexión en TCP frente a la continuidad de envío en UDP
Instrucciones de ejecución (Prueba normal):

Para TCP: Iniciar python servidor_tcp.py en una terminal y luego python cliente_tcp.py en otra.
Para UDP: Iniciar python servidor_udp.py en una terminal y luego python cliente_udp.py en otra.
