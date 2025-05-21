Versión funcional y simplificada para hacer preguntas a Ollama usando python sobre un modelo de lenguaje y usando la API de Ollama para la comunicación.

Esta versión sólo maneja preguntas simples y no tiene la parte de kubernetes...la estoy preparando. 20-5-2025

Para que OLLAMA escuche en todas las IPS, debe usarse el comando: ollama serve --host 0.0.0.0 * Nota , esto funciona en Linux o WSL, no en Windows

con esto se puede acceder a la API desde cualquier IP de la red y no solo desde localhost

Importar las librerías necesarias
