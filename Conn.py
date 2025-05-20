#Versión funcional y simplificada para hacer preguntas a Ollama
#usando python sobre un modelo de lenguaje y usando la API de Ollama
#para la comunicación
#esta versión sólo maneja preguntas simples y no tiene la parte de kubernetes
#
#Para que OLLAMA escuche en todas las IPS, debe usarse el comando:
# ollama serve --host 0.0.0.0 * Nota , esto funciona en Linux o WSL, no en Windows
#con esto se puede acceder a la API desde cualquier IP de la red y no solo desde localhost
#
# Importar las librerías necesarias
import requests

OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen:latest"

def ask_ollama(question, model=MODEL_NAME):
    payload = {
        "model": model,
        "prompt": question,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    result = response.json()
    return result["response"]

# Ejemplo de uso
pregunta = "¿Que es el Karma?"
respuesta = ask_ollama(pregunta)
print("Respuesta:", respuesta)