# GLP Grok bridge

Servidor MCP mínimo (solo biblioteca estándar de Python) con una única herramienta,
`assign_shot_coffee`: liga un shot de [GLP](https://github.com/mxkissnr/gaggiuino-local-profiler)
a un café de la biblioteca y, opcionalmente, fija la dosis. El MCP de GLP 3.7.0 no permite
cambiar esos campos; sin ellos GLP no descuenta stock ni cuenta el shot en las estadísticas del café.

## Despliegue

Dos contenedores en la red Docker de GLP (`glp-net`), publicados por Tailscale Funnel:

```bash
source ~/.config/shell/secrets.env   # GLP_TOKEN y GLP_GROK_MCP_KEY
DIR="<ruta del repo>/tools/glp-grok-bridge"

docker run -d --name glp-grok-bridge --restart unless-stopped --network glp-net \
  --read-only --user 65534:65534 -e GLP_TOKEN \
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
