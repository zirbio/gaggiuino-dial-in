# Grok: el mismo asistente de dial-in, conectado a la máquina

Esta carpeta prepara Grok para que recomiende con las mismas reglas y los mismos datos que el skill de Claude Code.

| Pieza | Qué es |
|---|---|
| [`instructions.md`](instructions.md) | Instrucciones del asistente: equipo, herramientas, cómo analizar y recomendar, perfiles y pruebas en curso. |
| [`../ios/dial-in-project-context.md`](../ios/dial-in-project-context.md) | Base de conocimiento completa (todo el skill en un archivo). |
| Conector `/mcp` | MCP de GLP: shots, curvas, cafés, notas. |
| Conector `/extra/mcp` | [Puente](../tools/glp-grok-bridge/): perfil exacto de cada shot, perfiles instalados en la Gaggiuino y asignar café y dosis. |

## Configuración en grok.com

1. **Conectores.** Los dos ya están dados de alta (ver el [README del puente](../tools/glp-grok-bridge/README.md)):
   - `https://<host>.ts.net:10000/<clave>/mcp`
   - `https://<host>.ts.net:10000/<clave>/extra/mcp`

   Desde la versión 1.1.0 el puente ofrece también `get_shot_profile` y `list_machine_profiles`. Si Grok no las ve, desconecta y vuelve a conectar el conector `/extra/mcp` para que relea la lista de herramientas.
2. **Proyecto.** Crea un proyecto (p. ej. "Gaggia dial-in"):
   - Pega `instructions.md` como instrucciones del proyecto.
   - Sube `ios/dial-in-project-context.md` como archivo de conocimiento.
   - Activa los dos conectores en el proyecto.

   Si tu Grok no tiene proyectos, pega `instructions.md` en las instrucciones personalizadas y adjunta el archivo de conocimiento al empezar la conversación.
3. **Prueba.** Pregunta "analiza mi último shot". Grok debería llamar a `list_shots`, `get_shot_profile` y `get_shot`, y nombrar el perfil real.

## Mantenerlo alineado

Cuando cambie el skill (perfiles, reglas o pruebas en curso):

1. Actualiza `instructions.md` si cambian reglas, perfiles instalados o pruebas en curso.
2. Regenera `ios/dial-in-project-context.md` (SKILL.md sin la parte de GLP + archivos de referencia + `profiles/*.md`).
3. Vuelve a pegar las instrucciones y a subir el archivo en el proyecto de Grok.
4. Si cambias `server.py`, reinicia el contenedor `glp-grok-bridge`.

Grok puede escribir en GLP (estrellas, notas, molienda, café y dosis) porque los conectores lo permiten; las instrucciones le limitan a hacerlo solo cuando se lo pidas. No puede tocar perfiles ni ajustes de la máquina: las herramientas de máquina solo hacen `GET`.
