Pregunta 1

pyproject.toml sí: contiene la configuración del proyecto, la versión de Python compatible y las dependencias.
uv.lock sí: fija las versiones exactas de las dependencias y permite reproducir el mismo entorno.
.python-version sí: indica qué versión de Python utiliza el proyecto por defecto.
.venv no: es el entorno virtual local y uv puede reconstruirlo con uv sync.
.gitignore sí: contiene las reglas que indican a Git qué archivos y carpetas debe ignorar, como .venv.

Pregunta 2

Según uv tree, pandas trae cuatro subdependencias que yo no pedí directamente: numpy, python-dateutil, tzdata y six (esta última es una dependencia de python-dateutil).

Con un requirements.txt, las dependencias y sus versiones podían quedar incompletas o cambiar al instalar en otra máquina. uv.lock registra el árbol completo de dependencias y sus versiones exactas, por lo que permite reproducir el mismo entorno.

Pregunta 3
uv run puede crear/recrear automáticamente el entorno virtual y sincronizar las dependencias declaradas en el proyecto. En mi prueba, al eliminar el entorno, uv intentó reconstruirlo automáticamente.

Pregunta 4
Si se elimina manualmente rich de pyproject.toml y se ejecuta uv sync, rich deja de estar disponible aunque pueda seguir apareciendo en el lockfile según el estado de sincronización. Al ejecutar el programa aparece un error porque main.py necesita rich. Después se recupera con uv add rich.

Pregunta 5
.python-version indica la versión de Python que uv utiliza por defecto en el proyecto. requires-python de pyproject.toml indica qué versiones son compatibles con el proyecto. Si mañana quisiera usar Python 3.15 como versión por defecto, cambiaría .python-version a 3.15; requires-python no tendría que cambiar si ya permite 3.15.