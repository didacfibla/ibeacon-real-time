<h1> ibeacon-real-time </h1>

Esta herramienta muestra en tiempo real la señal de advertising de un beacon que utilize el protocolo iBeacon. 
<br><i>(ScannUtility también es compatible con eddystone)</i>
- Muestra la señal pura en tiempo real
- Muestra la señal filtrada con el filtro de Kalman en tiempo real
- Muestra ambas señales superpuestas

<h4> INSTALACION Y DEPENDENCIAS </h4>

- pip3 install matplotlib
- pip3 install pybluez 
- pip3 install numpy
- pip3 install bottleneck (solo para Filtro_media_movil.py)

<h4> INSTRUCCIONES DE USO</h4>

- Ejecutar como root: sudo python3 real_time.py
- Tienes que cambiar el <b>minor por defecto</b>
  - real_time.py --> linea 40 --> if item["minor"] == 30:
  - Cambiar el 30 por el minor correspondiente de tu beacon.

<h4> DEMOSTRACIÓN</h4>

<img src="./demo.gif" />
