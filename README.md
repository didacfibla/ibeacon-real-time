# ibeacon-real-time

<h1> INFORMACIÓN </h1>

Esta herramienta permite capturar los paquetes de advertising de un beacon que utiliza el protocolo iBeacon y muestra en tiempo real un grafico con la señal capturada y con la señal filtrada con el filtro de Kalman
Editar el fichero main.py y cambiar la linea 40: 'if item["minor"] == 30:'
Cambiar el 30 por el minor id de tu beacon.


<h1> INSTALACION Y DEPENDENCIAS </h1>

pip3 install matplotlib
pip3 install pybluez
pip3 install numpy

Ejecutar el programa como root:
sudo python3 main.py

<h1> DEMOSTRACIÓN</h1>

<img src="./demo.gif" />
