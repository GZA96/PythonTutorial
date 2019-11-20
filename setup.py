from setuptools import setup

setup(
    name="paqueteEj_paquete",
    version="1.0",
    description="PAquete con funciones de calculo básicas",
    author="Gonza",
    author_email="ejemplo@email.com",
    url="www.ejemplourl.com",
    packages=["Ej_paquete", "Ej_paquete.calculos_generales"]

)
# Desde el directorio del set up, abrir consola
# El comando para crear el paquete distribuible es: python setup.py sdist
# Consola dentro de dist -->
# El comando para instalar un paquete distribuible es: pip3 install nombredelpaquete.tar.gz
# - Esto hace que el paquete forme parte de nuestra instalacion de python y podamos importarle sin importar donde
# - esté ubicado
# El comando para desinstalar el paquete ditribuible es: pip3 uninstall nombredelpaquete.tar.gz
