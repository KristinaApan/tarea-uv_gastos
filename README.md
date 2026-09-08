Pregunta 1

pyproject.toml sí: contiene la configuración del proyecto, la versión de Python compatible y las dependencias.
uv.lock sí: fija las versiones exactas de las dependencias y permite reproducir el mismo entorno.
.python-version sí: indica qué versión de Python utiliza el proyecto por defecto.
.venv no: es el entorno virtual local y uv puede reconstruirlo con uv sync.
.gitignore sí: contiene las reglas que indican a Git qué archivos y carpetas debe ignorar, como .venv.

Pregunta 2

Según uv tree, pandas trae cuatro subdependencias que yo no pedí directamente: numpy, python-dateutil, tzdata y six (esta última es una dependencia de python-dateutil).

Con un requirements.txt, las dependencias y sus versiones podían quedar incompletas o cambiar al instalar en otra máquina. uv.lock registra el árbol completo de dependencias y sus versiones exactas, por lo que permite reproducir el mismo entorno.