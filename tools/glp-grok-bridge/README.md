# GLP Grok bridge

Servidor MCP mínimo (solo biblioteca estándar de Python) que completa el MCP de
[GLP](https://github.com/mxkissnr/gaggiuino-local-profiler) para un asistente remoto como Grok:

| Herramienta | Qué hace |
|---|---|
| `assign_shot_coffee` | Liga un shot de GLP a un café de la biblioteca y, opcionalmente, fija la dosis. El MCP de GLP 3.7.0 no permite cambiar esos campos; sin ellos GLP no descuenta stock ni cuenta el shot en las estadísticas del café. |
| `get_shot_profile` | Lee de la Gaggiuino el perfil exacto con el que se tiró un shot (nombre, temperatura, stop-on-weight y fases). GLP no guarda el nombre del perfil. Solo lectura. |
| `list_machine_profiles` | Lista los perfiles instalados en la Gaggiuino y cuál está activo. Solo lectura. |

Las dos herramientas de máquina solo aparecen si el contenedor tiene `MACHINE_URL`. Solo hacen
`GET` a la API web de la Gaggiuino; no pueden cambiar perfiles ni ajustes.

Las instrucciones para el asistente están en [`grok/`](../../grok/).

## Despliegue

Dos contenedores en la red Docker de GLP (`glp-net`), publicados por Tailscale Funnel:

```bash
source ~/.config/shell/secrets.env   # GLP_TOKEN y GLP_GROK_MCP_KEY
DIR="<ruta del repo>/tools/glp-grok-bridge"

docker run -d --name glp-grok-bridge --restart unless-stopped --network glp-net \
  --read-only --user 65534:65534 -e GLP_TOKEN -e MACHINE_URL=http://192.168.1.94 \
  -v "$DIR/server.py:/app/server.py:ro" python:3.13-slim python /app/server.py

docker run -d --name glp-grok-proxy --restart unless-stopped --network glp-net \
  -p 127.0.0.1:8100:8100 -e NGINX_ENVSUBST_FILTER='^GLP_' -e GLP_TOKEN -e GLP_GROK_MCP_KEY \
  -v "$DIR/nginx.conf.template:/etc/nginx/templates/default.conf.template:ro" nginx:1.29-alpine

tailscale funnel --bg --https=10000 http://127.0.0.1:8100
```

Conectores en grok.com: `https://<host>.ts.net:10000/<clave>/mcp` (GLP) y
`https://<host>.ts.net:10000/<clave>/extra/mcp` (este puente). Para cortar el acceso:
`tailscale funnel --https=10000 off`.

## Pruebas

```bash
docker run --rm -v "$PWD:/app:ro" -w /app -e PYTHONDONTWRITEBYTECODE=1 python:3.13-slim python -m unittest -v
```
