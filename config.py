import socket
import os
from dotenv import load_dotenv

# Valores por defecto
API_HOST = "127.0.0.1"
API_PORT = 8000

def init_config():
    global API_HOST, API_PORT

    hostname = socket.gethostname()

    # Si se quiere ajustar por nombre de máquina
    if hostname == "mi-servidor":
        API_HOST = "0.0.0.0"
        API_PORT = 8080

    # Permitir override por .env
    API_HOST = os.getenv("API_HOST", API_HOST)
    API_PORT = int(os.getenv("API_PORT", API_PORT))
